
import sdl2.ext
import ctypes

import joypad

"""

Two modes of display exists
    1.  This is a full screen display that maintains aspect ratio.
    2.  This is a resizable display where contents is stretched to fit the the window.
"""

key_map = {
    sdl2.SDLK_RIGHT: joypad.RIGHT,
    sdl2.SDLK_LEFT: joypad.LEFT,
    sdl2.SDLK_UP: joypad.UP,
    sdl2.SDLK_DOWN: joypad.DOWN,
    sdl2.SDLK_a: joypad.A,
    sdl2.SDLK_b: joypad.B,
    sdl2.SDLK_SPACE: joypad.SELECT,
    sdl2.SDLK_RETURN: joypad.START,
}


class Display:
    def __init__(self, _joypad, stretch=True, scale=1):
        self.joypad = _joypad
        self.blank = False
        self.stretch = stretch
        flags = sdl2.SDL_WINDOW_RESIZABLE| sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
        initial_width, initial_height = 160 * scale, 144 * scale
        self.window = sdl2.SDL_CreateWindow(b"Game Boy", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED,
                                            initial_width, initial_height, flags)
        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, sdl2.SDL_RENDERER_ACCELERATED)
        self.texture = sdl2.SDL_CreateTexture(self.renderer, sdl2.SDL_PIXELFORMAT_ARGB8888,
                                              sdl2.SDL_TEXTUREACCESS_STATIC, 160, 144)
        sdl2.SDL_ShowWindow(self.window)

    def _render(self, frame_bytes):
        sdl2.SDL_UpdateTexture(self.texture, None, frame_bytes, 160 * 4)
        if not self.stretch:
            w, h = ctypes.c_int(), ctypes.c_int()
            sdl2.SDL_GetWindowSize(self.window, w, h)
            w, h = w.value, h.value
            s = min(w // 160, h // 144)
            dst_rect = sdl2.SDL_Rect((w - s * 160) // 2, (h - s * 144) // 2, s * 160, s * 144)
        else:
            dst_rect = None

        sdl2.SDL_RenderCopy(self.renderer, self.texture, None, dst_rect)
        sdl2.SDL_RenderPresent(self.renderer)
        # sdl2.SDL_SetRenderDrawColor(self.renderer, 255, 255, 255, 255)
        # Clears background when scaled/re-sized
        sdl2.SDL_RenderClear(self.renderer)

    def _render_blank(self):
        # Fill with white (background)
        # sdl2.SDL_SetRenderDrawColor(self.renderer, 255, 255, 255, 255)
        sdl2.SDL_RenderClear(self.renderer)

    def _handle_events(self):
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                exit()
            if event.type == sdl2.SDL_KEYDOWN and event.key.keysym.sym in key_map:
                self.joypad.handle_key(key_map[event.key.keysym.sym], True)
            elif event.type == sdl2.SDL_KEYUP and event.key.keysym.sym in key_map:
                self.joypad.handle_key(key_map[event.key.keysym.sym], False)

    def render(self, frame):
        self._handle_events()
        # https://docs.python.org/3/library/array.html
        # array.buffer_info() ->  (address, length)
        self._render(ctypes.c_void_p(frame.buffer_info()[0]))
        self.blank = False

    def render_blank(self):
        self._handle_events()
        if not self.blank:
            self._render_blank()
            self.blank = True
