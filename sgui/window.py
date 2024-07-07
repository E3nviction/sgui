"""
Sgui Window Module 1.0.0
"""

import pygame

def get_display():
    """Return the display object representing the current display"""
    return pygame.display.get_display()
def get_surface():
    """Return the surface object representing the current display"""
    return pygame.display.get_surface()
def init():
    """Initializes all necessary modules and sets up the window"""
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("sgui window")
    pygame.display.set_mode((800, 600))
def Quit():
    """Quits Sgui."""
    pygame.quit()
def setwindow(width:int=800, height:int=600, title:str="sgui window", flags=0, depth=0, display=0, vsync=1):
    """
    Set the window properties for the GUI.

    width (int) width of the window = 800
    height (int) height of the window = 600
    title (str) title of the window = "sgui window"
    vsync (int 1/0) toggle for vsync = 1
    """
    pygame.display.set_caption(title)
    pygame.display.set_mode((width, height), flags=flags, depth=depth, display=display, vsync=vsync)
def bgfill(surface=pygame.display.get_surface(), color:tuple=(0, 0, 0)):
    """
    Fills the background of the Sgui display surface with the specified RGB color.

    surface (Surface)
    color (RGB tuple)
    """
    surface.fill(color)
