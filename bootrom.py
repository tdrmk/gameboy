try:
    from cython import compiled
except ImportError:
    compiled = False


# for cython compatibility, use array module instead of `bytearray` as former works in both modes,
# while bytearray only in python. Nope ??
# from array import array
if compiled:
    print('Cython mode!!')


class BootROM:
    def __init__(self, filename=None):
        if filename is not None:
            with open(filename, 'rb') as f:
                self.contents = f.read()
                # self.contents = array('B', f.read())
        else:
            self.contents = bytearray(256)
            # self.contents = array('B', [0] * 256)

            # Source [https://github.com/Baekalfen/PyBoy],
            # for faster booting while testing in python mode.
            # Set stack pointer
            self.contents[0x00] = 0x31
            self.contents[0x01] = 0xFE
            self.contents[0x02] = 0xFF
            # Inject jump to 0xFC
            self.contents[0x03] = 0xC3
            self.contents[0x04] = 0xFC
            self.contents[0x05] = 0x00
            # Inject code to disable boot-ROM
            self.contents[0xFC] = 0x3E
            self.contents[0xFD] = 0x01
            self.contents[0xFE] = 0xE0
            self.contents[0xFF] = 0x50

    def read_byte(self, address):
        return self.contents[address]

