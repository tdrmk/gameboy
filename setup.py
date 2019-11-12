from distutils.core import setup

from Cython.Build import cythonize

# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compiler-directives
setup(
    install_requires=[
        "cython",
        "pysdl2",
    ],
    ext_modules=cythonize(
        ['bootrom.py', 'cartridge.py', 'cpu.py', 'display.pyx', 'gameboy.py', 'graphics.py', 'joypad.py',
         'instructions.py', 'joypad.py', 'memory.py', 'timer.py'],
        annotate=True,
        language_level=3,
        compiler_directives={
            "cdivision": True,
            "cdivision_warnings": False,
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
            "nonecheck": False,
            "overflowcheck": False,
        })
)
