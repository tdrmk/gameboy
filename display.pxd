from libc.stdint cimport uint8_t, uint16_t
cimport numpy as np
ctypedef np.uint32_t DTYPE_t

from gameboy cimport Gameboy
cimport joypad

cdef dict key_map
cdef uint8_t WIDTH, HEIGHT

cdef class Display:
    cdef Gameboy gameboy
    cdef joypad.Joypad joypad
    cdef bint blank
    cdef bint stretch
    cdef object window

    cdef void _render_blank(self)
    cdef void _handle_events(self)
    cdef void _render(self, np.ndarray[DTYPE_t, ndim=2] frame)
    cdef void render_blank(self)
    cdef void render(self, np.ndarray[DTYPE_t, ndim=2] frame)
