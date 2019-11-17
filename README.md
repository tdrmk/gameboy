
Requires sdl2, sdl2_mixer to be installed.
MAC installed via 
    
    brew install sdl2 sdl2_mixer
    brew install pkg-config

`pkg-config` is used to obtain c-flags to pass while compiling using cython.

In Linux using apt-get use 

    sudo apt-get install libsdl2-2.0-0 libsdl2-mixer-2.0-0 libsdl2-dev libsdl2-mixer-dev 
     
To compile with cython use
    
    pkg-config --cflags --libs sdl2
    python3 setup.py build_ext --inplace {output of previous command}
    python3 setup.py build_ext --inplace  -D_REENTRANT -I/usr/include/SDL2 -lSDL2

 


