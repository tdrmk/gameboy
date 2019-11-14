from libc.stdint cimport uint8_t, uint16_t
cimport sdl2
import sdl2
from gameboy cimport Gameboy
cimport joypad
from joypad cimport Joypad
from cpython.array cimport array


cdef uint8_t RIGHT, LEFT, UP, DOWN, A, B, SELECT, START
RIGHT, LEFT, UP, DOWN, A, B, SELECT, START = range(8)


cdef class Display:
    def __init__(self, Gameboy gameboy, Joypad _joypad, bint stretch=True, int scale=1):
        self.gameboy = gameboy
        self.joypad = _joypad
        self.blank = False
        self.stretch = stretch
        self.window = sdl2.SDL_CreateWindow(b"Game Boy", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED,
                                            160 * scale, 144 * scale, sdl2.SDL_WINDOW_RESIZABLE| sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)

        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, sdl2.SDL_RENDERER_ACCELERATED)
        self.texture = sdl2.SDL_CreateTexture(self.renderer, sdl2.SDL_PIXELFORMAT_ARGB8888,
                                              sdl2.SDL_TEXTUREACCESS_STATIC, 160, 144)
        sdl2.SDL_ShowWindow(self.window)

    cdef void _render_blank(self):
        # sdl2.SDL_SetRenderDrawColor(self.renderer, 255, 255, 255, 255)
        sdl2.SDL_RenderClear(self.renderer)


    cdef void _handle_events(self):
        cdef sdl2.SDL_Event event
        cdef uint8_t pressed
        while sdl2.SDL_PollEvent(&event) != 0:
            if event.type == sdl2.SDL_QUIT or (event.type == sdl2.SDL_KEYDOWN and event.key.keysym.sym == sdl2.SDLK_q):
                # self.gameboy.save()
                exit()
            elif event.type == sdl2.SDL_KEYDOWN or event.type == sdl2.SDL_KEYUP:
                pressed = 0 if event.type == sdl2.SDL_KEYUP else 1
                if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    self.joypad.handle_key(RIGHT, pressed)
                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    self.joypad.handle_key(LEFT, pressed)
                elif event.key.keysym.sym == sdl2.SDLK_UP:
                    self.joypad.handle_key(UP, pressed)
                elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                    self.joypad.handle_key(DOWN, pressed)
                elif event.key.keysym.sym == sdl2.SDLK_a:
                    self.joypad.handle_key(A, pressed)
                elif event.key.keysym.sym == sdl2.SDLK_b:
                    self.joypad.handle_key(B, pressed)
                elif event.key.keysym.sym == sdl2.SDLK_SPACE:
                    self.joypad.handle_key(SELECT, pressed)
                elif event.key.keysym.sym == sdl2.SDLK_RETURN:
                    self.joypad.handle_key(START, pressed)
                elif event.key.keysym.sym == sdl2.SDLK_s and event.type == sdl2.SDL_KEYDOWN:
                    self.gameboy.save()

    cdef void _render(self, const void * frame):
        cdef int w, h
        cdef sdl2.SDL_Rect dst_rect
        cdef int s
        sdl2.SDL_UpdateTexture(self.texture, NULL, frame, 160 * 4)
        if not self.stretch:
            sdl2.SDL_GetWindowSize(self.window, &w, &h)
            s = min(w // 160, h // 144)
            dst_rect.x = (w - s * 160) // 2
            dst_rect.y = (h - s * 144) // 2
            dst_rect.w = s * 160
            dst_rect.h = s * 144
            sdl2.SDL_RenderCopy(self.renderer, self.texture, NULL, &dst_rect)
        else:
            sdl2.SDL_RenderCopy(self.renderer, self.texture, NULL, NULL)

        sdl2.SDL_RenderPresent(self.renderer)
        sdl2.SDL_RenderClear(self.renderer)

    cdef void render_blank(self):
        self._handle_events()
        if not self.blank:
            self._render_blank()
            self.blank = True

    cdef void render(self,  array frame):
        self._handle_events()
        # http://docs.cython.org/en/latest/src/tutorial/array.html
        self._render(frame.data.as_voidptr)
        self.blank = False



