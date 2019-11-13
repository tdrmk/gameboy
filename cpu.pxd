from libc.stdint cimport uint8_t, uint16_t, uint32_t

import cython
from memory cimport MMU
cdef uint8_t V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD
cdef uint16_t IE_ADDRESS, IF_ADDRESS
cimport instructions

cdef class CPU:
    cdef uint16_t PC
    cdef uint16_t SP
    cdef uint8_t A
    cdef uint8_t B
    cdef uint8_t C
    cdef uint8_t D
    cdef uint8_t E
    cdef uint16_t HL

    cdef bint FLAG_Z
    cdef bint FLAG_N
    cdef bint FLAG_H
    cdef bint FLAG_C

    cdef bint ime
    cdef MMU memory

    cdef void request_interrupt(self, uint8_t interrupt)

    @cython.locals(ie=uint8_t, ir=uint8_t, enabled_interrupts=uint8_t)
    cdef bint check_interrupts(self)

    @cython.locals(opcode=uint16_t)
    cdef uint32_t tick(self)

    cdef void save(self, object f)
    cdef void load(self, object f)