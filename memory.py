import struct

# SIZES
WORK_RAM = 8192
HIGH_RAM = 127
UNUSABLE_IO_PORTS = 96
IO_PORTS = 128

class MMU:
    # Memory management Unit
    def __init__(self, boot_rom, cartridge, gpu, joypad, timer, mixer):
        work_ram = bytearray(WORK_RAM)
        high_ram = bytearray(HIGH_RAM)
        unusable_io_ports = bytearray(UNUSABLE_IO_PORTS)
        io_ports = bytearray(IO_PORTS)
        self.work_ram = work_ram
        self.high_ram = high_ram
        self.unusable_io_ports = unusable_io_ports
        self.io_ports = io_ports  # Contains the i/o port as well unusable io ports

        self.boot_rom_enabled = True
        self.boot_rom = boot_rom
        self.cartridge = cartridge
        self.gpu = gpu
        self.joypad = joypad
        self.timer = timer
        self.mixer = mixer

        # I/O Registers
        self.dma = 0
        self.interrupt_request = 0
        self.interrupt_enable = 0

    def save(self, f):
        f.write(struct.pack('<BBBB', self.boot_rom_enabled, self.dma, self.interrupt_request, self.interrupt_enable))
        for i in range(WORK_RAM):
            f.write(self.work_ram[i].to_bytes(1, 'little'))
        for i in range(HIGH_RAM):
            f.write(self.high_ram[i].to_bytes(1, 'little'))
        for i in range(UNUSABLE_IO_PORTS):
            f.write(self.unusable_io_ports[i].to_bytes(1, 'little'))
        for i in range(IO_PORTS):
            f.write(self.io_ports[i].to_bytes(1, 'little'))

    def load(self, f):
        self.boot_rom_enabled, self.dma, self.interrupt_request,\
            self.interrupt_enable = struct.unpack('<BBBB', f.read(4))
        for i in range(WORK_RAM):
            self.work_ram[i] = ord(f.read(1))
        for i in range(HIGH_RAM):
            self.high_ram[i] = ord(f.read(1))
        for i in range(UNUSABLE_IO_PORTS):
            self.unusable_io_ports[i] = ord(f.read(1))
        for i in range(IO_PORTS):
            self.io_ports[i] = ord(f.read(1))

    def read_byte(self, address):
        if 0 <= address <= 0x7FFF:
            if self.boot_rom_enabled and 0x0000 <= address <= 0x00FF:
                return self.boot_rom.read_byte(address)
            # 32kB Cartridge ROM
            return self.cartridge.read_byte(address)
        elif 0x8000 <= address <= 0x9FFF:
            # 8kB Video RAM (VRAM)
            return self.gpu.video_ram[address & 0x1FFF]
        elif 0xA000 <= address <= 0xBFFF:
            # 8kB External RAM (in cartridge, switchable if any)
            return self.cartridge.read_byte(address)
        elif 0xC000 <= address <= 0xDFFF:
            # 8kB Internal RAM (WRAM)
            return self.work_ram[address & 0x1FFF]
        elif 0xE000 <= address <= 0xFDFF:
            # Echo of 8kB Internal RAM
            return self.work_ram[address & 0x1FFF]
        elif 0xFE00 <= address <= 0xFE9F:
            # 160B Sprite Attribute Memory (OAM)
            return self.gpu.sprite_attrib[address & 0xFF]
        elif 0xFEA0 <= address <= 0xFEFF:
            # Empty but unusable for I/O
            return self.unusable_io_ports[address - 0xFEA0]
        elif 0xFF00 <= address <= 0xFF7F:
            # 0xFEA0 - 0xFF4B I/O Ports
            # 0xFF4C - 0xFF7F Empty but unusable for I/O
            if address == 0xFF0F:
                return self.interrupt_request
            elif address == 0xFF00:
                return self.joypad.read_byte()
            elif address == 0xFF40:
                return self.gpu.lcdc
            elif address == 0xFF41:
                return self.gpu.stat
            elif address == 0xFF42:
                return self.gpu.scy
            elif address == 0xFF43:
                return self.gpu.scx
            elif address == 0xFF44:
                return self.gpu.ly
            elif address == 0xFF45:
                return self.gpu.lyc
            elif address == 0xFF46:
                return self.dma
            elif address == 0xFF47:
                return self.gpu.bgp
            elif address == 0xFF48:
                return self.gpu.obp0
            elif address == 0xFF49:
                return self.gpu.obp1

            elif address == 0xFF4A:
                return self.gpu.wy
            elif address == 0xFF4B:
                return self.gpu.wx
            elif address == 0xFF04:
                return self.timer.div
            elif address == 0xFF05:
                return self.timer.tima
            elif address == 0xFF06:
                return self.timer.tma
            elif address == 0xFF07:
                return self.timer.tac
            if 0xFF10 <= address <= 0xFF3F:
                return self.mixer.read_byte(address)
            return self.io_ports[address & 0xFF]
        elif 0xFF80 <= address <= 0xFFFE:
            return self.high_ram[address & 0x7F]
        elif address == 0xFFFF:
            return self.interrupt_enable

    def write_byte(self, address, byte):
        address &= 0xFFFF
        byte &= 0xFF
        if 0 <= address <= 0x7FFF:
            self.cartridge.write_byte(address, byte)
        elif 0x8000 <= address <= 0x9FFF:
            self.gpu.set_vram(address & 0x1FFF, byte)
        elif 0xA000 <= address <= 0xBFFF:
            self.cartridge.write_byte(address, byte)
        elif 0xC000 <= address <= 0xDFFF:
            # 8kB Internal RAM (WRAM)
            self.work_ram[address & 0x1FFF] = byte
        elif 0xE000 <= address <= 0xFDFF:
            # Echo of 8kB Internal RAM
            self.work_ram[address & 0x1FFF] = byte
        elif 0xFE00 <= address <= 0xFE9F:
            # 160B Sprite Attribute Memory (OAM)
            self.gpu.sprite_attrib[address & 0xFF] = byte
        elif 0xFEA0 <= address <= 0xFEFF:
            # Empty but unusable for I/O
            self.unusable_io_ports[address - 0xFEA0] = byte
        elif 0xFF00 <= address <= 0xFF7F:
            # 0xFEA0 - 0xFF4B I/O Ports
            # 0xFF4C - 0xFF7F Empty but unusable for I/O
            if address == 0xFF0F:
                self.interrupt_request = byte
                # Registers
            elif address == 0xFF00:
                self.joypad.write_byte(byte)
            elif address == 0xFF40:
                self.gpu.set_lcdc(byte)
            elif address == 0xFF41:
                self.gpu.stat &= 0x07  # Keep the first 3-bits
                self.gpu.stat |= byte & 0xF8
            elif address == 0xFF42:
                self.gpu.scy = byte
            elif address == 0xFF43:
                self.gpu.scx = byte

            # elif address == 0xFF44:
            #     self.gpu.ly = 0
            elif address == 0xFF45:
                self.gpu.lyc = byte
            elif address == 0xFF46:
                # Writing launches DMA Transfers to OAM from ROM or RAM
                # Source: XX00 - XX9F; Destination: FE00 - FE9F
                self.dma = byte
                src, dst = byte << 8, 0xFE00
                # print(f'DMA Initiated {byte:02X}')
                for i in range(0x00A0):
                    self.write_byte(dst + i, self.read_byte(src + i))
            elif address == 0xFF47:
                self.gpu.set_bgp(byte)
            elif address == 0xFF48:
                self.gpu.set_obp0(byte)
            elif address == 0xFF49:
                self.gpu.set_obp1(byte)
            elif address == 0xFF50:
                if byte == 0x01:
                    # print('BOOT DISABLED')
                    # Un-maps the boot ROM and first 255 bytes of address space is effectively mapped.
                    self.boot_rom_enabled = False
            elif address == 0xFF4A:
                self.gpu.wy = byte
            elif address == 0xFF4B:
                self.gpu.wx = byte
            elif address == 0xFF04:
                self.timer.div = 0
            elif address == 0xFF05:
                self.timer.tima = byte
            elif address == 0xFF06:
                self.timer.tma = byte
            elif address == 0xFF07:
                self.timer.tac = byte
            if 0xFF10 <= address <= 0xFF3F:
                self.mixer.write_byte(address, byte)
            else:
                self.io_ports[address & 0xFF] = byte
        elif 0xFF80 <= address <= 0xFFFE:
            self.high_ram[address & 0x7F] = byte
        elif address == 0xFFFF:
            self.interrupt_enable = byte
