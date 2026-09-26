import pygame
import random

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