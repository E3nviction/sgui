"""
Sgui Module 1.0.0
"""

mainloopfunc = None

import pygame

import sgui.window
import sgui.variable

draw_cache = []


def mainloop(mainloop):
    """
    event loop for sgui.

    mainloop (function)
    """
    global mainloopfunc
    mainloopfunc = mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        mainloopfunc()
        pygame.display.flip()