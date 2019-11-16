cimport cython
cimport numpy as np

cdef int Fs
cdef class Channel:
    cdef set_enable(self, bint enable)
    cdef void set_output(self, bint out1, bint out2)
    cdef void set_master_volume(self, float vol1, float vol2)
    cdef void play(self, list wave, float freq)
    cdef void stop(self)

cdef class PyGameChannel(Channel):
    cdef object channel
    cdef bint output1, output2
    cdef bint enabled, playing

    @cython.locals(n=int, N=int, s=float, snd_array=np.ndarray)
    cdef void play(self, list wave, float freq)
