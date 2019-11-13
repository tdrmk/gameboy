from libc.stdint cimport uint8_t, uint16_t, uint32_t
from cpu cimport CPU

import cython

cdef uint8_t V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD
cdef uint32_t[4] dividers

cdef class Timer:
    cdef uint8_t div
    cdef uint8_t tima
    cdef uint8_t tma
    cdef uint8_t tac
    cdef uint32_t div_counter
    cdef uint32_t tima_counter

    cdef CPU cpu
    cpdef void attach_cpu(self, CPU cpu)

    @cython.locals(divider=uint32_t)
    cdef void tick(self, uint32_t cycles)

    cdef void save(self, object f)
    cdef void load(self, object f)