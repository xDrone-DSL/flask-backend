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
    def up(distance_meters: Union[int, float]) -> Command:
        return Command("up", [distance_meters])

    @staticmethod
    def down(distance_meters: Union[int, float]) -> Command:
        return Command("down", [distance_meters])

    @staticmethod
    def left(distance_meters: Union[int, float]) -> Command:
        return Command("left", [distance_meters])

    @staticmethod
    def right(distance_meters: Union[int, float]) -> Command:
        return Command("right", [distance_meters])

    @staticmethod
    def forward(distance_meters: Union[int, float]) -> Command:
        return Command("forward", [distance_meters])

    @staticmethod
    def backward(distance_meters: Union[int, float]) -> Command:
        return Command("backward", [distance_meters])

    @staticmethod
    def rotate_left(angle_degrees: Union[int, float]) -> Command:
        return Command("rotate_left", [angle_degrees])

    @staticmethod
    def rotate_right(angle_degrees: Union[int, float]) -> Command:
        return Command("rotate_right", [angle_degrees])

    @staticmethod
    def wait(time_seconds: Union[int, float]) -> Command:
        return Command("wait", [time_seconds])

    def to_simulation_json(self) -> dict:
        return {"action": self._opcode, "value": self._operands}

    def __str__(self):
        return "Command: {{ opcode: {}, operands: {} }}".format(self._opcode, self._operands)

    def __eq__(self, other):
        if isinstance(other, Command):
            return other._opcode == self._opcode and other._operands == self._operands
        return False
