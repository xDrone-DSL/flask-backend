from math import sin, cos, radians

from xdrone import Command
from xdrone.visitors.state_safety_checker.drone_config import DroneConfig
from xdrone.visitors.state_safety_checker.state import State


class StateUpdater:
    def __init__(self, drone_config: DroneConfig):
        self.drone_config = drone_config
        self.OPCODE_METHOD_MAP = {
            "takeoff": self._update_takeoff,
            "land": self._update_land,
            "up": self._update_up,
            "down": self._update_down,
            "left": self._update_left,
            "right": self._update_right,
            "forward": self._update_forward,
            "backward": self._update_backward,
            "rotate_left": self._update_rotate_left,
            "rotate_right": self._update_rotate_right,
            "wait": self._update_wait
        }

    def update(self, command: Command, state: State) -> State:
        update_method = self.OPCODE_METHOD_MAP[command.opcode]
        return update_method(command, state)

    def _update_takeoff(self, command: Command, state: State) -> State:
        assert command.opcode == "takeoff"
        state = state.copy_and_set_has_taken_off(True)
        state = state.copy_and_set_time_used_seconds(
            state.time_used_seconds + self.drone_config.takeoff_height_meters / self.drone_config.speed_mps)
        state = state.copy_and_set_z_meters(self.drone_config.takeoff_height_meters)
        return state

    def _update_land(self, command: Command, state: State) -> State:
        assert command.opcode == "land"
        state = state.copy_and_set_has_taken_off(False)
        state = state.copy_and_set_time_used_seconds(
            state.time_used_seconds + state.z_meters / self.drone_config.speed_mps)
        state = state.copy_and_set_z_meters(0)
        return state

    def _update_up(self, command: Command, state: State) -> State:
        assert command.opcode == "up"
        up_meters, = command.operands
        state = state.copy_and_set_time_used_seconds(state.time_used_seconds + up_meters / self.drone_config.speed_mps)
        state = state.copy_and_set_z_meters(state.z_meters + up_meters)
        return state

    def _update_down(self, command: Command, state: State) -> State:
        assert command.opcode == "down"
        down_meters, = command.operands
        state = state.copy_and_set_time_used_seconds(
            state.time_used_seconds + down_meters / self.drone_config.speed_mps)
        state = state.copy_and_set_z_meters(state.z_meters - down_meters)
        return state

    def _update_left(self, command: Command, state: State) -> State:
        assert command.opcode == "left"
        left_meters, = command.operands
        move_direction = state.orientation_degrees - 90
        state = state.copy_and_set_time_used_seconds(
            state.time_used_seconds + left_meters / self.drone_config.speed_mps)
        state = state.copy_and_set_x_meters(state.x_meters + left_meters * sin(radians(move_direction)))
        state = state.copy_and_set_y_meters(state.y_meters + left_meters * cos(radians(move_direction)))
        return state

    def _update_right(self, command: Command, state: State) -> State:
        assert command.opcode == "right"
        right_meters, = command.operands
        move_direction = state.orientation_degrees + 90
        state = state.copy_and_set_time_used_seconds(
            state.time_used_seconds + right_meters / self.drone_config.speed_mps)
        state = state.copy_and_set_x_meters(state.x_meters + right_meters * sin(radians(move_direction)))
        state = state.copy_and_set_y_meters(state.y_meters + right_meters * cos(radians(move_direction)))
        return state

    def _update_forward(self, command: Command, state: State) -> State:
        assert command.opcode == "forward"
        forward_meters, = command.operands
        move_direction = state.orientation_degrees
        state = state.copy_and_set_time_used_seconds(
            state.time_used_seconds + forward_meters / self.drone_config.speed_mps)
        state = state.copy_and_set_x_meters(state.x_meters + forward_meters * sin(radians(move_direction)))
        state = state.copy_and_set_y_meters(state.y_meters + forward_meters * cos(radians(move_direction)))
        return state

    def _update_backward(self, command: Command, state: State) -> State:
        assert command.opcode == "backward"
        backward_meters, = command.operands
        move_direction = state.orientation_degrees + 180
        state = state.copy_and_set_time_used_seconds(
            state.time_used_seconds + backward_meters / self.drone_config.speed_mps)
        state = state.copy_and_set_x_meters(state.x_meters + backward_meters * sin(radians(move_direction)))
        state = state.copy_and_set_y_meters(state.y_meters + backward_meters * cos(radians(move_direction)))
        return state

    def _update_rotate_left(self, command: Command, state: State) -> State:
        assert command.opcode == "rotate_left"
        rotate_left_degrees, = command.operands
        state = state.copy_and_set_time_used_seconds(
            state.time_used_seconds + rotate_left_degrees / self.drone_config.rotate_speed_dps)
        state = state.copy_and_set_orientation_degrees((state.orientation_degrees - rotate_left_degrees) % 360)
        return state

    def _update_rotate_right(self, command: Command, state: State) -> State:
        assert command.opcode == "rotate_right"
        rotate_right_degrees, = command.operands
        state = state.copy_and_set_time_used_seconds(
            state.time_used_seconds + rotate_right_degrees / self.drone_config.rotate_speed_dps)
        state = state.copy_and_set_orientation_degrees((state.orientation_degrees + rotate_right_degrees) % 360)
        return state

    def _update_wait(self, command: Command, state: State) -> State:
        assert command.opcode == "wait"
        wait_seconds, = command.operands
        state = state.copy_and_set_time_used_seconds(state.time_used_seconds + wait_seconds)
        return state
