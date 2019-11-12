V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD = range(0, 5)

dividers = [1024, 16, 64, 256]

class Timer:
    # https://github.com/Baekalfen/PyBoy
    def __init__(self):
        # Registers
        self.div = 0
        self.tima = 0
        self.tma = 0
        self.tac = 0

        self.div_counter = 0
        self.tima_counter = 0

        # Needs CPU to raise interrupts
        self.cpu = None

    def attach_cpu(self, cpu):
        self.cpu = cpu

    def tick(self, cycles):
        # Returns whether to raise interrupt or not.

        # DIV incremented every 256 cycles
        self.div_counter += cycles
        self.div += self.div_counter >> 8
        self.div_counter &= 0xFF
        self.div &= 0xFF

        if self.tac & 0b100 != 0:
            # TIMA incremented based on Input Clock Select (lower 2 bits of TAC)
            # when timer is enabled
            self.tima_counter += cycles
            divider = dividers[self.tac & 0b011]
            if self.tima_counter > divider:
                self.tima_counter -= divider
                if self.tima >= 0xFF:
                    # In case of overflow reset to value im TMA
                    self.tima = self.tma
                    # Request Interrupt
                    self.cpu.request_interrupt(TIMER)
                else:
                    self.tima += 1

