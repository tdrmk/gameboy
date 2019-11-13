import cython

cdef dict rom_info
cdef dict ram_info
from libc.stdint cimport uint8_t, uint16_t

cdef class Controller:
    cdef uint8_t read_byte(self, uint16_t address)
    cdef void write_byte(self, uint16_t address, uint8_t byte)

cdef class NoController(Controller):
    cdef uint8_t[0x8000] contents
    cdef uint8_t[8192] ram
    cdef bint has_ram

    cdef uint8_t read_byte(self, uint16_t address)
    cdef void write_byte(self, uint16_t address, uint8_t byte)

cdef class MBC1(Controller):
    cdef int num_rom_banks
    cdef int num_ram_banks
    cdef uint8_t[:, :] rom_banks
    cdef uint8_t[4][8192] ram_banks
    cdef bint ram_enable
    cdef int selected_ram_bank
    cdef int selected_rom_bank
    cdef bint rom_banking_mode

    cdef uint8_t read_byte(self, uint16_t address)
    cdef void write_byte(self, uint16_t address, uint8_t byte)


cdef class RTC:
    cdef float start_time
    cdef uint8_t seconds
    cdef uint8_t minutes
    cdef uint8_t hours
    cdef uint8_t day_lower
    cdef bint day_upper
    cdef bint halt
    cdef bint day_carry

    cdef uint8_t read_register(self, uint8_t address)
    cdef void write_register(self, uint8_t address, uint8_t byte)
    @cython.locals(day_counter=int, latch_time=float)
    cdef void write_byte(self, uint16_t address, uint8_t byte)


cdef class MBC3(Controller):
    cdef int num_rom_banks
    cdef int num_ram_banks
    cdef uint8_t[:, :] rom_banks
    cdef uint8_t[16][8192] ram_banks
    cdef bint ram_enable
    cdef int selected_ram_bank
    cdef int selected_rom_bank
    cdef bint ram_banking_mode
    cdef RTC rtc

    cdef uint8_t read_byte(self, uint16_t address)
    cdef void write_byte(self, uint16_t address, uint8_t byte)


cpdef Controller get_cartridge(char *filename)