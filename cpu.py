# from instructions import fetch_opcode, execute_opcode
import instructions
import struct

IE_ADDRESS = 0xFFFF  # Interrupt Enable (enabled)
IF_ADDRESS = 0xFF0F  # Interrupt Flag (requests)

V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD = range(0, 5)


class CPU:
    def __init__(self, memory):
        self.PC = 0  # Program Counter
        self.SP = 0  # Stack Pointer
        self.A = 0  # Accumulator
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.HL = 0  # Since most instructions use HL together

        self.FLAG_Z = 0  # Zero flag
        self.FLAG_N = 0  # Subtract flag
        self.FLAG_H = 0  # Half carry flag
        self.FLAG_C = 0  # Carry flag

        self.ime = True  # Interrupt Master Enable Flag
        self.memory = memory

    def save(self, f):
        f.write(struct.pack('<HHBBBBBBHBBBB',
                            self.PC, self.SP, self.A, self.B, self.C, self.D, self.E, self.ime,
                            self.HL, self.FLAG_Z, self.FLAG_N, self.FLAG_H, self.FLAG_C))

    def load(self, f):
        self.PC, self.SP, self.A, self.B, self.C, self.D, self.E, self.ime, \
            self.HL, self.FLAG_Z, self.FLAG_N, self.FLAG_H, self.FLAG_C = struct.unpack('<HHBBBBBBHBBBB', f.read(16))

    def request_interrupt(self, interrupt):
        self.memory.write_byte(IF_ADDRESS, self.memory.read_byte(IF_ADDRESS) | (1 << interrupt))

    def check_interrupts(self):
        # https://gbdev.gg8.se/wiki/articles/Interrupts
        if not self.ime:
            return False

        ie = self.memory.read_byte(IE_ADDRESS)
        ir = self.memory.read_byte(IF_ADDRESS)

        enabled_interrupts = ie & ir & 0b00011111
        if enabled_interrupts == 0:  # No interrupts to execute
            return False

        # execute interrupt
        self.ime = False
        # Push PC to top of stack
        # LEARNING: Don't use push or call instruction (few instructions get skipped)
        self.SP -= 2
        self.memory.write_byte(self.SP + 1, self.PC >> 8)
        self.memory.write_byte(self.SP, self.PC & 0xFF)

        # Reset interrupt request and jump to corresponding ISR
        if enabled_interrupts & (1 << V_BLANK):
            # print('V Blank ISR')
            self.memory.write_byte(IF_ADDRESS, ir ^ (1 << V_BLANK))
            self.PC = 0x0040
        elif enabled_interrupts & (1 << LCD_STAT):
            # print('LCD Stat ISR')
            self.memory.write_byte(IF_ADDRESS, ir ^ (1 << LCD_STAT))
            self.PC = 0x0048
        elif enabled_interrupts & (1 << TIMER):
            # print('TIMER ISR')
            self.memory.write_byte(IF_ADDRESS, ir ^ (1 << TIMER))
            self.PC = 0x0050
        elif enabled_interrupts & (1 << SERIAL):
            # print('SERIAL ISR')
            self.memory.write_byte(IF_ADDRESS, ir ^ (1 << SERIAL))
            self.PC = 0x0058
        elif enabled_interrupts & (1 << JOYPAD):
            # print('JOYPAD ISR')
            self.memory.write_byte(IF_ADDRESS, ir ^ (1 << JOYPAD))
            self.PC = 0x0060
        return True

    def tick(self):
        self.check_interrupts()  # If any interrupt points PC to ISR
        opcode = instructions.fetch_opcode(self)
        return instructions.execute_opcode(self, opcode)
