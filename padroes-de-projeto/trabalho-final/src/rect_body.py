from src.body import Body
from src.vec2 import Vec2

class RectBody(Body):
    def __init__(
        self, 
        init_pos: Vec2, 
        init_vel: Vec2, 
        init_accel: Vec2, 
        mass: float,
        height: float,
        width: float
    ) -> None:
        super().__init__(init_pos, init_vel, init_accel, mass)
        self.height = height
        self.width = width