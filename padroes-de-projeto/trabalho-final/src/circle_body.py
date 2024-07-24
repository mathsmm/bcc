from src.body import Body
from src.vec2 import Vec2

class CircleBody(Body):
    def __init__(
        self, 
        init_pos: Vec2, 
        init_vel: Vec2, 
        init_accel: Vec2, 
        mass: float,
        radius: float
    ) -> None:
        super().__init__(init_pos, init_vel, init_accel, mass)
        self.radius = radius