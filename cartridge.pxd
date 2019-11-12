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


cdef class MBC3(Controller):
    cdef int num_rom_banks
    cdef int num_ram_banks
    cdef uint8_t[:, :] rom_banks
    cdef uint8_t[16][8192] ram_banks
    cdef bint ram_enable
    cdef int selected_ram_bank
    cdef int selected_rom_bank
    cdef bint ram_banking_mode

    cdef uint8_t read_byte(self, uint16_t address)
    cdef void write_byte(self, uint16_t address, uint8_t byte)


cpdef Controller get_cartridge(char *filename)