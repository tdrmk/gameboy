import channel
import struct


# WAVEFORMS = {
#     # duty , pattern
#     0b00: [0, 0, 0, 0, 0, 0, 0, 1],  # 12.5%
#     0b01: [1, 0, 0, 0, 0, 0, 0, 1],  # 25.0%
#     0b10: [1, 0, 0, 0, 0, 1, 1, 1],  # 50.0%
#     0b11: [0, 1, 1, 1, 1, 1, 1, 0],  # 75.0%
# }


def get_waveform(i):
    # i: duty
    if i == 0b00:
        return [0, 0, 0, 0, 0, 0, 0, 1]  # 12.5%
    elif i == 0b01:
        return [1, 0, 0, 0, 0, 0, 0, 1]  # 25.0%
    elif i == 0b10:
        return [1, 0, 0, 0, 0, 1, 1, 1]  # 50.0%
    elif i == 0b11:
        return [0, 1, 1, 1, 1, 1, 1, 0]  # 75.0%


class Sound1:
    def __init__(self, channel):
        self.NR10 = 0
        self.NR11 = 0
        self.NR12 = 0
        self.NR13 = 0
        self.NR14 = 0
        self.channel = channel

        # Whether the sound is running or not. Used for NR52 as well
        self.enabled = False
        self._stop()  # Stop while initialize

        # frame sequencer (self.steps << 13 + self.counter)
        self.counter = 0
        self.steps = 0  # Used with the counter

        # for handling sweep
        # Extracted from register (SWEEPING)
        self.sweep_period = 0
        self.sweep_dec = False
        self.sweep_shift = 0
        # Internal (SWEEPING)
        self.sweep_counter = 0
        self.sweep_enabled = False
        self.freq_x = 0  # Frequency shadow register
        self.frequency = 0  # COMPUTED from shadow register

        # Envelope
        # Extracted (Envelop)
        self.volume_initial = 0
        self.volume_amplify = False
        self.volume_period = 0
        # Internal (Envelop)
        self.volume_enabled = False
        self.volume = 0  # The computed volume (4-bit)
        self.volume_counter = 0

        self.wave = get_waveform(0)
        # Length
        self.length_enabled = False
        self.length = 64

    def save(self, f):
        f.write(struct.pack('<BBBBB', self.NR10, self.NR11, self.NR12, self.NR13, self.NR14))
        f.write(struct.pack('<BII', self.enabled, self.counter, self.steps))
        f.write(struct.pack('<BBIIIIf', self.sweep_dec, self.sweep_enabled, self.sweep_period, self.sweep_shift,
                            self.sweep_counter, self.freq_x, self.frequency))
        f.write(struct.pack('<BBIIII', self.volume_amplify, self.volume_enabled,
                            self.volume_initial, self.volume_period, self.volume_counter, self.volume))
        f.write(struct.pack('<BI', self.length_enabled, self.length))
        for i in range(len(self.wave)):
            f.write(self.wave[i].to_bytes(1, 'little'))

    def load(self, f):
        self.NR10, self.NR11, self.NR12, self.NR13, self.NR14 = struct.unpack('<BBBBB', f.read(5))
        self.enabled, self.counter, self.steps = struct.unpack('<BII', f.read(9))
        self.sweep_dec, self.sweep_enabled, self.sweep_period, self.sweep_shift,\
            self.sweep_counter, self.freq_x, self.frequency = struct.unpack('<BBIIIIf', f.read(22))
        self.volume_amplify, self.volume_enabled, self.volume_initial, self.volume_period,\
            self.volume_counter, self.volume = struct.unpack('<BBIIII', f.read(18))
        self.length_enabled, self.length = struct.unpack('<BI', f.read(5))
        for i in range(len(self.wave)):
            self.wave[i] = ord(f.read(1))

    def _stop(self):
        self.channel.stop()

    def _play(self):
        wave = [x * self.volume for x in self.wave]
        self.channel.play(wave, self.frequency)

    def reset(self):
        self.__init__(self.channel)

    def trigger(self):
        # Reset main counter
        self.counter, self.steps = 0, 0
        self.enabled = True

        self.sweep_counter = 0  # Timer reset
        self.sweep_enabled = not (self.sweep_period == 0 or self.sweep_shift == 0)

        # Frequency copied to shadow register
        self.freq_x = ((self.NR14 & 0x07) << 8) + self.NR13
        self.frequency = 131072 / (2048 - self.freq_x)
        # Should update frequency be called ??

        self.volume = self.volume_initial
        self.volume_counter = 0  # Timer reset
        self.volume_enabled = not (self.volume_period == 0)

        self._play()

    def nr10(self, byte):
        self.NR10 = byte
        # Extract values (Read only values.)
        self.sweep_period = (byte & 0x70) >> 4
        self.sweep_dec = bool(byte & (1 << 3))
        self.sweep_shift = byte & 0x07
        # Calculated when value updated!
        # sweep operation enabled if both sweep period and sweep shift is non zero
        # frequency remains unchanged when sweep shifts or sweep period is zero
        self.sweep_enabled = not (self.sweep_period == 0 or self.sweep_shift == 0)

    def update_frequency(self):
        if self.sweep_enabled:
            if self.sweep_dec:
                freq_x = self.freq_x - (self.freq_x >> self.sweep_shift)
                # if 0 retain previous value
                self.freq_x = freq_x if freq_x > 0 else self.freq_x
            else:
                freq_x = self.freq_x + (self.freq_x >> self.sweep_shift)
                if freq_x > 0x7FF:  # overflow
                    self.freq_x = 0  # Reset it
                    # Disable the sound itself
                    self.enabled = False
                    # TODO: handle disable
                    self._stop()
                    return  # Don't proceed !!
                else:
                    self.freq_x = freq_x
            # Update the registers from shadow
            self.NR13 = self.freq_x & 0xFF
            self.NR14 &= 0xF8
            self.NR14 |= (self.freq_x >> 8) & 0x07
        # The frequency to output if enabled (NOTE)
        self.frequency = 131072 / (2048 - self.freq_x)
        # TODO: Update the channel
        self._play()

    def nr12(self, byte):
        self.NR12 = byte
        # Extract values (Read only values.)
        self.volume_initial = byte >> 4
        self.volume_amplify = bool(byte & (1 << 3))
        self.volume_period = byte & 0x07
        # volume shifting is enabled if period is non zero
        self.volume_enabled = not (self.volume_period == 0)

    def update_volume(self):
        if self.volume_enabled:
            if self.volume_amplify:
                volume = self.volume + 1
                self.volume = min(volume, 15)
            else:
                volume = self.volume - 1
                self.volume = max(volume, 0)
            # TODO: Update the channel
            self._play()

    def nr11(self, byte):
        self.NR11 = byte
        self.wave = get_waveform(byte >> 6)
        self.length = 64 - (byte & 0x1F)  # Note: length not readable

    def update_length(self):
        if self.length_enabled:
            self.length -= 1
            if self.length <= 0:
                self.enabled = False
                # TODO: handle disable
                self._stop()

    def nr13(self, byte):
        # doesn't do any thing apart from writing register
        self.NR13 = byte

    def nr14(self, byte):
        self.NR14 = byte
        self.length_enabled = bool(byte & (1 << 6))
        # Frequency is taken up when needed.
        if byte & (1 << 7):
            # Trigger if set
            self.trigger()

    def handle_freq_sweep(self):
        if self.sweep_enabled:
            self.sweep_counter += 1
            if self.sweep_counter >= self.sweep_period:
                self.sweep_counter -= self.sweep_period  # reset counter
                self.update_frequency()

    def handle_length_ctr(self):
        if self.length_enabled:
            self.update_length()

    def handle_vol_env(self):
        if self.volume_enabled:
            self.volume_counter += 1
            if self.volume_counter >= self.volume_period:
                self.volume_counter -= self.volume_period
                self.update_volume()

    def tick(self, ticks):
        if self.enabled:
            self.counter += ticks
            if self.counter > 8192:  # 512 Hz counter
                self.steps += 1
                self.steps %= 8
                self.counter %= 8192
                if self.steps == 0 or self.steps == 4:  # Update length
                    self.handle_length_ctr()
                elif self.steps == 2 or self.steps == 6:  # Update length  and sweep
                    self.handle_length_ctr()
                    self.handle_freq_sweep()
                elif self.steps == 7:  # Update volume
                    self.handle_vol_env()
        # else:
        #     self._stop()


class Sound3:
    def __init__(self, channel):
        self.NR30 = 0
        self.NR31 = 0
        self.NR32 = 0
        self.NR33 = 0
        self.NR34 = 0

        self.channel = channel
        self._stop()  # Stop while initialize

        # Whether the sound is running or not. Used for NR52 as well
        # Used by NR30 as well
        self.enabled = False

        # frame sequencer (self.steps << 13 + self.counter)
        self.counter = 0
        self.steps = 0  # Used with the counter

        # Length
        self.length_enabled = False
        self.length = 256

        self.volume = 0  # Controlled by NR32
        self.frequency = 65536

        self.wave = [0] * 32

    def save(self, f):
        f.write(struct.pack('<BBBBB', self.NR30, self.NR31, self.NR32, self.NR33, self.NR34))
        f.write(struct.pack('<BII', self.enabled, self.counter, self.steps))
        f.write(struct.pack('<BI', self.length_enabled, self.length))
        f.write(struct.pack('<ff', self.frequency, self.volume))
        for i in range(len(self.wave)):
            f.write(self.wave[i].to_bytes(1, 'little'))

    def load(self, f):
        self.NR30, self.NR31, self.NR32, self.NR33, self.NR34 = struct.unpack('<BBBBB', f.read(5))
        self.enabled, self.counter, self.steps = struct.unpack('<BII', f.read(9))
        self.length_enabled, self.length = struct.unpack('<BI', f.read(5))
        self.frequency, self.volume = struct.unpack('<ff', f.read(8))
        for i in range(len(self.wave)):
            self.wave[i] = ord(f.read(1))

    def _stop(self):
        self.channel.stop()

    def _play(self):
        # wave = []
        # for x in self.wave:
        #     wave.extend([int(x * self.volume), -int(x * self.volume)])
        wave = [int(x * self.volume) for x in self.wave]
        self.channel.play(wave, self.frequency)

    def reset(self):
        self.__init__(self.channel)

    def nr30(self, byte):
        self.NR30 = byte
        self.enabled = bool(byte & (1 << 7))
        # Affects only existing play back
        if not self.enabled:
            self._stop()

    def nr31(self, byte):
        self.NR31 = byte
        self.length = 256 - byte

    def nr32(self, byte):
        self.NR32 = byte
        volume = (byte & 0x60) >> 5
        self.volume = 0.50 if volume == 2 else 0.25 if volume == 3 else volume

    def nr33(self, byte):
        self.NR33 = byte

    def nr34(self, byte):
        self.NR34 = byte
        self.length_enabled = bool(byte & (1 << 6))
        # Frequency is taken up when needed.
        if byte & (1 << 7):
            self.trigger()

    def wave_pattern_ram(self, offset, byte):
        # NOTE: First upper 4 bits are played !!!
        self.wave[offset * 2] = byte >> 4
        self.wave[offset * 2 + 1] = byte & 0x0F

    def trigger(self):
        # Reset main counter
        self.counter, self.steps = 0, 0
        self.enabled = True

        x = ((self.NR34 & 0x07) << 8) + self.NR33
        self.frequency = 65536 / (2048 - x)

        self._play()

    def update_length(self):
        if self.length_enabled:
            self.length -= 1
            if self.length <= 0:
                self.enabled = False
                # TODO: handle disable
                self._stop()

    def handle_length_ctr(self):
        if self.length_enabled:
            self.update_length()

    def tick(self, ticks):
        if self.enabled:
            self.counter += ticks
            if self.counter > 8192:  # 512 Hz counter
                self.steps += 1
                self.steps %= 8
                self.counter %= 8192
                if self.steps % 2 == 0:  # Update length
                    self.handle_length_ctr()


def lfsr(bits):
    register = (2 ** bits) - 1
    transitions = {}
    outputs = []
    while register not in transitions:
        b0, b1 = register & 0b1, (register & 0b10) >> 1
        transitions[register] = (register >> 1) + ((b0 ^ b1) << (bits - 1))
        register = transitions[register]
        outputs.append(1 ^ b0)
    del transitions
    return outputs


class Sound4:
    def __init__(self, channel):
        self.NR41 = 0
        self.NR42 = 0
        self.NR43 = 0
        self.NR44 = 0
        self.channel = channel
        self._stop()

        # Whether the sound is running or not. Used for NR52 as well
        self.enabled = False

        # frame sequencer (self.steps << 13 + self.counter)
        self.counter = 0
        self.steps = 0  # Used with the counter

        # Envelope
        # Extracted (Envelop)
        self.volume_initial = 0
        self.volume_amplify = False
        self.volume_period = 0
        # Internal (Envelop)
        self.volume_enabled = False
        self.volume = 0  # The computed volume (4-bit)
        self.volume_counter = 0

        # Frequency
        # Extracted (Polynomial Counter Register)
        self.clock_shift = 0
        self.lfsr_mode = False
        self.divisor_code = 0.5
        # both using same to lower the size impact on audio speed
        self.wave_bit15 = lfsr(7)  # Wave to use when lfsr mode = 0
        self.wave_bit7 = lfsr(7)  # Wave to use when lfsr mode = 1
        self.wave = self.wave_bit15
        # Computed
        self.frequency = 524288  # Computed from the Polynomial counter

        # Length
        self.length_enabled = False
        self.length = 64

    def save(self, f):
        f.write(struct.pack('<BBBB', self.NR41, self.NR42, self.NR43, self.NR44))
        f.write(struct.pack('<BII', self.enabled, self.counter, self.steps))
        f.write(struct.pack('<BIff', self.lfsr_mode, self.clock_shift, self.divisor_code, self.frequency))
        f.write(struct.pack('<BBIIII', self.volume_amplify, self.volume_enabled,
                            self.volume_initial, self.volume_period, self.volume_counter, self.volume))
        f.write(struct.pack('<BI', self.length_enabled, self.length))

    def load(self, f):
        self.NR41, self.NR42, self.NR43, self.NR44 = struct.unpack('<BBBB', f.read(4))
        self.enabled, self.counter, self.steps = struct.unpack('<BII', f.read(9))
        self.lfsr_mode, self.clock_shift, self.divisor_code, self.frequency = struct.unpack('<BIff', f.read(13))
        self.volume_amplify, self.volume_enabled, self.volume_initial, self.volume_period,\
            self.volume_counter, self.volume = struct.unpack('<BBIIII', f.read(18))
        self.length_enabled, self.length = struct.unpack('<BI', f.read(5))
        # Set the value based on the flag!
        self.wave = self.wave_bit7 if self.lfsr_mode else self.wave_bit15

    def _stop(self):
        self.channel.stop()

    def _play(self):
        # TODO: Decide on the length to play based on when next it would likely be called
        # TODO: Use the volume period and frequency to determine the portion of noise played and
        #  also have the a noise counter
        # TODO: Also normalize to prevent noise
        wave = [x * self.volume for x in self.wave]
        self.channel.play(wave, self.frequency / len(wave))

    def reset(self):
        self.__init__(self.channel)

    def nr41(self, byte):
        # print(f'Write to NR41: {byte:08b}')
        self.NR41 = byte
        self.length = 64 - (byte & 0x1F)  # Note: length not readable

    def nr42(self, byte):
        # print(f'Write to NR42: {byte:08b}')
        self.NR42 = byte
        # Extract values (Read only values.)
        self.volume_initial = byte >> 4
        self.volume_amplify = bool(byte & (1 << 3))
        self.volume_period = byte & 0x07
        # volume shifting is enabled if period is non zero
        self.volume_enabled = not (self.volume_period == 0)

    def nr43(self, byte):
        # print(f'Write to NR43: {byte:08b}')
        self.NR43 = byte
        self.clock_shift = byte >> 4
        self.lfsr_mode = bool(byte & (1 << 3))
        self.wave = self.wave_bit7 if self.lfsr_mode else self.wave_bit15
        divisor_code = byte & 0x07
        self.divisor_code = divisor_code if divisor_code > 0 else 0.5
        self.frequency = int(524288 / self.divisor_code) >> (1 + self.clock_shift)

    def nr44(self, byte):
        # print(f'Write to NR44: {byte:08b}')
        self.NR44 = byte
        self.length_enabled = bool(byte & (1 << 6))
        if byte & (1 << 7):
            # Trigger if set
            # print('Sound 4 trigger')
            self.trigger()

    def update_volume(self):
        if self.volume_enabled:
            if self.volume_amplify:
                volume = self.volume + 1
                self.volume = min(volume, 15)
            else:
                volume = self.volume - 1
                self.volume = max(volume, 0)
            # TODO: Update the channel
            self._play()

    def update_length(self):
        if self.length_enabled:
            self.length -= 1
            if self.length <= 0:
                self.enabled = False
                # TODO: handle disable
                self._stop()

    def handle_length_ctr(self):
        if self.length_enabled:
            self.update_length()

    def handle_vol_env(self):
        if self.volume_enabled:
            self.volume_counter += 1
            if self.volume_counter >= self.volume_period:
                self.volume_counter -= self.volume_period
                self.update_volume()

    def trigger(self):
        # Reset main counter
        self.counter, self.steps = 0, 0
        self.enabled = True
        # Frequency is set writing to register
        # Update volume
        self.volume = self.volume_initial
        self.volume_counter = 0  # Timer reset
        self.volume_enabled = not (self.volume_period == 0)

        self._play()

    def tick(self, ticks):
        if self.enabled:
            self.counter += ticks
            if self.counter > 8192:  # 512 Hz counter
                self.steps += 1
                self.steps %= 8
                self.counter %= 8192
                if self.steps % 2 == 0:  # Update length
                    self.handle_length_ctr()
                elif self.steps == 7:  # Update volume
                    self.handle_vol_env()


class Mixer:
    def __init__(self):
        # pygame.mixer.init()
        self.channel1 = channel.Channel(0)
        self.channel2 = channel.Channel(1)
        self.channel3 = channel.Channel(2)
        self.channel4 = channel.Channel(3)

        self.channel1.set_enable(True)
        self.channel2.set_enable(True)
        self.channel3.set_enable(True)
        self.channel4.set_enable(True)

        self.sound1 = Sound1(self.channel1)
        self.sound2 = Sound1(self.channel2)
        self.sound3 = Sound3(self.channel3)
        self.sound4 = Sound4(self.channel4)
        self.NR50 = 0
        self.NR51 = 0
        self.NR52 = 0
        self.enabled = False
        self._play_sound = True

    def toggle_mute(self):
        if self._play_sound:
            self.channel1.set_enable(False)
            self.channel2.set_enable(False)
            self.channel3.set_enable(False)
            self.channel4.set_enable(False)
            self._play_sound = False
        else:
            self.channel1.set_enable(True)
            self.channel2.set_enable(True)
            self.channel3.set_enable(True)
            self.channel4.set_enable(True)
            self._play_sound = True

    def save(self, f):
        f.write(struct.pack('<BBBB', self.NR50, self.NR51, self.NR52, self.enabled))
        self.sound1.save(f)
        self.sound2.save(f)
        self.sound3.save(f)
        self.sound4.save(f)

    def load(self, f):
        self.NR50, self.NR51, self.NR52, self.enabled = struct.unpack('<BBBB', f.read(4))
        self.sound1.load(f)
        self.sound2.load(f)
        self.sound3.load(f)
        self.sound4.load(f)

    def read_byte(self, address):
        if address == 0xFF24:
            return self.NR50
        elif address == 0xFF25:
            return self.NR51
        elif address == 0xFF26:
            # TODO: Read enabled from sounds
            return (self.NR52 & 0xF0) + (self.sound1.enabled << 0) + (self.sound2.enabled << 1) + \
                   (self.sound3.enabled << 2) + (self.sound4.enabled << 3)

        if self.enabled:
            # Sound 1
            if address == 0xFF10:
                return self.sound1.NR10 | 0x80
            elif address == 0xFF11:
                return self.sound1.NR11 | 0x3F
            elif address == 0xFF12:
                return self.sound1.NR12 | 0x00
            elif address == 0xFF13:
                return self.sound1.NR13 | 0xFF
            elif address == 0xFF14:
                return self.sound1.NR14 | 0xBF
            # Sound 2
            elif address == 0xFF16:
                return self.sound2.NR11 | 0x3F
            elif address == 0xFF17:
                return self.sound2.NR12 | 0x00
            elif address == 0xFF18:
                return self.sound2.NR13 | 0xFF
            elif address == 0xFF19:
                return self.sound2.NR14 | 0xBF

            # Sound 3
            elif address == 0xFF1A:
                return self.sound3.NR30 | 0x7F
            elif address == 0xFF1B:
                return self.sound3.NR31 | 0xFF
            elif address == 0xFF1C:
                return self.sound3.NR32 | 0x00
            elif address == 0xFF1D:
                return self.sound3.NR33 | 0x00
            elif address == 0xFF1E:
                return self.sound3.NR34 | 0xBF

            # Sound 4
            elif address == 0xFF20:
                return self.sound4.NR41 | 0xFF
            elif address == 0xFF21:
                return self.sound4.NR42 | 0x00
            elif address == 0xFF22:
                return self.sound4.NR43 | 0x00
            elif address == 0xFF23:
                return self.sound4.NR44 | 0xBF

            # Wave RAM
            elif 0xFF30 <= address <= 0xFF3F:
                offset = address & 0xF
                return (self.sound3.wave[offset * 2] << 4) + self.sound3.wave[offset * 2 + 1]
        return 0xFF

    def nr50(self, byte):
        self.NR50 = byte
        # TODO: Set channel volume
        v1, v2 = byte & 0x03, (byte & 0x30) >> 4
        self.channel1.set_master_volume(v1 / 7, v2 / 7)
        self.channel2.set_master_volume(v1 / 7, v2 / 7)
        self.channel3.set_master_volume(v1 / 7, v2 / 7)
        self.channel4.set_master_volume(v1 / 7, v2 / 7)

    def nr51(self, byte):
        self.NR51 = byte
        # TODO: Set stereo for channels
        self.channel1.set_output(bool(byte & (1 << 0)), bool(byte & (1 << 4)))
        self.channel2.set_output(bool(byte & (1 << 1)), bool(byte & (1 << 5)))
        self.channel3.set_output(bool(byte & (1 << 2)), bool(byte & (1 << 6)))
        self.channel4.set_output(bool(byte & (1 << 3)), bool(byte & (1 << 7)))

    def nr52(self, byte):
        self.NR52 = byte & 0xF0
        self.enabled = bool(byte >> 7)
        # print(f"Write to enabled: {self.enabled}")
        # TODO: enable or disable all sound circuits
        if not self.enabled:
            # Stop all channels
            self.sound1.reset()
            self.sound2.reset()
            self.sound3.reset()
            self.sound4.reset()

    def write_byte(self, address, byte):
        # print(f"MIXER: WRITE BYTE Enabled:{self.enabled:d} {address:04X}: {byte:08b} {sound_addr(address)}")
        if address == 0xFF24:
            self.nr50(byte)
        elif address == 0xFF25:
            self.nr51(byte)
        elif address == 0xFF26:
            self.nr52(byte)

        if self.enabled:
            # print(f"Write Enabled {address:04X}: {byte:02X} ")
            # Write only if enabled
            if address == 0xFF10:
                self.sound1.nr10(byte)
            elif address == 0xFF11:
                self.sound1.nr11(byte)
            elif address == 0xFF12:
                self.sound1.nr12(byte)
            elif address == 0xFF13:
                self.sound1.nr13(byte)
            elif address == 0xFF14:
                self.sound1.nr14(byte)

            elif address == 0xFF16:
                self.sound2.nr11(byte)
            elif address == 0xFF17:
                self.sound2.nr12(byte)
            elif address == 0xFF18:
                self.sound2.nr13(byte)
            elif address == 0xFF19:
                self.sound2.nr14(byte)

            elif address == 0xFF1A:
                self.sound3.nr30(byte)
            elif address == 0xFF1B:
                self.sound3.nr31(byte)
            elif address == 0xFF1C:
                self.sound3.nr32(byte)
            elif address == 0xFF1D:
                self.sound3.nr33(byte)
            elif address == 0xFF1E:
                self.sound3.nr34(byte)

            elif address == 0xFF20:
                self.sound4.nr41(byte)
            elif address == 0xFF21:
                self.sound4.nr42(byte)
            elif address == 0xFF22:
                self.sound4.nr43(byte)
            elif address == 0xFF23:
                self.sound4.nr44(byte)

            elif 0xFF30 <= address <= 0xFF3F:
                self.sound3.wave_pattern_ram(address & 0xF, byte)

    def tick(self, ticks):
        if self.enabled:
            self.sound1.tick(ticks)
            self.sound2.tick(ticks)
            self.sound3.tick(ticks)
            self.sound4.tick(ticks)
