import pygame as pg
from pygame.locals import *
from src.vec2 import Vec2
from src.body_strategy import *
from src.circle_body import CircleBody
from src.rect_body import RectBody
from src.collision_logic import CollisionLogic
from src.time_handler import TimeHandler
from src.body_iterator import BodyIterator

class App:
    def __init__(
        self, 
        fps: int,
        window_width: int, 
        window_height: int
    ) -> None:
        self.running = False
        self.fps = fps
        self.window_width = window_width
        self.window_heigth = window_height
        self.time_handler = TimeHandler(fps)

        # Bodies
        self.body_iter: BodyIterator = None
        self.circ_vtx_qty = 24

        # pygame
        pg.init()
        self.screen = pg.display.set_mode((window_width, window_height))

    def init(self):
        # PREPARAR LISTA DE CORPOS
        self.bodies = []
        for i in range(0, 100):
            self.bodies.append(
                CircleBody(
                    Vec2(80 * ((i % 10) + 1), 40 * ((i // 10) + 1) + 100),
                    Vec2(0, 0),
                    Vec2(0, 9.80665),
                    10,
                    15
                )
            )
            self.bodies[i].move_behav = DoMove(self.bodies[i])
            self.bodies[i].vel_display_behav = DoDisplayVel(self.screen, self.bodies[i])
            self.bodies[i].body_display_behav = DisplayCircle(self.screen, self.bodies[i])

        b1 = CircleBody(Vec2(40, 40), Vec2(35, 35), Vec2(0, 9.80665), 500, 25)
        b1.move_behav = DoMove(b1)
        b1.vel_display_behav = DoDisplayVel(self.screen, b1)
        b1.body_display_behav = DisplayCircle(self.screen, b1)

        r1 = RectBody(Vec2(0, 0), Vec2(0, 0), Vec2(0, 0), 100, self.window_heigth, 20)
        r1.move_behav = DontMove()
        r1.vel_display_behav = DontDisplayVel()
        r1.body_display_behav = DisplayRect(self.screen, r1)

        r2 = RectBody(Vec2(self.window_width - 20, 0), Vec2(0, 0), Vec2(0, 0), 100, self.window_heigth, 20)
        r2.move_behav = DontMove()
        r2.vel_display_behav = DontDisplayVel()
        r2.body_display_behav = DisplayRect(self.screen, r2)

        r3 = RectBody(Vec2(20, 0), Vec2(0, 0), Vec2(0, 0), 100, 20, self.window_width - 40)
        r3.move_behav = DontMove()
        r3.vel_display_behav = DontDisplayVel()
        r3.body_display_behav = DisplayRect(self.screen, r3)

        r4 = RectBody(Vec2(20, self.window_heigth - 20), Vec2(0, 0), Vec2(0, 0), 100, 20, self.window_width - 40)
        r4.move_behav = DontMove()
        r4.vel_display_behav = DontDisplayVel()
        r4.body_display_behav = DisplayRect(self.screen, r4)
        
        self.bodies.append(b1)
        self.bodies.append(r1)
        self.bodies.append(r2)
        self.bodies.append(r3)
        self.bodies.append(r4)

        # CRIAR OBJETO ITERADOR
        self.body_iter = BodyIterator(self.bodies)

        self.running = True
        self.start_main_loop()

        pg.quit()

    def start_main_loop(self):
        while self.running:
            self.time_handler.ticks = pg.time.get_ticks()

            self.screen.fill((0, 0, 0))

            self.handle_events()
            self.loop_bodies()
            
            # pg.draw.line(self.screen, line_color, (60, 80), (130, 100))
            pg.display.flip()

            self.time_handler.wait()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == KEYDOWN:

                if event.key == K_BACKSPACE:
                    self.running = False

            # Check for QUIT event
            elif event.type == QUIT:
                self.running = False

    def loop_bodies(self):
        # Itera uma vez sobre cada corpo para mostrá-los e movê-los
        for b in self.bodies:
            b.move(self.time_handler.rDT)
            b.display((255, 0, 0))
            b.display_vel((0, 255, 0))

        # Itera uma segunda vez sobre cada combinação de par
        # entre corpos para verificar colisões
        self.body_iter.first()
        while self.body_iter.has_next():
            b1, b2 = self.body_iter.next()

            if type(b1) is CircleBody   and type(b2) is CircleBody:
                CollisionLogic.circle_circle_collision(b1, b2)
            elif type(b1) is CircleBody and type(b2) is RectBody:
                CollisionLogic.circle_rect_collision(b1, b2)
            elif type(b1) is RectBody   and type(b2) is CircleBody:
                CollisionLogic.circle_rect_collision(b2, b1)
            elif type(b1) is RectBody   and type(b2) is RectBody:
                pass