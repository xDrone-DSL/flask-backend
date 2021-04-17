from typing import List

from xdrone import Command
from xdrone.visitors.state_safety_checker.safety_check_error import SafetyCheckError
from xdrone.visitors.state_safety_checker.safety_config import SafetyConfig
from xdrone.visitors.state_safety_checker.state import State


class SafetyChecker:
    def __init__(self, safety_config: SafetyConfig):
        self.safety_config = safety_config
        self.OPCODE_METHOD_MAP = {
            "takeoff": self._check_takeoff,
            "land": self._check_land,
            "up": self._check_up,
            "down": self._check_down,
            "left": self._check_left,
            "right": self._check_right,
            "forward": self._check_forward,
            "backward": self._check_backward,
            "rotate_left": self._check_rotate_left,
            "rotate_right": self._check_rotate_right,
            "wait": self._check_wait
        }

    def check(self, commands: List[Command], states: List[State]):
        assert len(commands) + 1 == len(states)
        for i, command in enumerate(commands):
            state_before = states[i]
            state_after = states[i + 1]
            check_method = self.OPCODE_METHOD_MAP[command.opcode]
            check_method(command, state_before, state_after)
        if states[-1].has_taken_off:
            raise SafetyCheckError("The drone did not land in the end")

    def _check_takeoff(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "takeoff"
        if state_before.has_taken_off:
            raise SafetyCheckError("'takeoff' command used when the drone has already been taken off")
        self.safety_config.check_state(state_after)

    def _check_land(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "land"
        if not state_before.has_taken_off:
            raise SafetyCheckError("'land' command used when the drone has not been taken off")
        self.safety_config.check_state(state_after)

    def _check_up(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "up"
        if not state_before.has_taken_off:
            raise SafetyCheckError("'up' command used when the drone has not been taken off")
        self.safety_config.check_state(state_after)

    def _check_down(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "down"
        if not state_before.has_taken_off:
            raise SafetyCheckError("'down' command used when the drone has not been taken off")
        self.safety_config.check_state(state_after)

    def _check_left(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "left"
        if not state_before.has_taken_off:
            raise SafetyCheckError("'left' command used when the drone has not been taken off")
        self.safety_config.check_state(state_after)

    def _check_right(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "right"
        if not state_before.has_taken_off:
            raise SafetyCheckError("'right' command used when the drone has not been taken off")
        self.safety_config.check_state(state_after)

    def _check_forward(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "forward"
        if not state_before.has_taken_off:
            raise SafetyCheckError("'forward' command used when the drone has not been taken off")
        self.safety_config.check_state(state_after)

    def _check_backward(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "backward"
        if not state_before.has_taken_off:
            raise SafetyCheckError("'backward' command used when the drone has not been taken off")
        self.safety_config.check_state(state_after)

    def _check_rotate_left(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "rotate_left"
        if not state_before.has_taken_off:
            raise SafetyCheckError("'rotate_left' command used when the drone has not been taken off")
        self.safety_config.check_state(state_after)

    def _check_rotate_right(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "rotate_right"
        if not state_before.has_taken_off:
            raise SafetyCheckError("'rotate_right' command used when the drone has not been taken off")
        self.safety_config.check_state(state_after)

    def _check_wait(self, command: Command, state_before: State, state_after: State):
        assert command.opcode == "wait"
        self.safety_config.check_state(state_after)
