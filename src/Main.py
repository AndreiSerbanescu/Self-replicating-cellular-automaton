import pygame
from src import settings
from src.Cell import *
from src.Position import *


pygame.init()

pygame.display.init()
screen = pygame.display.set_mode((settings.SCREENWIDTH, settings.SCREENHEIGHT))
fps_clock = pygame.time.Clock()


#for i in range(Settings.COLLNO):
 #   for j in range(Settings.ROWNO):
  ##      grid.cells[i][j] = Cell(Position(i, j))

WHITE = (255, 255, 255)

is_paused = True
FPS = settings.FPS

cell = Cell(Position(3, 3))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_p:
                is_paused = not is_paused


    if is_paused:
        FPS = 120
    else:
        FPS = settings.FPS

    #mousePos = pygame.mouse.get_pos()
    #if pygame.mouse.get_pressed()[0]:
     #   grid.cells[mousePos[0] // Settings.CELLSIZE][mousePos[1] // Settings.CELLSIZE].is_alive = True

    screen.fill(WHITE)
    cell.render(screen)

    #grid.render(screen)

    #if not is_paused:
     #   grid.update()

    pygame.display.update()
    fps_clock.tick(FPS)