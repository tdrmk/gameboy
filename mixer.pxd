from libc.stdint cimport uint8_t, uint16_t, uint32_t
from channel cimport Channel
import cython

cdef list get_waveform(int)

cdef class Sound1:
    cdef uint8_t NR10, NR11, NR12, NR13, NR14
    cdef Channel channel
    cdef bint enabled
    cdef int counter, steps

    cdef bint sweep_dec, sweep_enabled
    cdef int sweep_period, sweep_shift, sweep_counter, freq_x
    cdef float frequency

    cdef bint volume_amplify, volume_enabled
    cdef int volume_initial, volume_period, volume_counter, volume

    cdef list wave
    cdef bint length_enabled
    cdef int length

    cdef void _stop(self)

    @cython.locals(wave=list)
    cdef void _play(self)

    cdef void reset(self)
    cdef void trigger(self)
    cdef void nr10(self, uint8_t byte)
    cdef void nr11(self, uint8_t byte)
    cdef void nr12(self, uint8_t byte)
    cdef void nr13(self, uint8_t byte)
    cdef void nr14(self, uint8_t byte)


    @cython.locals(freq_x=int)
    cdef void update_frequency(self)
    @cython.locals(volume=int)
    cdef void update_volume(self)
    cdef void update_length(self)

    cdef void handle_freq_sweep(self)
    cdef void handle_length_ctr(self)
    cdef void handle_vol_env(self)
    cdef void save(self, object f)
    cdef void load(self, object f)
    cdef void tick(self, uint32_t ticks)

cdef class Sound3:
    cdef uint8_t NR30, NR31, NR32, NR33, NR34
    cdef Channel channel
    cdef bint enabled
    cdef int counter, steps

    cdef int length
    cdef bint length_enabled

    cdef list wave
    cdef float frequency
    cdef float volume

    cdef void _stop(self)

    @cython.locals(wave=list)
    cdef void _play(self)

    cdef void reset(self)
    @cython.locals(x=int)
    cdef void trigger(self)

    cdef void nr30(self, uint8_t byte)
    cdef void nr31(self, uint8_t byte)
    cdef void nr32(self, uint8_t byte)
    cdef void nr33(self, uint8_t byte)
    cdef void nr34(self, uint8_t byte)

    cdef wave_pattern_ram(self, uint8_t offset, uint8_t byte)
    cdef void update_length(self)
    cdef void handle_length_ctr(self)
    cdef void tick(self, uint32_t ticks)
    cdef void save(self, object f)
    cdef void load(self, object f)

cdef list lfsr(int bits)


cdef class Sound4:
    cdef uint8_t NR41, NR42, NR43, NR44
    cdef Channel channel
    cdef bint enabled
    cdef int counter, steps

    cdef bint lfsr_mode
    cdef int clock_shift
    cdef float divisor_code
    cdef float frequency

    cdef int volume_initial, volume_period, volume_counter, volume
    cdef bint volume_amplify, volume_enabled

    cdef list wave_bit15, wave_bit7, wave
    cdef int length
    cdef bint length_enabled

    cdef void _stop(self)

    @cython.locals(wave=list)
    cdef void _play(self)

    cdef void reset(self)
    cdef void trigger(self)

    cdef void nr41(self, uint8_t byte)
    cdef void nr42(self, uint8_t byte)

    @cython.locals(divisor_code=int)
    cdef void nr43(self, uint8_t byte)
    cdef void nr44(self, uint8_t byte)


    @cython.locals(volume=int)
    cdef void update_volume(self)
    cdef void update_length(self)

    cdef void handle_length_ctr(self)
    cdef void handle_vol_env(self)
    cdef void save(self, object f)
    cdef void load(self, object f)
    cdef void tick(self, uint32_t ticks)

cdef class Mixer:
    cdef Channel channel1, channel2, channel3, channel4
    cdef Sound1 sound1
    cdef Sound1 sound2
    cdef Sound3 sound3
    cdef Sound4 sound4
    cdef uint8_t NR50, NR51, NR52
    cdef bint enabled

    @cython.locals(offset=uint8_t)
    cdef uint8_t read_byte(self, uint16_t address)
    @cython.locals(v1=uint8_t, v2=uint8_t)
    cdef void nr50(self, uint8_t byte)
    cdef void nr51(self, uint8_t byte)
    cdef void nr52(self, uint8_t byte)
    cdef void write_byte(self, uint16_t address, uint8_t byte)
    cdef void tick(self, uint32_t ticks)
    cdef void save(self, object f)
    cdef void load(self, object f)

