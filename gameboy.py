try:
    from cython import compiled
except ImportError:
    compiled = False

from cpu import CPU
from memory import MMU
from graphics import GPU
from bootrom import BootROM
from cartridge import get_cartridge
from joypad import Joypad
from timer import Timer
from display import Display
import time

V_BLANK, LCD_STAT, TIMER, SERIAL, JOYPAD = range(0, 5)


class Gameboy:
    def __init__(self, gb_file, boot_file=None):
        boot_rom = BootROM(boot_file)
        cartridge = get_cartridge(gb_file)
        timer = Timer()
        joypad = Joypad()
        gpu = GPU()
        memory = MMU(boot_rom, cartridge, gpu, joypad, timer)
        display = Display(joypad)
        cpu = CPU(memory)

        timer.attach_cpu(cpu)
        joypad.attach_cpu(cpu)
        gpu.attach_cpu(cpu)

        self.boot_rom = boot_rom
        self.cartridge = cartridge
        self.timer = timer
        self.joypad = joypad
        self.gpu = gpu
        self.memory = memory
        self.cpu = cpu
        self.display = display

    def tick_frame(self):
        if self.gpu.display_enable:
            start_time = time.time()
            for ly in range(144):
                self.gpu.ly = ly
                self.gpu.check_coincidence()

                # Mode 2
                self.gpu.set_stat_mode(2)
                self.handle_cycles(80)

                # Mode 3
                self.gpu.set_stat_mode(3)
                self.handle_cycles(170)

                self.gpu.scan_line(ly)

                # Mode 0
                self.gpu.set_stat_mode(0)
                self.handle_cycles(206)

            self.cpu.request_interrupt(V_BLANK)
            frame = self.gpu.render()
            self.display.render(frame)

            # Mode 1 (V BLANK)
            for ly in range(144, 154):
                self.gpu.ly = ly
                self.gpu.check_coincidence()

                # Mode 1
                self.gpu.set_stat_mode(1)
                self.handle_cycles(456)

            end_time = time.time()
            # Time so as to adjust the frame rate!!
            if start_time - end_time < 0.00837:
                time.sleep(0.00837 - (start_time - end_time))

        else:
            self.display.render_blank()
            self.gpu.set_stat_mode(0)
            self.gpu.ly = 0
            self.gpu.check_coincidence()
            for y in range(154):
                self.handle_cycles(456)

    def handle_cycles(self, num_cycles):
        cycles = 0
        while cycles < num_cycles:
            ticks = self.cpu.tick()
            self.timer.tick(ticks)
            cycles += ticks

    def mainloop(self):
        while True:
            self.tick_frame()

