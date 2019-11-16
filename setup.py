from distutils.core import setup
import numpy

from Cython.Build import cythonize

# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compiler-directives
setup(
    ext_modules=cythonize(
        ['bootrom.py', 'cartridge.py', 'cpu.py', 'display.py', 'gameboy.py', 'graphics.py', 'joypad.py',
         'instructions.py', 'joypad.py', 'memory.py', 'timer.py', 'channel.py', 'mixer.py'],
        annotate=True,
        language_level=3,
        include_path=[numpy.get_include()],
        compiler_directives={
            "cdivision": True,
            "cdivision_warnings": False,
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
            "nonecheck": False,
            "overflowcheck": False,
        }),
)
