import pygame
import joypad

key_map = {
    pygame.K_RIGHT: joypad.RIGHT,
    pygame.K_LEFT: joypad.LEFT,
    pygame.K_UP: joypad.UP,
    pygame.K_DOWN: joypad.DOWN,
    pygame.K_a: joypad.A,
    pygame.K_b: joypad.B,
    pygame.K_SPACE: joypad.SELECT,
    pygame.K_RETURN: joypad.START,
}

WIDTH, HEIGHT = 160, 144


class Display:
    def __init__(self, gameboy, joypad0, stretch=False):
        self.gameboy = gameboy
        self.joypad = joypad0
        self.blank = False
        self.stretch = stretch

        pygame.display.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT),
                                           pygame.SCALED | pygame.DOUBLEBUF | pygame.HWSURFACE)
        self._render_blank()

    def _render(self, frame_buffer):
        pygame.surfarray.blit_array(self.window, frame_buffer)
        pygame.display.update()

    def _render_blank(self):
        self.window.fill((255, 255, 255))
        pygame.display.update()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                print('Exiting the game boy emulator ..')
                exit()
            elif event.type == pygame.KEYDOWN and event.key in key_map:
                self.joypad.handle_key(key_map[event.key], True)
            elif event.type == pygame.KEYUP and event.key in key_map:
                self.joypad.handle_key(key_map[event.key], False)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                # Saving the game to a file.
                self.gameboy.save()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.gameboy.mixer.toggle_mute()

    def render(self, frame_buffer):
        self._handle_events()
        self._render(frame_buffer)
        self.blank = False

    def render_blank(self):
        self._handle_events()
        if not self.blank:
            self._render_blank()
            self.blank = True
