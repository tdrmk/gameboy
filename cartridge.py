try:
    from cython import compiled
except ImportError:
    compiled = False

from time import time
import array

rom_info = {
    0: {'size': 32768, 'banks': 2},  # 32kB
    1: {'size': 65536, 'banks': 4},  # 64kB
    2: {'size': 131072, 'banks': 8},  # 128kB
    3: {'size': 262144, 'banks': 16},  # 256kB
    4: {'size': 524288, 'banks': 32},  # 512kB
    5: {'size': 1048576, 'banks': 64},  # 1MB
    6: {'size': 2097152, 'banks': 128},  # 2MB
    0x52: {'size': 1179648, 'banks': 72},  # 1.125MB
    0x53: {'size': 1310720, 'banks': 80},  # 1.25MB
    0x54: {'size': 1572864, 'banks': 96},  # 1.5MB
}

ram_info = {
    0: {'size': 0, 'banks': 0},  # None
    1: {'size': 2048, 'banks': 1},  # 2kB
    2: {'size': 8192, 'banks': 1},  # 8kB
    3: {'size': 32768, 'banks': 4},  # 32kB
    4: {'size': 131072, 'banks': 16},  # 128kB
}


def get_cartridge(filename):
    with open(filename, 'rb') as f:
        contents = f.read()
    title = contents[0x134:0x143].strip(b'\x00')
    print(f'Game: {title.decode()}')
    cartridge_type = contents[0x147]
    print(f'0x0143:{contents[0x143]:02X} 0x146:{contents[0x0146]:02X}')
    num_rom_banks = rom_info[contents[0x0148]]['banks']
    num_ram_banks = ram_info[contents[0x0149]]['banks']
    if cartridge_type == 0x00:
        print('Cartridge has ROM')
        return NoController(contents, has_ram=False)
    elif cartridge_type == 0x08 or cartridge_type == 0x09:
        print('Cartridge has ROM + RAM')
        return NoController(contents, has_ram=True)
    elif cartridge_type == 0x01:
        print('Cartridge has ROM + MBC1')
        return MBC1(contents, num_rom_banks, num_ram_banks)
    elif cartridge_type == 0x02 or cartridge_type == 0x03:
        print('Cartridge has ROM + MBC1 + RAM')
        return MBC1(contents, num_rom_banks, num_ram_banks)
    elif cartridge_type == 0x12 or cartridge_type == 0x13:
        print('Cartridge has ROM + MBC3 + RAM')
        return MBC3(contents, num_rom_banks, num_ram_banks)
    else:
        raise NotImplementedError(f'Cartridge type {cartridge_type:02X} not implemented!')


class Controller:
    def read_byte(self, address):
        pass

    def write_byte(self, address, byte):
        pass


class NoController(Controller):
    def __init__(self, contents, has_ram=False):
        self.contents = contents
        self.has_ram = has_ram
        if self.has_ram:  # 8kB RAM if it has any
            ram = bytearray(8192)
            self.ram = ram

    def read_byte(self, address):
        if 0x0000 <= address <= 0x7FFF:
            return self.contents[address]
        elif self.has_ram and 0xA000 <= address <= 0xBFFF:
            return self.ram[address & 0x1FFF]
        return 0x00

    def write_byte(self, address, byte):
        if self.has_ram and 0xA000 <= address <= 0xBFFF:
            self.ram[address & 0x1FFF] = byte


class MBC1(Controller):
    def __init__(self, contents, num_rom_banks, num_ram_banks):
        self.num_rom_banks = num_rom_banks
        self.num_ram_banks = num_ram_banks

        if compiled:
            self.rom_banks = memoryview(bytearray(contents)).cast('B', shape=(num_rom_banks, 16384))
            self.ram_banks = [array.array('B', [0] * 8192) for _ in range(4)]
        else:
            self.rom_banks = [contents[16384 * i: 16384 * (i + 1)] for i in range(num_rom_banks)]
            self.ram_banks = [array.array('B', [0] * 8192) for _ in range(4)]
        self.ram_enable = False  # Flag to indicate if ram is enabled or not
        self.selected_ram_bank = 0
        self.selected_rom_bank = 1

        # Controller exists in either one of the modes (RAM or ROM banking modes).
        self.rom_banking_mode = True

    def read_byte(self, address):
        if 0x0000 <= address <= 0x3FFF:
            # ROM Bank 0
            return self.rom_banks[0][address]
        elif 0x4000 <= address <= 0x7FFF:
            # From selected ROM bank
            return self.rom_banks[self.selected_rom_bank][address & 0x3FFF]
        elif self.ram_enable and 0xA000 <= address <= 0xBFFF:
            # From selected RAM Bank
            return self.ram_banks[self.selected_ram_bank][address & 0x1FFF]
        return 0x00

    def write_byte(self, address, byte):
        if self.ram_enable and 0xA000 <= address <= 0xBFFF:
            # Write to corresponding RAM bank
            self.ram_banks[self.selected_ram_bank][address & 0x1FFF] = byte

        # Writing to read-only addresses change the selected rom and ram banks,
        # enable ram and change banking mode.
        elif 0x0000 <= address <= 0x1FFF:
            # Enable RAM if lower 4 bits are 0x0A and if ram banks exists
            self.ram_enable = (byte & 0x0F == 0x0A) and (self.num_ram_banks > 0)

        elif 0x2000 <= address <= 0x3FFF:
            # Update the lower 5 bits of ROM bank number.
            self.selected_rom_bank = (self.selected_rom_bank & 0xE0) + (byte & 0x1F)
            if self.selected_rom_bank in (0x00, 0x20, 0x40, 0x60):
                # select the next bank instead
                self.selected_rom_bank += 1
            self.selected_rom_bank = self.selected_rom_bank % self.num_rom_banks

        elif 0x4000 <= address <= 0x5FFF:
            if self.rom_banking_mode:
                # Set the bit 5-6 of the rom bank number
                self.selected_rom_bank = ((byte & 0x03) << 5) + (self.selected_rom_bank & 0x1F)
                self.selected_rom_bank = self.selected_rom_bank % self.num_rom_banks
            else:  # RAM banking Mode
                # Set the RAM bank number in range 00-03
                self.selected_ram_bank = byte & 0x03
                self.selected_ram_bank = self.selected_ram_bank % self.num_ram_banks

        elif 0x6000 <= address <= 0x7FFF:
            if byte & 0x01 == 0x01:
                # RAM Banking mode (up to 32k RAM, 512KB ROM)
                self.rom_banking_mode = False
                self.selected_rom_bank &= 0x1F  # Only first 32 rom banks accessible
                self.selected_rom_bank = self.selected_rom_bank % self.num_rom_banks
            else:
                # ROM Banking mode (up to 8kB RAM, 2MB ROM)
                self.rom_banking_mode = True
                self.selected_ram_bank = 0  # Only first bank is accessible


class RTC:
    # A Crude implementation of RTC
    def __init__(self):
        self.start_time = time()
        # Latched values
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.day_lower = 0
        self.day_upper = 0
        self.halt = 0  # Active by default
        self.day_carry = 0

    # These reads and writes are different from usual and are not addresses
    # https://gbdev.gg8.se/wiki/articles/Memory_Bank_Controllers
    def read_register(self, address):
        if address == 0x08:  # RTC Seconds
            return self.seconds
        elif address == 0x09:  # RTC Minutes
            return self.minutes
        elif address == 0x0A:
            return self.hours
        elif address == 0x0B:
            return self.day_lower
        elif address == 0x0C:
            return self.day_upper + (self.halt << 6) + (self.day_carry << 7)
        return 0x00

    def write_register(self, address, byte):
        if address == 0x08:
            self.seconds = byte
        elif address == 0x09:
            self.minutes = byte
        elif address == 0x0A:
            self.hours = byte
        elif address == 0x0B:
            self.day_lower = byte
        elif address == 0x0C:
            self.day_upper = byte & 0b1
            self.halt = (byte >> 6) & 0b1
            # TODO: HALT and DAY CARRY
            self.day_carry = (byte >> 7) & 0b1

    def write_byte(self, address, byte):
        # Writes for enabling latch clock data 0x6000-0x7FFF
        if byte == 0x01:
            latch_time = time()
            self.seconds = int(latch_time - self.start_time) % 60
            self.minutes = int((latch_time - self.start_time) / 60) % 60
            self.hours = int((latch_time - self.start_time) / 3600) % 24
            day_counter = int((latch_time - self.start_time) / 86400)
            self.day_lower = day_counter % 256
            self.day_upper = (day_counter >> 8) & 0b1
            if day_counter > 512:
                # It is reset only on write
                self.day_carry = 1
            if day_counter > 512:
                # Update the start time by
                self.start_time += ((day_counter >> 9) << 9) * 86400


class MBC3(Controller):
    def __init__(self, contents, num_rom_banks, num_ram_banks):
        self.num_rom_banks = num_rom_banks
        self.num_ram_banks = num_ram_banks
        # self.rom_banks = [contents[16384 * i:16384 * (i + 1)] for i in range(num_rom_banks)]
        # self.ram_banks = [bytearray(8192) for _ in range(num_ram_banks)]
        if compiled:
            self.rom_banks = memoryview(bytearray(contents)).cast('B', shape=(num_rom_banks, 16384))
            self.ram_banks = [array.array('B', [0] * 8192) for _ in range(16)]
        else:
            self.rom_banks = [contents[16384 * i: 16384 * (i + 1)] for i in range(num_rom_banks)]
            self.ram_banks = [array.array('B', [0] * 8192) for _ in range(16)]

        self.ram_enable = False  # Flag to indicate if ram/rtc is enabled or not
        self.selected_ram_bank = 0  # Value in range 0x00-0x07 indicate external RAM bank, 0x08-0x0C RTC Register
        # TODO: Implement RTC Register
        self.selected_rom_bank = 1

        # Controller exists in either one of the modes (RAM banking modes or RTC Register Select).
        self.ram_banking_mode = True

        self.rtc = RTC()

    def read_byte(self, address):
        if 0x0000 <= address <= 0x3FFF:
            # ROM Bank 0
            return self.rom_banks[0][address]
        elif 0x4000 <= address <= 0x7FFF:
            # From selected ROM bank
            return self.rom_banks[self.selected_rom_bank][address & 0x3FFF]
        elif self.ram_enable and 0xA000 <= address <= 0xBFFF:
            if 0x08 <= self.selected_ram_bank <= 0x0C:
                # TODO: Use RTC Register
                # print('Reading from RTC Register ??')
                return self.rtc.read_register(self.selected_ram_bank)
                pass
            # From selected RAM Bank
            return self.ram_banks[self.selected_ram_bank][address & 0x1FFF]
        return 0x00

    def write_byte(self, address, byte):
        if self.ram_enable and 0xA000 <= address <= 0xBFFF:
            if 0x08 <= self.selected_ram_bank <= 0x0C:
                # TODO: Use RTC Register
                # print('Writing to RTC Register ??')
                self.rtc.write_register(self.selected_ram_bank, byte)
            else:
                # Write to corresponding RAM bank
                self.ram_banks[self.selected_ram_bank][address & 0x1FFF] = byte

        # Writing to read-only addresses change the selected rom and ram banks,
        # enable ram and change banking mode.
        elif 0x0000 <= address <= 0x1FFF:
            # Enable RAM if lower 4 bits are 0x0A and if ram banks exists
            self.ram_enable = (byte & 0x0F == 0x0A) and (self.num_ram_banks > 0)

        elif 0x2000 <= address <= 0x3FFF:
            # Contains all the 7 bits of ROM bank number.
            self.selected_rom_bank = byte & 0x7F
            if self.selected_rom_bank == 0x00:
                # when bank 0 selected use the bank 1 instead
                self.selected_rom_bank = 0x01
            self.selected_rom_bank = self.selected_rom_bank % self.num_rom_banks

        elif 0x4000 <= address <= 0x5FFF:
            # Based on written value either RAM (0x00-0x07) or RTC register (0x08-0x0C) is mapped
            self.selected_ram_bank = byte

        elif 0x6000 <= address <= 0x7FFF:
            # TODO: Use RTC Register
            # print('Latching RTC Register ??')
            self.rtc.write_byte(address, byte)
