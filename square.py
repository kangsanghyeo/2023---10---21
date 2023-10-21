import pygame
from pygame.color import Color


class Square:
    def __init__(self):
        self.sprite_image = 'pygame.draw.rect()'
        self.sprite_width = 10
        self.sprite_height = 10

    def update(self):
        self.calc_next_frame()
        
        rect = (slef.sprite_width *self.current_frame, 0,
                self.sprite_width, self.sprite_height)
        self.image.blit( self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(0, 0, 255))
        
