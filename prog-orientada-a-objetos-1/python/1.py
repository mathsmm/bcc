# Aplicação de matemática e física em um jogo
# -- Matheus Marchi Moro

# Importação das bibliotecas pygame e math
import pygame
from math import asin, acos
from auxmath import Vect

# Importação de funcionalidades do pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_a,
    K_d,
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
# pos0_body_1 = Vect(x, y)
pos0_x = center_x - 100
pos0_y = center_y

# Posição atual
pos_x = pos0_x
pos_y = pos0_y

# Velocidade inicial
speed0_x = 20
speed0_y = -50

# Velocidade atual
speed_x = speed0_x
speed_y = speed0_y

# Aceleração inicial
accel0_x = 0
accel0_y = 9.81

# Aceleração atual
accel_x = accel0_x
accel_y = accel0_y

# Tamanho do vetor de velocidade
# Posteriormente é usado como se fosse uma hipotenusa

# Calculado com pitágoras
# Distância entre dois pontos:
# ((Xb - Xa) ** 2 + (Yb - Ya) ** 2) ** 0.5
speed_vect_size = (speed_x ** 2 + speed_y ** 2) ** 0.5

# Seno e cosseno do vetor de velocidade
speed_vect_sin = speed_y / speed_vect_size
speed_vect_cos = speed_x / speed_vect_size


# Direção do vetor de velocidade
speed_alpha = 0
# Se o tamanho do vetor de velocidade for zero,
# ocorre uma divisão por zero. Isto deve ser tratado
if speed_vect_size != 0:
    # Apontando para o primeiro quadrante (seno positivo e cosseno positivo)
    if speed_vect_sin > 0 and speed_vect_cos > 0:
        speed_alpha = asin(speed_vect_sin)


# EXECUÇÃO DO JOGO: 
running = True

# Executa até o usuário fechar a tela
while running:
    # Tratamento de eventos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            #     speed_y = -10
            # if event.key == pygame.K_DOWN:
            #     accel_y += 0.1

            # Manipulação do tempo
            if event.key == pygame.K_d:
                time_inc += 1 / (fps * 2)
            if event.key == pygame.K_a:
                time_inc -= 1 / (fps * 3)

        if event.type == pygame.QUIT:
            running = False


    # Preenche toda a tela com uma cor
    screen.fill((0, 0, 0))

    # CORPO:
    # Círculo que representa o corpo
    pygame.draw.circle(screen, (255, 255, 255), # Tela onde o círculo será desenhado / Cor
    (pos_x, pos_y), 15) # Centro do círculo / Raio

    # Vetor de posição
    pygame.draw.line(screen, (255, 128, 255),
    (center_x, center_y), # Ponto inicial
    (pos_x, pos_y), 2) # Ponto final / Espessura

    # Vetor de velocidade
    pygame.draw.line(screen, (0, 0, 255),
    (pos_x, pos_y),
    ((pos_x + speed_x, pos_y + speed_y)), 2)

    # Vetor de aceleração
    pygame.draw.line(screen, (255, 100, 100),
    (pos_x, pos_y),
    ((pos_x + accel_x, pos_y + accel_y)), 2)

    # CENTRO:

    # Vetor de velocidade do corpo
    pygame.draw.line(screen, (0, 0, 255),
    (center_x, center_y),
    ((center_x + speed_x), (center_y + speed_y)), 2)

    # Vetor de aceleração do corpo
    pygame.draw.line(screen, (255, 100, 100),
    (center_x, center_y),
    ((center_x + accel_x), (center_y + accel_y)), 2)

    # EIXO HORIZONTAL:
    pygame.draw.line(screen, (32, 64, 64),
    (0, center_y),
    (screen_width, center_y), 1)

    # Texto (desenho de texto e atualização de variáveis relacionadas a texto)
    # arr_text = [FPS, Informação, Posição, Velocidade, Aceleração, Tempo]
    arr_text = [
        font.render(f'FPS: {Clock.get_fps():.02f}', True, (255, 255, 255)),
        font.render('1 pixel = 1 metro', True, (255, 255, 255)),
        font.render(f'Posição: ({pos_x:.02f}, {pos_y:.02f})', True, (255, 255, 255)),
        font.render(f'Velocidade: ({speed_x:.02f}, {speed_y:.02f})', True, (255, 255, 255)),
        font.render(f'Aceleração: ({accel_x:.02f}, {accel_y:.02f})', True, (255, 255, 255)),
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

    # Posição do corpo em função do tempo
    # pos_x = pos0_x + (speed0_x * time) + (1 / 2 * accel_x * time ** 2)
    # pos_y = pos0_y + (speed0_y * time) + (1 / 2 * accel_y * time ** 2)
    pos_x = ((speed_x + speed0_x) / 2) * time + pos0_x
    pos_y = ((speed_y + speed0_y) / 2) * time + pos0_y

    # Velocidade do corpo em função do tempo
    speed_x = speed0_x + accel_x * time
    speed_y = speed0_y + accel_y * time

    # speed_x = (speed0_x ** 2 + 2 * accel_x * (pos0_x - pos_x)) ** 0.5
    # speed_y = (speed0_y ** 2 + 2 * accel_y * (pos0_y - pos_y)) ** 0.5

    # pygame.time.delay(1000//fps)
    Clock.tick(fps)


# Termina o pygame
pygame.quit()