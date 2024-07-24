from src.vec2 import Vec2
# from src.body_behavior import MovementBehav, VelDisplayBehav, BodyDisplayBehav

class Body:
    def __init__(
        self,
        init_pos: Vec2,
        init_vel: Vec2,
        init_accel: Vec2,
        mass: float
    ) -> None:
        self.pos: Vec2 = init_pos
        self.vel: Vec2 = init_vel
        self.acc: Vec2 = init_accel
        self.mass: float = mass
        self.move_behav = None
        self.vel_display_behav = None
        self.body_display_behav = None

    def move(self, rDT: float):
        self.move_behav.move(rDT)

    def display_vel(self, color: tuple):
        self.vel_display_behav.display(color)

    def display(self, color: tuple):
        self.body_display_behav.display(color)