from libc.stdint cimport uint8_t, uint16_t, uint32_t
cimport cpu
cimport bootrom
cimport cartridge
cimport graphics
cimport joypad
cimport timer

import cython

cdef class MMU:
    cdef uint8_t[8192] work_ram
    cdef uint8_t[127] high_ram
    cdef uint8_t[96] unusable_io_ports
    cdef uint8_t[128] io_ports
    cdef bint boot_rom_enabled
    cdef bootrom.BootROM boot_rom
    cdef cartridge.Controller cartridge
    cdef graphics.GPU gpu
    cdef joypad.Joypad joypad
    cdef timer.Timer timer
    cdef uint8_t dma
    cdef uint8_t interrupt_request
    cdef uint8_t interrupt_enable
    cdef object mixer

    cdef uint8_t read_byte(self, uint16_t address)
    @cython.locals(src=uint16_t, dst=uint16_t, i=uint16_t)
    cdef void write_byte(self, uint16_t address, uint8_t byte)

    cdef void save(self, object f)
    cdef void load(self, object f)