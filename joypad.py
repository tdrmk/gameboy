import struct

V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD = range(0, 5)

RIGHT, LEFT, UP, DOWN, A, B, SELECT, START = range(8)


def reset_bit(x, bit):
    return x & ~(1 << bit)


def set_bit(x, bit):
    return x | (1 << bit)


class Joypad:
    # TODO: Raise Interrupt
    def __init__(self):
        # 0 - Selected or pressed
        self.right = 1
        self.left = 1
        self.up = 1
        self.down = 1
        self.A = 1
        self.B = 1
        self.select = 1
        self.start = 1

        self.buttons = 1
        self.directions = 1

        # Needs CPU to raise interrupts
        self.cpu = None

    def save(self, f):
        f.write(struct.pack('<BBBBB BBBBB', self.right, self.left, self.up, self.down, self.A, self.B, self.select,
                            self.start, self.buttons, self.directions))

    def load(self, f):
        self.right, self.left, self.up, self.down, self.A, self.B, self.select, \
            self.start, self.buttons, self.directions = struct.unpack('<BBBBB BBBBB', f.read(10))

    def attach_cpu(self, cpu):
        self.cpu = cpu

    def handle_key(self, key, pressed):
        v = 0 if pressed else 1
        if key == RIGHT:
            self.right = v
        elif key == LEFT:
            self.left = v
        elif key == UP:
            self.up = v
        elif key == DOWN:
            self.down = v
        elif key == A:
            self.A = v
        elif key == B:
            self.B = v
        elif key == SELECT:
            self.select = v
        elif key == START:
            self.start = v
        # ELSE Throw an error
        if pressed:
            self.cpu.request_interrupt(JOYPAD)

    def write_byte(self, byte):
        self.directions = byte & 0b0001_0000 > 0
        self.buttons = byte & 0b0010_0000 > 0

    def read_byte(self):
        byte = 0x0F
        if not self.directions:
            byte = self.right | (self.left << 1) | (self.up << 2) | (self.down << 3)
        elif not self.buttons:
            byte = self.A | (self.B << 1) | (self.select << 2) | (self.start << 3)
        return byte
