import numpy as np
import sdl2.sdlmixer as mixer
import ctypes
import sdl2
# Fs = 131072 # Frequency of mixer
Fs = 44100


sdl2.SDL_Init(sdl2.SDL_INIT_AUDIO | sdl2.SDL_INIT_VIDEO | sdl2.SDL_INIT_TIMER)
mixer.Mix_OpenAudio(Fs, sdl2.AUDIO_S8, 1, 4096)
mixer.Mix_AllocateChannels(4)

class Channel:
    def __init__(self, _id):
        # Unsigned 8 bit representation of sound, stereo output
        self.channel = _id
        self.output =  False
        self.enabled = False
        self.playing = False

    def set_output(self, out1, out2):
        self.output = out1 or out2

    def set_master_volume(self, vol1, vol2):
        # volume must be between 0.0 and 1.0
        volume = int(max(vol1, vol2) * 7 * 16)
        mixer.Mix_Volume(self.channel, volume)

    def set_enable(self, enable):
        self.enabled = enable
        if not enable:
            self.stop()

    def play(self, wave, freq):
        # Plays a given waveform in specified frequency
        # Example: say to play 100Hz signal, pass ([1, 0], 100)
        # To alter duty cycle of 100Hz signal, pass ([1, 0, 0, 0], 100)
        # Note: wave is of type array (python array module)
        # Note: sound only plays if playable. and is approximated to nearest possible frequency
        n = len(wave)
        if self.enabled and self.output and Fs > freq > 0 and n > 0:
            N = int(Fs / freq)  # Lower integer
            s = Fs / freq / n
            if N > 0 and any(wave):  # Number of samples of the wave must be greater than 0 to output
                # volume is taken into account while mixing

                music = np.array([wave[int(i / s)] for i in range(N)], dtype=np.uint8)
                ptr = music.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))
                print('Creating chunk')
                chunk = mixer.Mix_Chunk(0, ptr , N, 128)
                print('Creating chunk complete', chunk)
                self.stop()
                print(mixer.Mix_Playing(self.channel))
                print('Halting complete')
                mixer.Mix_PlayChannel(self.channel, chunk, 1000)
                print('Playing chunk complete')
                self.playing = True
                # Starting playing
                return
        # If sound was not played
        if self.playing:
            # then stop playing if any existing playing sounds
            self.stop()

    def stop(self):
        if self.playing:
            # If playing something stop it !!
            self.playing = False
            print('Pausing Channel')
            mixer.Mix_HaltChannel(self.channel)
            print('Pausing Channel Complete')
