try:
    from cython import compiled
except ImportError:
    compiled = False

import struct
from array import array

V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD = range(0, 5)
color_palette = (0xFFFFFFFF, 0xFFAAAAAA, 0xFF555555, 0xFF000000)

PALETTE = 4
VIDEO_RAM = 8192
SPRITE_ATTRIB = 160
TILES_UNPACKED = 384 * 8 * 8


class GPU:
    def __init__(self):
        self.video_ram = bytearray(VIDEO_RAM)
        self.sprite_attrib = bytearray(SPRITE_ATTRIB)

        # 8000-97FF, each tile is 16B unpacked to 64B
        self.tiles_unpacked = bytearray(TILES_UNPACKED)

        # while line is getting scanned, store values for scy, scx, wy and wx
        self.line_params = bytearray(144 * 7)
        # Registers
        self.lcdc = 0
        self.stat = 0
        self.scy = 0
        self.scx = 0
        self.ly = 0
        self.lyc = 0
        self.bgp = 0
        self.obp0 = 0
        self.obp1 = 0
        self.wy = 0
        self.wx = 0
        self.bgp_palette = bytearray(4)
        self.obp0_palette = bytearray(4)
        self.obp1_palette = bytearray(4)

        # Flags
        self.display_enable = False
        self.display_window = False
        self.display_background = False
        self.display_sprite = False
        self.large_tiles = False
        # addresses in video ram
        self.window_tile_map = 0x1800
        self.bkgrnd_tile_map = 0x1800
        self.tile_data_addr = 0x0800
        self.signed_addr = True

        # Need cpu to raise interrupt
        self.cpu = None

        # Frame used for rendering allocate once
        self.frame_bytes = array('B', [0] * (160 * 144 * 4))
        if compiled:
            self.frame_buffer = memoryview(self.frame_bytes).cast('I', shape=(144, 160))
        else:
            v = memoryview(self.frame_bytes).cast('I')
            self.frame_buffer = [v[i:i + 160] for i in range(0, 160 * 144, 160)]

    def save(self, f):
        f.write(struct.pack('<BBBBB BBBBB B', self.lcdc, self.stat, self.scy, self.scx, self.ly, self.lyc, self.bgp,
                            self.obp0, self.obp1, self.wy, self.wx))
        f.write(struct.pack('<BBBBB HHHB', self.display_enable, self.display_window, self.display_background,
                            self.display_sprite, self.large_tiles, self.window_tile_map, self.bkgrnd_tile_map,
                            self.tile_data_addr, self.signed_addr))
        for i in range(PALETTE):
            f.write(self.bgp_palette[i].to_bytes(1, 'little'))
        for i in range(PALETTE):
            f.write(self.obp0_palette[i].to_bytes(1, 'little'))
        for i in range(PALETTE):
            f.write(self.obp1_palette[i].to_bytes(1, 'little'))
        for i in range(VIDEO_RAM):
            f.write(self.video_ram[i].to_bytes(1, 'little'))
        for i in range(SPRITE_ATTRIB):
            f.write(self.sprite_attrib[i].to_bytes(1, 'little'))
        for i in range(TILES_UNPACKED):
            f.write(self.tiles_unpacked[i].to_bytes(1, 'little'))

    def load(self, f):
        self.lcdc, self.stat, self.scy, self.scx, self.ly, self.lyc, self.bgp, \
            self.obp0, self.obp1, self.wy, self.wx = struct.unpack('<BBBBB BBBBB B', f.read(11))
        self.display_enable, self.display_window, self.display_background, \
            self.display_sprite, self.large_tiles, self.window_tile_map, self.bkgrnd_tile_map, \
            self.tile_data_addr, self.signed_addr = struct.unpack('<BBBBB HHHB', f.read(12))
        for i in range(PALETTE):
            self.bgp_palette[i] = ord(f.read(1))
        for i in range(PALETTE):
            self.obp0_palette[i] = ord(f.read(1))
        for i in range(PALETTE):
            self.obp1_palette[i] = ord(f.read(1))
        for i in range(VIDEO_RAM):
            self.video_ram[i] = ord(f.read(1))
        for i in range(SPRITE_ATTRIB):
            self.sprite_attrib[i] = ord(f.read(1))
        for i in range(TILES_UNPACKED):
            self.tiles_unpacked[i] = ord(f.read(1))

    def attach_cpu(self, cpu):
        self.cpu = cpu

    def set_vram(self, address, byte):
        self.video_ram[address] = byte
        if 0 <= address <= 0x17FF:
            # write to tile area is un-pack from tile 16B --> 64B, ie, 2B row -> 8B row
            tr = address & ~(1 << 0)  # row address
            high_byte = self.video_ram[tr + 1]
            low_byte = self.video_ram[tr]
            self.tiles_unpacked[tr * 4 + 0] = ((high_byte & 0x80) >> 6) + ((low_byte & 0x80) >> 7)
            self.tiles_unpacked[tr * 4 + 1] = ((high_byte & 0x40) >> 5) + ((low_byte & 0x40) >> 6)
            self.tiles_unpacked[tr * 4 + 2] = ((high_byte & 0x20) >> 4) + ((low_byte & 0x20) >> 5)
            self.tiles_unpacked[tr * 4 + 3] = ((high_byte & 0x10) >> 3) + ((low_byte & 0x10) >> 4)
            self.tiles_unpacked[tr * 4 + 4] = ((high_byte & 0x08) >> 2) + ((low_byte & 0x08) >> 3)
            self.tiles_unpacked[tr * 4 + 5] = ((high_byte & 0x04) >> 1) + ((low_byte & 0x04) >> 2)
            self.tiles_unpacked[tr * 4 + 6] = ((high_byte & 0x02) >> 0) + ((low_byte & 0x02) >> 1)
            self.tiles_unpacked[tr * 4 + 7] = ((high_byte & 0x01) << 1) + ((low_byte & 0x01) >> 0)

    def set_lcdc(self, byte):
        self.lcdc = byte
        self.display_enable = byte & (1 << 7)
        self.display_window = byte & (1 << 5) and byte & (1 << 0)
        self.display_sprite = byte & (1 << 1)
        self.display_background = byte & (1 << 0)
        self.large_tiles = byte & (1 << 2)
        self.window_tile_map = 0x1C00 if byte & (1 << 6) else 0x1800
        self.bkgrnd_tile_map = 0x1C00 if byte & (1 << 3) else 0x1800
        self.tile_data_addr = 0x0000 if byte & (1 << 4) else 0x0800
        self.signed_addr = not (byte & (1 << 4))

    def set_bgp(self, byte):
        self.bgp = byte
        self.bgp_palette[0] = byte & 0b11
        self.bgp_palette[1] = (byte >> 2) & 0b11
        self.bgp_palette[2] = (byte >> 4) & 0b11
        self.bgp_palette[3] = (byte >> 6) & 0b11

    def set_obp0(self, byte):
        self.obp0 = byte
        self.obp0_palette[0] = byte & 0b11
        self.obp0_palette[1] = (byte >> 2) & 0b11
        self.obp0_palette[2] = (byte >> 4) & 0b11
        self.obp0_palette[3] = (byte >> 6) & 0b11

    def set_obp1(self, byte):
        self.obp1 = byte
        self.obp1_palette[0] = byte & 0b11
        self.obp1_palette[1] = (byte >> 2) & 0b11
        self.obp1_palette[2] = (byte >> 4) & 0b11
        self.obp1_palette[3] = (byte >> 6) & 0b11

    def scan_line(self, y):
        # Store the line parameters when line was scanned.
        self.line_params[y * 7 + 0] = self.scy
        self.line_params[y * 7 + 1] = self.scx
        self.line_params[y * 7 + 2] = self.wy
        self.line_params[y * 7 + 3] = self.wx
        self.line_params[y * 7 + 4] = self.display_sprite

    def render(self):
        for y in range(144):
            # Use those parameters when the line was scanned.
            scy, scx = self.line_params[y * 7 + 0], self.line_params[y * 7 + 1]
            wy = self.line_params[y * 7 + 2]
            wx = self.line_params[y * 7 + 3] - 7
            for x in range(160):
                if self.display_window and y >= wy and x >= wx:
                    wt = self.video_ram[self.window_tile_map + (((y - wy) // 8) % 32) * 32 + (((x - wx) // 8) % 32)]
                    if self.signed_addr:
                        wt = (wt ^ 0x80) + 128
                    self.frame_buffer[y][x] = color_palette[self.bgp_palette[
                        self.tiles_unpacked[wt * 64 + ((y - wy) % 8) * 8 + ((x - wx) % 8)]]]
                elif self.display_background:
                    bt = self.video_ram[self.bkgrnd_tile_map + (((y + scy) // 8) % 32) * 32 + (((x + scx) // 8) % 32)]
                    if self.signed_addr:
                        bt = (bt ^ 0x80) + 128
                    self.frame_buffer[y][x] = color_palette[self.bgp_palette[
                        self.tiles_unpacked[bt * 64 + ((y + scy) % 8) * 8 + ((x + scx) % 8)]]]
                else:
                    self.frame_buffer[y][x] = color_palette[0]
                # Else stays at the default value of 0!

        # TODO: Handle display sprites properly
        if self.display_sprite or True:  # Testing purpose set to always true
            # Sprite rendering does not match that of game-boy exactly
            # It renders all sprites along a line (doesn't limit to 10)
            # TODO: Implement large tiles!!
            for n in range(0, 0xA0, 4):
                oy, ox = self.sprite_attrib[n + 0] - 16, self.sprite_attrib[n + 1] - 8
                if -16 < oy < 144 and -8 < ox < 160:
                    pr = self.sprite_attrib[n + 3] & (1 << 7)  # Priority
                    yf = self.sprite_attrib[n + 3] & (1 << 6)  # y flip
                    xf = self.sprite_attrib[n + 3] & (1 << 5)  # x flip
                    if self.large_tiles:
                        st = self.sprite_attrib[n + 2] & 0xFE  # select the upper tile
                        sprite_height = 16
                    else:
                        st = self.sprite_attrib[n + 2]
                        sprite_height = 8

                    for dy in range(sprite_height):
                        y = oy + dy if not yf else oy + (sprite_height - dy - 1)  # y position on the frame

                        if y < 0 or y >= 144 or not self.line_params[y * 7 + 4]: continue
                        for dx in range(8):
                            x = ox + dx if not xf else ox + (7 - dx)  # x position on the frame
                            if x < 0 or x >= 160: continue
                            if self.sprite_attrib[n + 3] & (1 << 4):
                                color = self.obp1_palette[self.tiles_unpacked[st * 64 + dy * 8 + dx]]
                            else:
                                color = self.obp0_palette[self.tiles_unpacked[st * 64 + dy * 8 + dx]]
                            if (pr == 0 or self.frame_buffer[y][x] == color_palette[0]) and color != 0:
                                self.frame_buffer[y][x] = color_palette[color]

        return self.frame_bytes

    def set_stat_mode(self, mode):
        self.stat = (self.stat & 0xFC) | (mode & 0x03)
        if self.stat & 0x38 > 0 and mode != 3:
            if self.stat & (1 << (mode + 3)):
                self.cpu.request_interrupt(LCD_STAT)

    def check_coincidence(self):
        if self.ly == self.lyc:
            self.stat = self.stat | (1 << 2)
            if self.stat & (1 << 6):
                self.cpu.request_interrupt(LCD_STAT)
        else:
            self.stat = self.stat & ~(1 << 2)
