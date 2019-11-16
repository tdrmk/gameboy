import pygame
import numpy as np

# Fs = 131072 # Frequency of mixer
Fs = 44100
pygame.mixer.init(frequency=Fs, size=-8, channels=2)  # Unsigned 8 bit representation of sound, mono output


class MixerChannel:
    def __init__(self, _id):
        self.channel = pygame.mixer.Channel(_id)
        self.output1, self.output2 = False, False
        self.enabled = False
        self.playing = False

    def set_output(self, out1, out2):
        self.output1, self.output2 = out1, out2

    def set_master_volume(self, vol1, vol2):
        # volume must be between 0.0 and 1.0
        self.channel.set_volume(vol1, vol2)

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
        if self.enabled and (self.output1 or self.output2) and Fs > freq > 0 and n > 0:
            N = int(Fs / freq)  # Lower integer
            s = Fs / freq / n
            if N > 0 and any(wave):  # Number of samples of the wave must be greater than 0 to output
                # volume is taken into account while mixing
                self.channel.play(pygame.sndarray.make_sound(np.array(
                    [[wave[int(i/s)], wave[int(i/s)]] for i in range(N)], dtype=np.uint8)), loops=-1)
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
            self.channel.stop()
