# Aplicação de matemática e física em um jogo
# -- Matheus Marchi Moro

# Importação das bibliotecas pygame e math
import pygame
from math import pi
from auxmath import Vect

# Importação de funcionalidades do pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_a, K_d, K_q, K_e,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

Clock = pygame.time.Clock()


# Variáveis:

# JOGO:
# Frames por segundo
fps = 60

# Comprimento e altura do plano
screen_width = 800
screen_height = 600

# Texto
font = pygame.font.SysFont(None, 20)

# Setar a tela
screen = pygame.display.set_mode([screen_width, screen_height])

# Centro do plano
center_x = screen_width // 2
center_y = screen_height // 2

# Tempo do sistema
time = 0
time_inc = 1 / fps

# CORPO:
# Posição inicial
pos0_v = Vect(center_x - 100, center_y)

# Posição atual
pos_v = Vect(pos0_v.x, pos0_v.y)

# Variação de posição
pos_x_var = 0
pos_y_var = 0

# Velocidade inicial
speed0_v = Vect(20, -50)
sqrd_speed0_v = speed0_v * speed0_v

# Velocidade atual
speed_v = Vect(speed0_v.x, speed0_v.y)

# Aceleração inicial
accel0_v = Vect(1, 9.81)

# Aceleração atual
accel_v = Vect(accel0_v.x, accel0_v.y)


# EXECUÇÃO DO JOGO: 
running = True

# Executa até o usuário fechar a tela
while running:
    # Tratamento de eventos
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Manipulação do ângulo do vetor de velocidade
            if event.key == K_q:
                speed_v.inc_alpha(pi/18)
            if event.key == K_e:
                speed_v.inc_alpha(-pi/18)

            # Manipulação do tempo
            if event.key == K_d:
                time_inc += 1 / (fps * 2)
            if event.key == K_a:
                time_inc -= 1 / (fps * 3)

        if event.type == pygame.QUIT:
            running = False


    # Preenche toda a tela com uma cor
    screen.fill((0, 0, 0))

    # CORPO:
    # Círculo que representa o corpo
    pygame.draw.circle(screen, (255, 255, 255), # Tela onde o círculo será desenhado / Cor
    (pos_v.x, pos_v.y), 15) # Centro do círculo / Raio

    # Vetor de posição
    pygame.draw.line(screen, (255, 128, 255),
    (center_x, center_y), # Ponto inicial
    (pos_v.x, pos_v.y), 2) # Ponto final / Espessura

    # Vetor de velocidade
    pygame.draw.line(screen, (0, 0, 255),
    (pos_v.x, pos_v.y),
    ((pos_v.x + speed_v.x, pos_v.y + speed_v.y)), 2)

    # Vetor de aceleração
    pygame.draw.line(screen, (255, 100, 100),
    (pos_v.x, pos_v.y),
    ((pos_v.x + accel_v.x, pos_v.y + accel_v.y)), 2)

    # CENTRO:

    # Vetor de velocidade do corpo
    pygame.draw.line(screen, (0, 0, 255),
    (center_x, center_y),
    ((center_x + speed_v.x), (center_y + speed_v.y)), 2)

    # Vetor de aceleração do corpo
    pygame.draw.line(screen, (255, 100, 100),
    (center_x, center_y),
    ((center_x + accel_v.x), (center_y + accel_v.y)), 2)

    # EIXO HORIZONTAL:
    pygame.draw.line(screen, (32, 64, 64),
    (0, center_y),
    (screen_width, center_y), 1)

    # Texto (desenho de texto e atualização de variáveis relacionadas a texto)
    # arr_text = [FPS, Informação, Posição, Velocidade, Aceleração, Tempo]
    arr_text = [
        font.render(f'FPS: {Clock.get_fps():.02f}', True, (255, 255, 255)),
        font.render('1 pixel = 1 metro', True, (255, 255, 255)),
        font.render(f'Posição: ({pos_v.x:.02f}, {pos_v.y:.02f})', True, (255, 255, 255)),
        font.render(f'Velocidade: ({speed_v.x:.02f}, {speed_v.y:.02f})', True, (255, 255, 255)),
        font.render(f'Aceleração: ({accel_v.x:.02f}, {accel_v.y:.02f})', True, (255, 255, 255)),
        font.render(f'Tempo (segundos): {time:.02f}', True, (255, 255, 255))
    ]
    i = 16
    for text in arr_text:
        screen.blit(text, (12, i))
        i += 16

    # Mostra a tela desenhada para o usuário
    pygame.display.flip()


    # Atualização de variáveis

    # Tempo
    time += time_inc

    # Variação de posição
    pos_x_var = ((speed_v.x) ** 2 - sqrd_speed0_v.x) / (2 * accel0_v.x)
    pos_y_var = ((speed_v.y) ** 2 - sqrd_speed0_v.y) / (2 * accel0_v.y)

    # Posição do corpo em função do tempo
    # Não pode depender do tempo!/
    pos_v.x = ((speed_v.x + speed0_v.x) / 2) * time + pos0_v.x
    pos_v.y = ((speed_v.y + speed0_v.y) / 2) * time + pos0_v.y
    # pos_v.x += pos_x_var
    # pos_v.y += pos_y_var

    # Velocidade do corpo em função do tempo
    # Não pode depender do tempo!
    speed_v.x = speed0_v.x + accel_v.x * time
    speed_v.y = speed0_v.y + accel_v.y * time

    # pygame.time.delay(1000//fps)
    Clock.tick(fps)


# Termina o pygame
pygame.quit()