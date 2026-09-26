import pygame
import random

pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
mainfps = 60
running = True

tempcol = "#4BF25C"
playerpos = pygame.Vector2(10,10)


def gridcreate(rows,cols):
    colour = "blue"
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            number = random.randint(1, 2)
            if number == 1:
                colour = "white"
            else:
                colour = "blue"
            row.append(colour)
        grid.append(row)

    return grid

def gridbordercreater(scr):
    colour = "black"
    x,y =80,80
    amm = 27
    startpos = pygame.Vector2(x,y)
    #top
    for i in range(amm):
        pygame.draw.rect(scr, colour, (startpos.x, startpos.y, 20, 20))
        startpos.x+=20
    #bottom
    startpos.y = 600
    startpos.x = 80
    for i in range(amm):
            pygame.draw.rect(scr, colour, (startpos.x, startpos.y, 20, 20))
            startpos.x+=20
    #left
    startpos.y = 80
    startpos.x = 80
    for i in range(amm):
            pygame.draw.rect(scr, colour, (startpos.x, startpos.y, 20, 20))
            startpos.y+=20
    #right
    startpos.y = 80
    startpos.x = 600
    for i in range(amm):
            pygame.draw.rect(scr, colour, (startpos.x, startpos.y, 20, 20))
            startpos.y+=20
    



def griddraw(scr,grid,valx,valy):
    squaresize = 20
    placement = pygame.Vector2(valx,valy)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(scr,grid[i][j],(placement.x + (i * squaresize),placement.y + (j * squaresize),squaresize,squaresize))

def drawplayer():
    pygame.draw.rect(screen, tempcol, (playerpos.x, playerpos.y, 20, 20))
grid = gridcreate(25,25)
while running:
    #close on X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#B2664B")

    #control
    k = pygame.key.get_pressed()
    if k[pygame.K_w]:
        playerpos.y -= 5
    if k[pygame.K_s]:
        playerpos.y += 5
    if k[pygame.K_a]:
        playerpos.x -= 5
    if k[pygame.K_d]:
        playerpos.x += 5

    #render
    gridbordercreater(screen)
    griddraw(screen,grid,100,100)
    drawplayer()
    pygame.display.flip()

    #framerate with framerate independence
    dt = clock.tick(60) / 1000

pygame.quit()

#note 15x17 grid