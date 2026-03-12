# Game Boy Emulator

A Game Boy (DMG) emulator written in Python, with optional Cython compilation for improved performance. Renders graphics and audio through SDL2 via pygame and PySDL2.

[Demo video](https://www.youtube.com/watch?v=GABvbq5cPyk)

## Prerequisites

### macOS

```bash
brew install sdl2 sdl2_mixer pkg-config
```

### Linux (Debian/Ubuntu)

```bash
sudo apt-get install libsdl2-2.0-0 libsdl2-mixer-2.0-0 libsdl2-dev libsdl2-mixer-dev
```

### Python dependencies

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py -c <rom_file>
```

### Options

| Flag | Description |
|---|---|
| `-c`, `--cartridge` | Path to a `.gb` ROM file (required) |
| `-b`, `--boot_file` | Path to a bootstrap ROM for the boot sequence |
| `-s`, `--save_file` | Path to a `.save` file to resume from |
| `--stretch` | Stretch the display to fill the window |
| `--most_recent` | Load the most recent save from the `SAVE/` directory |

### Examples

```bash
# Run a ROM
python3 main.py -c roms/tetris.gb

# Run with the original boot animation
python3 main.py -c roms/tetris.gb -b dmg_boot.bin

# Resume from a save file
python3 main.py -c roms/tetris.gb -s "SAVE/TETRIS[01 Jan 2025 12:00:00].save"

# Resume from the most recent save
python3 main.py -c roms/tetris.gb --most_recent
```

## Controls

### Game Boy buttons

| Key | Button |
|---|---|
| Arrow keys | D-Pad |
| A | A |
| B | B |
| Space | Select |
| Enter | Start |

### Emulator controls

| Key | Action |
|---|---|
| S | Save state to `SAVE/` directory |
| M | Toggle audio mute |
| F | Toggle between normal and double speed |
| Q | Quit |

## Architecture

The emulator mirrors the real Game Boy hardware, with each module corresponding to a physical component.

```
main.py                  CLI entry point
  └── gameboy.py         Main loop and frame timing
        ├── cpu.py       Sharp LR35902 CPU — fetch/decode/execute cycle
        │   └── instructions.py   Opcode implementations
        ├── memory.py    MMU — address bus routing and memory-mapped I/O
        ├── graphics.py  GPU/PPU — background, window, and sprite rendering
        ├── display.py   Screen output and input handling (pygame / SDL2)
        ├── mixer.py     APU — 4-channel audio mixer and register interface
        │   └── channel.py   Low-level waveform playback (PySDL2)
        ├── cartridge.py ROM loading and memory bank controllers (MBC)
        ├── bootrom.py   Optional bootstrap ROM (Nintendo logo scroll)
        ├── timer.py     Hardware timer and divider register
        └── joypad.py    Button input and interrupt signaling
```

### Emulation loop

Each frame (`gameboy.tick_frame`) follows the real scanline timing of the Game Boy's PPU:

1. **144 visible scanlines** — each cycles through Mode 2 (OAM search), Mode 3 (pixel transfer), and Mode 0 (H-blank)
2. **10 V-blank scanlines** (Mode 1) — the CPU continues running while the screen is not being drawn
3. **Frame pacing** — the elapsed time is measured and the loop sleeps to maintain ~59.7 FPS (matching the original 4.194 MHz clock)

The CPU, timer, and audio are ticked in lockstep within each scanline, keeping all subsystems synchronized.

### Audio

The `Mixer` emulates the Game Boy's four sound channels:

| Channel | Type | Features |
|---|---|---|
| Sound 1 | Pulse wave | Frequency sweep, volume envelope, duty cycle |
| Sound 2 | Pulse wave | Volume envelope, duty cycle (no sweep) |
| Sound 3 | Custom wave | 32-sample waveform from Wave RAM |
| Sound 4 | Noise | LFSR-based (15-bit white noise / 7-bit metallic), volume envelope |

All channels are driven by a 512 Hz frame sequencer that clocks length counters, volume envelopes, and frequency sweeps.

## Implementation details

### CPU (`cpu.py`, `instructions.py`)

Emulates the Sharp LR35902 — the Game Boy's 8-bit processor. The `CPU` class holds the register file: 8-bit registers `A`, `B`, `C`, `D`, `E`, four flag bits (`Z`, `N`, `H`, `C`), a 16-bit combined `HL` register, a 16-bit program counter (`PC`), and a stack pointer (`SP`). An interrupt master enable flag (`ime`) gates all interrupt handling.

Each `tick()` first checks for pending interrupts. If `ime` is set and a requested interrupt is enabled, the CPU pushes the current PC onto the stack and jumps to the corresponding interrupt service routine (V-Blank at `0x0040`, LCD STAT at `0x0048`, Timer at `0x0050`, Serial at `0x0058`, Joypad at `0x0060`). Then it fetches and executes the next opcode.

`instructions.py` is a generated file containing individual Python functions for every Game Boy opcode (including CB-prefixed bit operations). Each function mutates the CPU state directly and returns the number of T-cycles consumed, which the caller uses to keep subsystems in sync.

### Memory (`memory.py`)

The `MMU` (Memory Management Unit) implements the Game Boy's 16-bit address bus. Reads and writes are routed to the correct subsystem based on the address:

| Address range | Region |
|---|---|
| `0x0000–0x00FF` | Boot ROM (when mapped), then cartridge ROM |
| `0x0000–0x7FFF` | Cartridge ROM (bank 0 + switchable bank) |
| `0x8000–0x9FFF` | Video RAM (GPU) |
| `0xA000–0xBFFF` | External RAM (cartridge) |
| `0xC000–0xDFFF` | Work RAM (8 KB) |
| `0xE000–0xFDFF` | Echo of Work RAM |
| `0xFE00–0xFE9F` | OAM — sprite attribute table (GPU) |
| `0xFF00` | Joypad register |
| `0xFF04–0xFF07` | Timer registers |
| `0xFF10–0xFF3F` | Audio registers (Mixer) |
| `0xFF40–0xFF4B` | GPU registers (LCDC, STAT, scroll, palettes) |
| `0xFF46` | DMA transfer — bulk-copies 160 bytes to OAM |
| `0xFF50` | Boot ROM disable latch |
| `0xFF80–0xFFFE` | High RAM (127 bytes) |
| `0xFFFF` | Interrupt Enable register |

### Graphics (`graphics.py`)

The `GPU` manages 8 KB of video RAM, a 160-byte OAM sprite table, and an unpacked tile cache (384 tiles x 64 pixels each). When VRAM is written, tiles are decoded on the fly from the Game Boy's 2bpp format into individual pixel values for fast lookup at render time.

Rendering happens once per frame in `render()`. For each of the 160x144 pixels it:

1. Checks the **window layer** — if enabled and the pixel falls within the window region, it looks up the tile from the window tile map.
2. Falls back to the **background layer** — scrolls by `SCX`/`SCY` and indexes into the background tile map.
3. Overlays **sprites** — iterates all 40 OAM entries, supports 8x8 and 8x16 (large) tiles, X/Y flipping, two palettes (`OBP0`/`OBP1`), and priority over background.

Palette registers (`BGP`, `OBP0`, `OBP1`) map 2-bit color indices to a 4-shade grayscale palette. The STAT register and LY/LYC coincidence checks trigger LCD STAT interrupts when enabled.

### Display (`display.py`)

Uses pygame with hardware-accelerated double buffering (`SCALED | DOUBLEBUF | HWSURFACE`) to present the 160x144 frame buffer. Handles all keyboard input by polling pygame events each frame and dispatching them to the joypad or emulator commands (save, mute, speed toggle, quit).

### Cartridge (`cartridge.py`)

Loads a `.gb` ROM file and selects the correct memory bank controller based on the cartridge type byte at `0x0147` in the ROM header. Supported controller types:

- **NoController** — plain 32 KB ROMs, optionally with 8 KB of static RAM.
- **MBC1** — up to 2 MB ROM / 32 KB RAM. Supports ROM banking (5-bit bank register with upper 2-bit extension) and RAM banking mode. Handles the special-case bank numbers `0x00`, `0x20`, `0x40`, `0x60` which auto-increment to the next bank.
- **MBC3** — up to 2 MB ROM / 64 KB RAM. Includes a real-time clock (RTC) with latch support. The `RTC` class tracks elapsed wall-clock time and exposes seconds, minutes, hours, and a 9-bit day counter through memory-mapped registers `0x08–0x0C`.

All controllers implement `save()` and `load()` for full state serialization of selected banks and external RAM contents.

### Boot ROM (`bootrom.py`)

Wraps an optional bootstrap ROM (the 256-byte program that scrolls the Nintendo logo and plays the chime on real hardware). If no boot ROM file is provided, a minimal stub is injected that sets the stack pointer to `0xFFFE` and immediately writes `0x01` to `0xFF50` to unmap itself, letting execution fall through to the cartridge.

### Timer (`timer.py`)

Implements the Game Boy's four timer registers:

- **DIV** (`0xFF04`) — incremented every 256 CPU cycles. Writing any value resets it to zero.
- **TIMA** (`0xFF05`) — the main timer counter, incremented at a rate selected by TAC. On overflow it reloads from TMA and fires a Timer interrupt.
- **TMA** (`0xFF06`) — the value TIMA resets to on overflow.
- **TAC** (`0xFF07`) — timer control. Bit 2 enables/disables the timer; bits 0–1 select the clock divider (4096, 262144, 65536, or 16384 Hz).

### Joypad (`joypad.py`)

Models the Game Boy's multiplexed button register at `0xFF00`. The Game Boy has 8 buttons split into two groups — directions (right, left, up, down) and actions (A, B, Select, Start). The game selects which group to read by writing to bits 4–5 of the joypad register, then reads the result from bits 0–3. A Joypad interrupt is requested whenever a button is pressed.

### Audio mixer (`mixer.py`)

The `Mixer` is the top-level audio controller, mapping Game Boy I/O registers `0xFF10–0xFF3F` to four sound generators (`Sound1`–`Sound4`). It handles:

- **NR50** (`0xFF24`) — master volume for left and right outputs (3-bit each, 0–7).
- **NR51** (`0xFF25`) — per-channel stereo panning (each channel can be routed to left, right, both, or neither).
- **NR52** (`0xFF26`) — master on/off. Disabling resets all sound generators. Reading returns per-channel enabled status in the lower nibble.

Each sound class manages its own registers, frame sequencer counter, and internal state (sweep, envelope, length). On every `tick()` the 512 Hz frame sequencer steps through an 8-step cycle that clocks length counters (steps 0, 2, 4, 6), frequency sweep (steps 2, 6), and volume envelope (step 7).

### Audio channels (`channel.py`)

`PyGameChannel` bridges the emulated sound generators to real audio output via `pygame.mixer`. The mixer is initialized once at 44.1 kHz, signed 8-bit stereo. Each channel's `play()` method takes a waveform array and a frequency, resamples it to the target sample rate using nearest-neighbor interpolation with NumPy, and loops it continuously via `pygame.sndarray`. Per-channel stereo output and master volume are controlled through pygame's channel volume API.

### Save system (`gameboy.py`)

The emulator supports full save states. Pressing **S** during gameplay serializes the complete state of every subsystem (CPU registers, cartridge RAM and bank selection, all memory regions, GPU state, timer, joypad, and audio) into a binary `.save` file in the `SAVE/` directory. The filename includes the game title and a human-readable timestamp. On startup, a specific save can be loaded with `--save_file`, or the most recent one can be auto-detected with `--most_recent`.

## Cython compilation (optional)

Compiling with Cython significantly improves emulation speed. `pkg-config` is used to obtain the necessary C flags for SDL2.

```bash
# Get the SDL2 compiler flags
pkg-config --cflags --libs sdl2

# Build (substitute the output of the previous command)
python3 setup.py build_ext --inplace <pkg-config output>
```

For example, on a typical Linux system:

```bash
python3 setup.py build_ext --inplace -D_REENTRANT -I/usr/include/SDL2 -lSDL2
```
