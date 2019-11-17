from libc.stdint cimport uint8_t, uint16_t, uint32_t
cimport cpu
cimport bootrom
cimport cartridge
cimport graphics
cimport joypad
cimport timer
cimport memory
cimport display
cimport mixer
cimport numpy as np
ctypedef np.uint32_t DTYPE_t
import cython

cdef uint8_t V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD
cdef list frequencies

cdef class Gameboy:
    cdef bootrom.BootROM boot_rom
    cdef cartridge.Controller cartridge
    cdef graphics.GPU gpu
    cdef joypad.Joypad joypad
    cdef timer.Timer timer
    cdef memory.MMU memory
    cdef cpu.CPU cpu
    cdef display.Display display
    cdef mixer.Mixer mixer
    cdef int f_index
    cdef float frame_duration

    cdef void toggle_frequency(self)
    @cython.locals(ly=uint8_t, frame=np.ndarray, start_time=float, end_time=float, time_taken=float)
    cdef void tick_frame(self)

    @cython.locals(cycles=uint32_t, ticks=uint32_t)
    cdef void handle_cycles(self, uint32_t num_cycles)

    cpdef void mainloop(self)

    cdef void save(self)
    cpdef void load(self, str filename)
