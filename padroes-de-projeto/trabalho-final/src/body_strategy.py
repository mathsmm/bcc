from abc import ABC, abstractmethod
import pygame
from pygame.locals import *
from pygame import Surface
from src.vec2 import Vec2
from src.body import Body

PI_DIV_180 = 0.01745329251994329576923690768489
PI_MINUS_PI_DIV_6 = 2.6179938779914943653855361527329
PI_PLUS_PI_DIV_6 = 3.6651914291880921115397506138261

class MovementBehav(ABC):
    @abstractmethod
    def move(self, rDT):
        pass

class DoMove(MovementBehav):
    def __init__(self, b: Body) -> None:
        self.b = b
    def move(self, rDT):
        # Accelerate then move
        self.b.vel = self.b.vel + (self.b.acc * rDT)
        self.b.pos = self.b.pos + (self.b.vel * rDT)

class DontMove(MovementBehav):
    def __init__(self) -> None:
        pass
    def move(self, rDT):
        pass

class VelDisplayBehav(ABC):
    @abstractmethod
    def display(self, color: tuple):
        pass

class DoDisplayVel(VelDisplayBehav):
    def __init__(self, surface: Surface, b: Body) -> None:
        self.srfc = surface
        self.b = b

    def display(self, color: tuple):
        arrow_mod = self.b.vel.module() * 0.10
        if arrow_mod < 0.01:
            return

        l_arrow_segment = (self.b.vel.unit() * arrow_mod)
        l_arrow_segment.rotate(PI_MINUS_PI_DIV_6)
        r_arrow_segment = (self.b.vel.unit() * arrow_mod)
        r_arrow_segment.rotate(PI_PLUS_PI_DIV_6)

        pygame.draw.line(
            self.srfc, color, 
            (self.b.pos.x, self.b.pos.y), 
            (self.b.pos.x + self.b.vel.x, self.b.pos.y + self.b.vel.y)
        )
        arrow_initial_pos = self.b.pos + self.b.vel
        pygame.draw.line(
            self.srfc, color, 
            (arrow_initial_pos.x, arrow_initial_pos.y),
            (arrow_initial_pos.x + l_arrow_segment.x, arrow_initial_pos.y + l_arrow_segment.y)
        )
        pygame.draw.line(
            self.srfc, color, 
            (arrow_initial_pos.x, arrow_initial_pos.y), 
            (arrow_initial_pos.x + r_arrow_segment.x, arrow_initial_pos.y + r_arrow_segment.y)
        )
        
class DontDisplayVel(VelDisplayBehav):
    def __init__(self) -> None:
        pass

    def display(self, color: tuple):
        pass 

class BodyDisplayBehav(ABC):
    @abstractmethod
    def display(self, color: tuple):
        pass

class DisplayRect(BodyDisplayBehav):
    def __init__(self, surface: Surface, b: Body) -> None:
        self.srfc = surface
        self.b = b

    def display(self, color: tuple):
        pygame.draw.line(
            self.srfc, color, 
            (self.b.pos.x, self.b.pos.y), 
            (self.b.pos.x + self.b.width, self.b.pos.y)
        )
        pygame.draw.line(
            self.srfc, color, 
            (self.b.pos.x, self.b.pos.y), 
            (self.b.pos.x, self.b.pos.y + self.b.height)
        )
        pygame.draw.line(
            self.srfc, color, 
            (self.b.pos.x + self.b.width, self.b.pos.y), 
            (self.b.pos.x + self.b.width, self.b.pos.y + self.b.height)
        )
        pygame.draw.line(
            self.srfc, color, 
            (self.b.pos.x, self.b.pos.y + self.b.height), 
            (self.b.pos.x + self.b.width, self.b.pos.y + self.b.height)
        )

class DisplayCircle(BodyDisplayBehav):
    def __init__(self, surface: Surface, b: Body) -> None:
        self.srfc = surface
        self.b = b

    def display(self, color: tuple):
        circle_vertex_qty = 24
        rad_inc = (360.0 / circle_vertex_qty) * PI_DIV_180
        v1 = Vec2(self.b.radius, 0.0)
        v2 = Vec2(self.b.radius, 0.0)
        v2.rotate(rad_inc)
        for i in range(0, circle_vertex_qty):
            pos_plus_v1 = self.b.pos + v1
            pos_plus_v2 = self.b.pos + v2
            pygame.draw.line(
                self.srfc, color, 
                (pos_plus_v1.x, pos_plus_v1.y), 
                (pos_plus_v2.x, pos_plus_v2.y)
            )
            v1.rotate(rad_inc)
            v2.rotate(rad_inc)

# class CollisionBehav(ABC):
#     @abstractmethod
#     def collide(self):
#         pass

# class CollisionDetectionBehav(ABC):
#     @abstractmethod
#     def is_colliding(self):
#         pass