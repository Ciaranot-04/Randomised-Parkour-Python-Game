import pygame
import grid
import random

pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
mainfps = 60
running = True

tempcol = "#4BF25C"
playerpos = pygame.Vector2(10,10)


def drawplayer():
    pygame.draw.rect(screen, tempcol, (playerpos.x, playerpos.y, 20, 20))
grids = grid.gridcreate(25,25)
while running:
    #close on X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#D5653C")

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
    grid.gridbordercreater(screen)
    grid.griddraw(screen,grids,100,100)
    drawplayer()
    pygame.display.flip()

    #framerate with framerate independence
    dt = clock.tick(60) / 1000

pygame.quit()
