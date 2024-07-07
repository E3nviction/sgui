"""
Sgui Draw builtin component 1.0.0
"""

import pygame
from pygame import gfxdraw

class shape():
    """
    shape builtin component 1.0.0
    """

    def rectangle(
        surface,
        color:tuple,
        rect,
        border_radius:int=5,
        border_radius_topleft:int=0,
        border_radius_topright:int=0,
        border_radius_bottomleft:int=0,
        border_radius_bottomright:int=0,
        width:int=0
        ):
        """
        Draw a rectangle.

        surface (Surface): The surface to draw on.
        color (RGB tuple/RGBA tuple): The color of the rectangle.
        rect (Rect): The rectangle to draw.
        border_radius (int): The border radius of the rectangle.
        border_radius_topleft (int): The border radius of the top left corner.
        border_radius_topright (int): The border radius of the top right corner.
        border_radius_bottomleft (int): The border radius of the bottom left corner.
        border_radius_bottomright (int): The border radius of the bottom right corner.
        width (int): The width of the rectangle.
        """
        color = pygame.Color(color)
        rect = pygame.Rect(rect)
        if not border_radius_bottomleft and not border_radius_bottomright and not border_radius_topleft and not border_radius_topright:
            shape._draw_rect_alpha(surface, color, rect, width, border_radius, border_radius, border_radius, border_radius)
        else:
            shape._draw_rect_alpha(surface, color, rect, width, border_radius_bottomright, border_radius_bottomleft, border_radius_topright, border_radius_topleft)

    def circle(surface, color:tuple, center:tuple, radius:int=5):
        """
        Draw a circle.

        surface (Surface): The surface to draw on.
        color (RGB tuple/RGBA tuple): The color of the circle.
        center (tuple): The center of the circle.
        radius (int): The radius of the circle.
        """
        color = pygame.Color(color)
        #shape._draw_aacircle_alpha(surface, color, center, radius)
        #shape._draw_circle_alpha(surface, color, center, radius)
        shape.rectangle(surface, color, (center[0]-radius, center[1]-radius, radius*2, radius*2), 9999)

    def line(surface, color, start, end, radius=5):
        """
        Draw a line.

        surface (Surface): The surface to draw on.
        color (RGB tuple/RGBA tuple): The color of the line.
        start (tuple): The start of the line.
        end (tuple): The end of the line.
        radius (int): The radius of the line.
        """
        color = pygame.Color(color)
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int(start[0] + float(i) / distance * dx)
            y = int(start[1] + float(i) / distance * dy)
            shape._draw_rect_alpha(surface, color, (x,y-radius,radius*2,radius*2), 0,9999,9999,9999,9999)
    
    def _draw_rect_alpha(
        surface,
        color:tuple,
        rect,
        width:int=0,
        border_radius_bottomright:int=-1,
        border_radius_bottomleft:int=-1,
        border_radius_topright:int=-1,
        border_radius_topleft:int=-1
        ):
        """
        Draw a rectangle with transparency.

        surface (Surface): The surface to draw on.
        color (RGB tuple/RGBA tuple): The color of the rectangle.
        rect (Rect): The rectangle to draw.
        width (int): The width of the rectangle.
        border_radius_bottomright (int): The border radius of the bottom right corner.
        border_radius_bottomleft (int): The border radius of the bottom left corner.
        border_radius_topright (int): The border radius of the top right corner.
        border_radius_topleft (int): The border radius of the top left corner.
        """
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), width, 0, border_radius_bottomright, border_radius_bottomleft, border_radius_topright, border_radius_topleft)
        surface.blit(shape_surf, rect)
    
    def _draw_polygon_alpha(surface, color:tuple, points:list):
        """
        Draw a polygon with transparency.

        surface (Surface): The surface to draw on.
        color (RGB tuple/RGBA tuple): The color of the polygon.
        points (list): The points of the polygon.
        """
        lx, ly = zip(*points)
        min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
        target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
        surface.blit(shape_surf, target_rect)
    
    def _draw_aacircle_alpha(surface, color:tuple, center:tuple, radius:int):
        """
        Draw an antialiased circle with transparency.

        surface (Surface): The surface to draw on.
        color (RGB tuple/RGBA tuple): The color of the circle.
        center (tuple): The center of the circle.
        radius (int): The radius of the circle.
        """
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        gfxdraw.aacircle(shape_surf, radius, radius, radius, color)
        surface.blit(shape_surf, target_rect)
    
    def _draw_circle_alpha(surface, color:tuple, center:tuple, radius:int):
        """
        Draw a circle with transparency.

        surface (Surface): The surface to draw on.
        color (RGB tuple/RGBA tuple): The color of the circle.
        center (tuple): The center of the circle.
        radius (int): The radius of the circle.
        """
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        gfxdraw.filled_circle(shape_surf, radius, radius, radius, color)
        surface.blit(shape_surf, target_rect)
