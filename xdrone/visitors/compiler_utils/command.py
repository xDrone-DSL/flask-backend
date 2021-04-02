from __future__ import annotations

import copy
from typing import Union


class Command:
    def __init__(self, opcode: str, operands: list):
        self._opcode = opcode
        self._operands = operands

    @property
    def opcode(self) -> str:
        return copy.deepcopy(self._opcode)

    @property
    def operands(self) -> list:
        return copy.deepcopy(self._operands)

    @staticmethod
    def takeoff() -> Command:
        return Command("takeoff", [])

    @staticmethod
    def land() -> Command:
        return Command("land", [])

    @staticmethod
    def up(distance: Union[int, float]) -> Command:
        return Command("up", [distance])

    @staticmethod
    def down(distance: Union[int, float]) -> Command:
        return Command("down", [distance])

    @staticmethod
    def left(distance: Union[int, float]) -> Command:
        return Command("left", [distance])

    @staticmethod
    def right(distance: Union[int, float]) -> Command:
        return Command("right", [distance])

    @staticmethod
    def forward(distance: Union[int, float]) -> Command:
        return Command("forward", [distance])

    @staticmethod
    def backward(distance: Union[int, float]) -> Command:
        return Command("backward", [distance])

    @staticmethod
    def rotate_left(angle: Union[int, float]) -> Command:
        return Command("rotateL", [angle])

    @staticmethod
    def rotate_right(angle: Union[int, float]) -> Command:
        return Command("rotateR", [angle])

    @staticmethod
    def wait(time: Union[int, float]) -> Command:
        return Command("wait", [time])

    def to_simulation_json(self) -> dict:
        return {"action": self._opcode, "value": self._operands}

    def __str__(self):
        return "Command: {{ opcode: {}, operands: {} }}".format(self._opcode, self._operands)

    def __eq__(self, other):
        if isinstance(other, Command):
            return other._opcode == self._opcode and other._operands == self._operands
        return False
