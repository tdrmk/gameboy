import argparse

from gameboy import Gameboy

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cartridge", help="GameBoy cartridge rom to use. '.gb' file. (Required)", required=True)
parser.add_argument("-b", "--boot_file", help="bootstrap rom to use for booting. (Optional)", default=None)
parser.add_argument("-s", "--save_file", help="save file to load from. '.save' file. (Optional)", default=None)
parser.add_argument("--stretch", help="stretch the display to full screen. Default aspect ratio is maintained.",
                    action="store_true")
parser.add_argument("--most_recent", help="Load from the most recent save file from the 'SAVE/' directory. "
                                          "A shortcut over '--save_file' parameter. (Optional)", action="store_true")
args = parser.parse_args()
gb_file = args.cartridge
boot_file = args.boot_file
save_file = args.save_file
stretch = args.stretch
most_recent = args.most_recent

gameboy = Gameboy(
    gb_file.encode(),
    boot_file=boot_file,
    save_file=save_file,
    stretch=stretch,
    most_recent=most_recent
)
gameboy.mainloop()
