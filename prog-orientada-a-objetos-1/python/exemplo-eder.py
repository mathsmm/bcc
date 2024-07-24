# Simple pygame program
# Import and initialize the pygame library

import pygame
from math import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True

A = 80
alpha = 0.0

dt = 1/2000

c_x = 250
c_y = 250

o_x = 0
o_y = 0
v_x = A*cos(alpha)
v_y = A*sin(alpha)


# loop de jogo
while running:

    # capturar eventos
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # aqui deveria ter uma lógica


    # atualizar tela
    # limpar a tela
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center

    o_x = o_x + v_x * dt
    o_y = o_y + v_y * dt

    print(v_y)

    pygame.draw.circle(screen, (0, 0, 255), 
        (c_x + o_x, c_y + o_y), 75)

    pygame.draw.line( screen, (255,0,0),
        (c_x + o_x, c_y + o_y), 
        (c_x + o_x +v_x, c_x + o_y + v_y), 1) 

    pygame.draw.line( screen, (255,255,0),
        (c_x + o_x, c_y + o_y), 
        (c_x + o_x - A*sin(alpha), c_x + o_y + A*cos(alpha)), 1) 

    # Flip the display
    pygame.display.flip()

    # mudar os objetos de lugar
    alpha += dt

    # recalcular 
    v_x = A*cos(alpha) 
    v_y = A*sin(alpha)


# Done! Time to quit.

pygame.quit()

