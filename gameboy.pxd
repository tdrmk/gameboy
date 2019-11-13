from libc.stdint cimport uint8_t, uint16_t, uint32_t
cimport cpu
cimport bootrom
cimport cartridge
cimport graphics
cimport joypad
cimport timer
cimport memory
cimport display
from cpython.array cimport array
import cython

cdef uint8_t V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD

cdef class Gameboy:
    cdef bootrom.BootROM boot_rom
    cdef cartridge.Controller cartridge
    cdef graphics.GPU gpu
    cdef joypad.Joypad joypad
    cdef timer.Timer timer
    cdef memory.MMU memory
    cdef cpu.CPU cpu
    cdef display.Display display

    @cython.locals(ly=uint8_t, frame=array)
    cdef void tick_frame(self)

    @cython.locals(cycles=uint32_t, ticks=uint32_t)
    cdef void handle_cycles(self, uint32_t num_cycles)

    cpdef void mainloop(self)

    cdef void save(self)
    cpdef void load(self, str filename)