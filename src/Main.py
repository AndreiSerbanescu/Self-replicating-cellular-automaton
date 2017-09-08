import pygame
from src import settings
from src.Cell import *
from src.Position import *
from src.Grid import *




def fps_count(fpscount):
    fpscount += 1

    if fpscount < 9:
        return "000" + str(fpscount)
    if fpscount < 99:
        return "00" + str(fpscount)

    if fpscount < 999:
        return "0" + str(fpscount)

    return str(fpscount)



pygame.init()

pygame.display.init()
screen = pygame.display.set_mode((settings.SCREENWIDTH, settings.SCREENHEIGHT))
fps_clock = pygame.time.Clock()

grid = Grid()

#for i in range(Settings.COLLNO):
 #   for j in range(Settings.ROWNO):
  ##      grid.cells[i][j] = Cell(Position(i, j))

WHITE = (255, 255, 255)

is_paused = True
FPS = settings.FPS

cell = Cell(Position(3, 3))
fpscount = 0



while True:
    mousePressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_p:
                is_paused = not is_paused

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed = True

    if is_paused:
        FPS = 120
    else:
        FPS = settings.FPS

    mousePos = pygame.mouse.get_pos()
    #if pygame.mouse.get_pressed()[0]:
     #   grid.cells[mousePos[0] // settings.CELLSIZE][mousePos[1] // settings.CELLSIZE].set_next_state()

    if mousePressed:
        grid.cells[mousePos[0] // settings.CELLSIZE][mousePos[1] // settings.CELLSIZE].set_next_state()


    grid.render(screen)

    if not is_paused:
        grid.update()

        fpscount += 1

        if fpscount % 20 == 0:
            count_string = fps_count(fpscount)
            #pygame.image.save(screen, "loop.jpg" + count_string)

    pygame.display.update()
    fps_clock.tick(FPS)