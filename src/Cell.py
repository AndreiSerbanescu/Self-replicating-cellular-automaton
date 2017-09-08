from src import *
import pygame
from src.State import *

class Cell:

    def __init__(self, position):
        self.position = position
        self.bounds = pygame.Rect(position.x * settings.CELLSIZE, \
                                  position.y * settings.CELLSIZE, \
                                  settings.CELLSIZE, settings.CELLSIZE)

        self.state = State.BLACK
        self.__init_colour_dict()

    def render(self, screen):
        pygame.draw.rect(screen, (self.stateColour.get(self.state)), self.bounds)

    def __init_colour_dict(self):
        self.stateColour = dict()


        self.stateColour.update({State.BLACK : (0, 0, 0)})
        self.stateColour.update({State.BLUE : (0, 0, 255)})
        self.stateColour.update({State.RED : (255, 0, 0)})
        self.stateColour.update({State.GREEN : (0, 255, 0)})
        self.stateColour.update({State.YELLOW : (255, 255, 0)})
        self.stateColour.update({State.PURPLE : (128, 0, 128)})
        self.stateColour.update({State.WHITE : (255, 255, 255)})
        self.stateColour.update({State.CYAN : (0, 255, 255)})