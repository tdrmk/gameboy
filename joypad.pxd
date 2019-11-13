from libc.stdint cimport uint8_t, uint16_t

from cpu cimport CPU

cdef uint8_t V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD

cdef int P10, P11, P12, P13
cdef uint8_t RIGHT, LEFT, UP, DOWN, A, B, SELECT, START


cdef uint8_t reset_bit(uint8_t x, uint8_t bit)
cdef uint8_t set_bit(uint8_t x, uint8_t bit)

cdef class Joypad:
    cdef bint right 
    cdef bint left 
    cdef bint up 
    cdef bint down 
    cdef bint A 
    cdef bint B 
    cdef bint select 
    cdef bint start 
    cdef bint buttons 
    cdef bint directions     
    cdef CPU cpu
    cpdef void attach_cpu(self, CPU cpu)
    cdef void handle_key(self, uint8_t key, uint8_t pressed)
    cdef void write_byte(self, uint8_t byte)
    cdef uint8_t read_byte(self)

    cdef void save(self, object f)
    cdef void load(self, object f)