"""
Sgui Node builtin component 1.0.0
"""

import pygame
import sguie.sgui as sgui
import sguie.components.built_ins.draw as draw
import sguie.components.built_ins.implement as implement

class add:
    def frame(surface, color, rect, width, border_radius=5, border_radius_topleft=0, border_radius_topright=0, border_radius_bottomleft=0, border_radius_bottomright=0, lt=0):
        """
        (Static)
        A function to draw a filled rectangular frame with rounded corners on a given surface.

        Parameters:
        - surface: (surface)
        - colors: (list)
        - rect: (Rect)
        - border_radius: (int)
        - border_radius_topleft: (int)
        - border_radius_topright: (int)
        - border_radius_bottomleft: (int)
        - border_radius_bottomright: (int)
        - lt: (int)
        """
        rect = pygame.Rect(rect)
        if sgui.draw_cache:
            implement._add_to_draw_cache(f"rect{len(sgui.draw_cache)}", draw.draw.aaroundedfilled_rect, surface=surface, color=color, rect=rect, width=width, border_radius=border_radius, border_radius_topleft=border_radius_topleft, border_radius_topright=border_radius_topright, border_radius_bottomleft=border_radius_bottomleft, border_radius_bottomright=border_radius_bottomright)
        else:
            implement._add_to_draw_cache(f"rect", draw.draw.aaroundedfilled_rect, surface=surface, color=color, rect=rect, width=width, border_radius=border_radius, border_radius_topleft=border_radius_topleft, border_radius_topright=border_radius_topright, border_radius_bottomleft=border_radius_bottomleft, border_radius_bottomright=border_radius_bottomright)
