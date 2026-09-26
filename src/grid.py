import pygame
import random

#need to sort out saving borders when defined like the grid.
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

def bordercreate(rows):
    colour = "blue"
    number = random.randint(1, 25) # selects yellow position
    number2 = random.randint(1,25) # selects red position
    if number == number2:
         number2 = random.choice([i for i in range(1, 25) if i != number])
    yellwall = random.randint(1,4)
    redwall = random.randint(1,4)
    grid1 = []
    grid2 = []
    grid3 = []
    grid4 = []
    for i in range(rows):
        
        colour1 = "blue"
        colour2 = "blue"
        colour3 = "blue"
        colour4 = "blue"
        if i == number:
            if yellwall == 1:
                colour1 = "yellow"
            elif yellwall == 2:
                colour2 = "yellow"
            elif yellwall == 3:
                colour3 = "yellow"
            elif yellwall == 4:
                colour4 = "yellow"
        if i == number2:
            if redwall == 1:
                colour1 = "red"
            elif redwall == 2:
                colour2 = "red"
            elif redwall == 3:
                colour3 = "red"
            elif redwall == 4:
                colour4 = "red"
        grid1.append(colour1)
        grid2.append(colour2)
        grid3.append(colour3)
        grid4.append(colour4)       
    return grid1, grid2, grid3, grid4

def gridbordercreater(scr,g1,g2,g3,g4):
    gridwalls = [g1, g2, g3, g4]
    sx = 80
    sy = 80
    #top
    for i in range(27):
        pygame.draw.rect(scr, g1[i], (sx, sy, 20, 20))
        sx+=20
    #bottom
    sy = 600
    sx = 80
    for i in range(27):
        pygame.draw.rect(scr, g2[i], (sx, sy, 20, 20))
        sx+=20
    #left
    sy = 80
    sx = 80
    for i in range(27):
        pygame.draw.rect(scr, g3[i], (sx, sy, 20, 20))
        sy+=20
    #right
    sy = 80
    sx = 600
    for i in range(27):
        pygame.draw.rect(scr, g4[i], (sx, sy, 20, 20))
        sy+=20
        



def griddraw(scr,grid,valx,valy):
    squaresize = 20
    placement = pygame.Vector2(valx,valy)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(scr,grid[i][j],(placement.x + (i * squaresize),placement.y + (j * squaresize),squaresize,squaresize))