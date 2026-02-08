import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    """
    Docstring for AlienInvasion
    overall class to manage game assesst and behavior
    """
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: start screen
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #set bg color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """"Main game loop"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    sys.exit()
            #redraw screen during each pass thru loop
            self.screen.fill(self.settings.bg_color)

            #make most recent drawn screen visbile
            pygame.display.flip()
            self.clock.tick(60)
    
if __name__=='__main__':
    #make game instance and run
    ai = AlienInvasion()
    ai.run_game()