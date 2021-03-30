import copy
from typing import Union


class Command:
    def __init__(self, opcode: str, operands: list):
        self._opcode = opcode
        self._operands = operands

    @property
    def opcode(self):
        return copy.deepcopy(self._opcode)

    @property
    def operands(self):
        return copy.deepcopy(self._operands)

    def to_simulation_json(self):
        return {"action": self._opcode, "value": self._operands}

class Takeoff(Command):
    def __init__(self):
        super().__init__("takeoff", [])

class Land(Command):
    def __init__(self):
        super().__init__("land", [])

class Up(Command):
    def __init__(self, distance: Union[int, float]):
        super().__init__("up", [distance])

class Down(Command):
    def __init__(self, distance: Union[int, float]):
        super().__init__("down", [distance])

class Left(Command):
    def __init__(self, distance: Union[int, float]):
        super().__init__("left", [distance])

class Right(Command):
    def __init__(self, distance: Union[int, float]):
        super().__init__("right", [distance])

class Forward(Command):
    def __init__(self, distance: Union[int, float]):
        super().__init__("forward", [distance])

class Backward(Command):
    def __init__(self, distance: Union[int, float]):
        super().__init__("backward", [distance])

class RotateLeft(Command):
    def __init__(self, angle: Union[int, float]):
        super().__init__("rotateL", [angle])

class RotateRight(Command):
    def __init__(self, angle: Union[int, float]):
        super().__init__("rotateR", [angle])

class Wait(Command):
    def __init__(self, time: Union[int, float]):
        super().__init__("wait", [time])

