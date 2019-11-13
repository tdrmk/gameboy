from libc.stdint cimport uint8_t, uint16_t, uint32_t
from cpu cimport CPU
from cpython.array cimport array

import cython



cdef uint32_t[4] color_palette
cdef uint8_t V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD

cdef class GPU:
    cdef uint8_t[8192] video_ram
    cdef uint8_t[160] sprite_attrib
    cdef uint8_t[384 * 8 * 8] tiles_unpacked
    cdef uint8_t[144 * 4] line_params

    cdef uint8_t lcdc
    cdef uint8_t stat
    cdef uint8_t scy
    cdef uint8_t scx
    cdef uint8_t ly
    cdef uint8_t lyc
    cdef uint8_t bgp
    cdef uint8_t[4] bgp_palette
    cdef uint8_t obp0
    cdef uint8_t[4] obp0_palette
    cdef uint8_t obp1
    cdef uint8_t[4] obp1_palette

    cdef uint8_t wy
    cdef uint8_t wx

    # Flags
    cdef bint display_enable
    cdef bint display_window
    cdef bint display_background
    cdef bint display_sprite
    cdef bint large_tiles
    # addresses in video ram
    cdef uint16_t window_tile_map
    cdef uint16_t bkgrnd_tile_map
    cdef uint16_t tile_data_addr
    cdef bint signed_addr

    # Need cpu to raise interrupt
    cdef CPU cpu
    cdef array frame_bytes
    cdef uint32_t[:,:] frame_buffer

    cpdef void attach_cpu(self, CPU cpu)
    @cython.locals(high_byte=uint8_t, low_byte=uint8_t, tr=uint16_t)
    cdef void set_vram(self, uint16_t address, uint8_t byte)
    cdef void set_lcdc(self, uint8_t byte)
    cdef void set_bgp(self, uint8_t byte)
    cdef void set_obp0(self, uint8_t byte)
    cdef void set_obp1(self, uint8_t byte)
    cdef void scan_line(self, uint16_t y)
    cdef void set_stat_mode(self, uint8_t mode)
    cdef void check_coincidence(self)

    @cython.locals(
        y=int, x=int, n=int,
        scy=int, scx=int,
        wy=int, wx=int,
        wt=int, bt=int,
        pr=bint, yf=bint, xf=bint,
        st=int, sprite_height=int,
        dy=int, dx=int, oy=int, ox=int,
        color=int
        )
    cdef array render(self)

    cdef void save(self, object f)
    cdef void load(self, object f)