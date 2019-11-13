from libc.stdint cimport uint8_t, uint16_t
from cpython.array cimport array

from gameboy cimport Gameboy
cimport sdl2
cimport joypad

cdef class Display:
    cdef Gameboy gameboy
    cdef joypad.Joypad joypad
    cdef bint blank
    cdef bint stretch
    cdef sdl2.SDL_Window *window
    cdef sdl2.SDL_Renderer *renderer
    cdef sdl2.SDL_Texture *texture

    cdef void _render_blank(self)
    cdef void _handle_events(self)
    cdef void _render(self, void * frame)
    cdef void render_blank(self)
    cdef void render(self, array frame)
