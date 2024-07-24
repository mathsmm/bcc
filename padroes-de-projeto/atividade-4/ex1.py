from abc import ABC, abstractmethod

# INTERFACE
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# CONCRETAS
class NoCommand(Command):
    def execute(self):
        pass

class Light:
    def __init__(self, room: str) -> None: self.room = room
    def on(self):  print(f"{self.room} light is on")
    def off(self): print(f"{self.room} light is off")

class CeilingFan:
    def __init__(self, room: str) -> None: self.room = room
    def on(self):  print(f"{self.room} ceiling fan is on high")
    def off(self): print(f"{self.room} ceiling fan is off")

class GarageDoor:
    def __init__(self, room: str) -> None: self.room = room
    def open(self):  print(f"{self.room} garage door is open")
    def close(self): print(f"{self.room} garage door is close")

class Stereo:
    def __init__(self, room: str) -> None: self.room = room
    def on(self):  
        print(f"{self.room} stereo is on")
        print(f"{self.room} stereo is set for CD input")
        print(f"{self.room} stereo volume set to 11")
    def off(self): print(f"{self.room} stereo is off")

class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self):
        self.light.off()

class CeilingFanOnCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan: CeilingFan = ceiling_fan

    def execute(self):
        self.ceiling_fan.on()

class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan: CeilingFan = ceiling_fan

    def execute(self):
        self.ceiling_fan.off()

class GarageDoorOnCommand(Command):
    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door: GarageDoor = garage_door

    def execute(self):
        self.garage_door.open()

class GarageDoorOffCommand(Command):
    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door: GarageDoor = garage_door

    def execute(self):
        self.garage_door.close()

class StereoOnCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self.stereo: Stereo = stereo

    def execute(self):
        self.stereo.on()

class StereoOffCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self.stereo: Stereo = stereo

    def execute(self):
        self.stereo.off()

class RemoteControl:
    def __init__(self) -> None:
        self.on_commands = [None] * 7
        self.off_commands = [None] * 7
        for i in range(len(self.on_commands)):
            self.on_commands[i] = NoCommand()
        for i in range(len(self.off_commands)):
            self.off_commands[i] = NoCommand()

    def set_command(
        self, 
        slot: int, 
        on_comm: Command,
        off_comm: Command
    ) -> None:
        self.on_commands[slot] = on_comm
        self.off_commands[slot] = off_comm

    def on_btn_was_pushed(self, slot: int):
        self.on_commands[slot].execute()

    def off_btn_was_pushed(self, slot: int):
        self.off_commands[slot].execute()

    def __str__(self) -> str:
        s = ""
        for i in range(len(self.on_commands)):
            s += f"[slot {i}] {type(self.on_commands[i]).__name__} - {type(self.off_commands[i]).__name__}\n"
        return s

class RemoteLoader:
    def __init__(self) -> None:
        self.remote_control = None

    def main(self):
        light_living_room = Light("Living Room")
        light_kitchen = Light("Kitchen")
        ceiling_fan = CeilingFan("Living Room")
        garage_door = GarageDoor("Garage")
        stereo = Stereo("Living Room")

        c1_on  = LightOnCommand(light_living_room)
        c1_off = LightOffCommand(light_living_room)
        c2_on  = LightOnCommand(light_kitchen)
        c2_off = LightOffCommand(light_kitchen)
        c3_on  = CeilingFanOnCommand(ceiling_fan)
        c3_off = CeilingFanOffCommand(ceiling_fan)
        c4_on  = GarageDoorOnCommand(garage_door)
        c4_off = GarageDoorOffCommand(garage_door)
        c5_on  = StereoOnCommand(stereo)
        c5_off = StereoOffCommand(stereo)

        self.remote_control = RemoteControl()
        self.remote_control.set_command(0, c1_on, c1_off)
        self.remote_control.set_command(1, c2_on, c2_off)
        self.remote_control.set_command(2, c3_on, c3_off)
        self.remote_control.set_command(3, c4_on, c4_off)
        self.remote_control.set_command(4, c5_on, c5_off)

rl = RemoteLoader()
rl.main()

print(rl.remote_control, end="\n")

rl.remote_control.on_btn_was_pushed(0)
rl.remote_control.off_btn_was_pushed(0)
rl.remote_control.on_btn_was_pushed(1)
rl.remote_control.off_btn_was_pushed(1)
rl.remote_control.on_btn_was_pushed(2)
rl.remote_control.off_btn_was_pushed(2)
rl.remote_control.on_btn_was_pushed(4)
rl.remote_control.off_btn_was_pushed(4)