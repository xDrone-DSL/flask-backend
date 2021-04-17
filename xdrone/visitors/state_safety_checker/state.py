from __future__ import annotations

import copy
from math import isclose


class State:
    def __init__(self, has_taken_off: bool = False, time_used_seconds: float = 0,
                 x_meters: float = 0, y_meters: float = 0, z_meters: float = 0, orientation_degrees: float = 0):
        self._has_taken_off = has_taken_off
        self._time_used_seconds = time_used_seconds
        self._x_meters = x_meters
        self._y_meters = y_meters
        self._z_meters = z_meters
        self._orientation_degrees = orientation_degrees

    @staticmethod
    def init_state() -> State:
        return State(has_taken_off=False, time_used_seconds=0,
                     x_meters=0, y_meters=0, z_meters=0, orientation_degrees=0)

    @property
    def has_taken_off(self) -> bool:
        return copy.deepcopy(self._has_taken_off)

    @property
    def time_used_seconds(self) -> float:
        return copy.deepcopy(self._time_used_seconds)

    @property
    def x_meters(self) -> float:
        return copy.deepcopy(self._x_meters)

    @property
    def y_meters(self) -> float:
        return copy.deepcopy(self._y_meters)

    @property
    def z_meters(self) -> float:
        return copy.deepcopy(self._z_meters)

    @property
    def orientation_degrees(self) -> float:
        return copy.deepcopy(self._orientation_degrees)

    def copy_and_set_has_taken_off(self, has_taken_off: bool) -> State:
        return State(has_taken_off=has_taken_off, time_used_seconds=self.time_used_seconds,
                     x_meters=self.x_meters, y_meters=self.y_meters, z_meters=self.z_meters,
                     orientation_degrees=self.orientation_degrees)

    def copy_and_set_time_used_seconds(self, time_used_seconds: float) -> State:
        return State(has_taken_off=self.has_taken_off, time_used_seconds=time_used_seconds,
                     x_meters=self.x_meters, y_meters=self.y_meters, z_meters=self.z_meters,
                     orientation_degrees=self.orientation_degrees)

    def copy_and_set_x_meters(self, x_meters: float) -> State:
        return State(has_taken_off=self.has_taken_off, time_used_seconds=self.time_used_seconds,
                     x_meters=x_meters, y_meters=self.y_meters, z_meters=self.z_meters,
                     orientation_degrees=self.orientation_degrees)

    def copy_and_set_y_meters(self, y_meters: float) -> State:
        return State(has_taken_off=self.has_taken_off, time_used_seconds=self.time_used_seconds,
                     x_meters=self.x_meters, y_meters=y_meters, z_meters=self.z_meters,
                     orientation_degrees=self.orientation_degrees)

    def copy_and_set_z_meters(self, z_meters: float) -> State:
        return State(has_taken_off=self.has_taken_off, time_used_seconds=self.time_used_seconds,
                     x_meters=self.x_meters, y_meters=self.y_meters, z_meters=z_meters,
                     orientation_degrees=self.orientation_degrees)

    def copy_and_set_orientation_degrees(self, orientation_degrees: float) -> State:
        return State(has_taken_off=self.has_taken_off, time_used_seconds=self.time_used_seconds,
                     x_meters=self.x_meters, y_meters=self.y_meters, z_meters=self.z_meters,
                     orientation_degrees=orientation_degrees)

    def __str__(self):
        return ("State: {{ has_taken_off: {}, time_used_seconds: {}, "
                .format(self.has_taken_off, self.time_used_seconds) +
                "x_meters: {}, y_meters: {}, z_meters: {}, orientation_degrees: {} }}"
                .format(self.x_meters, self.y_meters, self.z_meters, self.orientation_degrees))

    def __eq__(self, other):
        if isinstance(other, State):
            return other.has_taken_off == self.has_taken_off \
                   and isclose(other.time_used_seconds, self.time_used_seconds) \
                   and isclose(other.x_meters, self.x_meters) and isclose(other.y_meters, self.y_meters) \
                   and isclose(other.z_meters, self.z_meters) \
                   and isclose(other.orientation_degrees, self.orientation_degrees)
        return False
