import sys
import pygame as pg

from .settings import AlienInvasionWindowSettings
from .ship import Ship


class AlienInvasion:

    def __init__(self):
        pg.init()
        self.settings = AlienInvasionWindowSettings()
        # surface (we will call screen as surface which is window)
        self.screen = pg.display.set_mode((self.settings.width, self.settings.height))
        self.clock = pg.time.Clock()
        pg.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pg.event.get():
                match event.type:
                    case pg.QUIT:
                        self.close_game()
            
            self.screen.fill(self.settings.bg_color)
            self.ship.blit()
            # draws most recent screen on window
            pg.display.flip()
            # draw the screen exactly 60 times per seconds (to adjust frame rate issue on different devices if any)
            self.clock.tick(60)

    def close_game(self):
        sys.exit()

