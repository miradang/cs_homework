import pygame

class Ship:

    def __init__(self, ai_game):
        """
        Docstring for __init__
        
        :param self: initizlie ship
        :param ai_game: get starting location
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship images and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.images.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):

        self.screen.blit(self.image, self.rect)

        
