from libc.stdint cimport uint8_t, uint16_t

cdef class BootROM:
    cdef uint8_t[256] contents
    cdef uint8_t read_byte(self, uint16_t address)