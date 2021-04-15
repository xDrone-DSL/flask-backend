from math import sin, cos, radians
from typing import List

from xdrone import Command
from xdrone.visitors.safety_checker_utils.drone_config import DroneConfig
from xdrone.visitors.safety_checker_utils.safety_boundary import SafetyBoundary
from xdrone.visitors.safety_checker_utils.safety_check_error import SafetyCheckError
from xdrone.visitors.safety_checker_utils.status import Status


class SafetyChecker:
    def __init__(self):
        self.OPCODE_METHOD_MAP = {
            "takeoff": self.__check_takeoff,
            "land": self.__check_land,
            "up": self.__check_up,
            "down": self.__check_down,
            "left": self.__check_left,
            "right": self.__check_right,
            "forward": self.__check_forward,
            "backward": self.__check_backward,
            "rotate_left": self.__check_rotate_left,
            "rotate_right": self.__check_rotate_right,
            "wait": self.__check_wait
        }

    def check(self, commands: List[Command], drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        status = Status(has_taken_off=False)
        for command in commands:
            check_method = self.OPCODE_METHOD_MAP[command.opcode]
            check_method(command, status, drone_config, safety_boundary)
        if status.has_taken_off:
            raise SafetyCheckError("The drone did not land in the end")

    @staticmethod
    def __check_takeoff(command: Command, status: Status, drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        assert command.opcode == "takeoff"
        if status.has_taken_off:
            raise SafetyCheckError("Takeoff command used when the drone has already been taken off")
        status.has_taken_off = True
        status.time_used_seconds += drone_config.takeoff_height_meters / drone_config.speed_mps
        status.z_meters = drone_config.takeoff_height_meters
        safety_boundary.check_status(status)

    @staticmethod
    def __check_land(command: Command, status: Status, drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        assert command.opcode == "land"
        if not status.has_taken_off:
            raise SafetyCheckError("Land command used when the drone has not been taken off")
        status.has_taken_off = False
        status.time_used_seconds += status.z_meters / drone_config.speed_mps
        status.z_meters = 0
        safety_boundary.check_status(status)

    @staticmethod
    def __check_up(command: Command, status: Status, drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        assert command.opcode == "up"
        if not status.has_taken_off:
            raise SafetyCheckError("Up command used when the drone has not been taken off")
        up_meters, = command.operands
        status.time_used_seconds += up_meters / drone_config.speed_mps
        status.z_meters += up_meters
        safety_boundary.check_status(status)

    @staticmethod
    def __check_down(command: Command, status: Status, drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        assert command.opcode == "down"
        if not status.has_taken_off:
            raise SafetyCheckError("Down command used when the drone has not been taken off")
        down_meters, = command.operands
        status.time_used_seconds += down_meters / drone_config.speed_mps
        status.z_meters -= down_meters
        safety_boundary.check_status(status)

    @staticmethod
    def __check_left(command: Command, status: Status, drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        assert command.opcode == "left"
        if not status.has_taken_off:
            raise SafetyCheckError("Left command used when the drone has not been taken off")
        left_meters, = command.operands
        move_direction = status.orientation_degrees - 90
        status.time_used_seconds += left_meters / drone_config.speed_mps
        status.x_meters += left_meters * sin(radians(move_direction))
        status.y_meters += left_meters * cos(radians(move_direction))
        safety_boundary.check_status(status)

    @staticmethod
    def __check_right(command: Command, status: Status, drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        assert command.opcode == "right"
        if not status.has_taken_off:
            raise SafetyCheckError("Right command used when the drone has not been taken off")
        right_meters, = command.operands
        move_direction = status.orientation_degrees + 90
        status.time_used_seconds += right_meters / drone_config.speed_mps
        status.x_meters += right_meters * sin(radians(move_direction))
        status.y_meters += right_meters * cos(radians(move_direction))
        safety_boundary.check_status(status)

    @staticmethod
    def __check_forward(command: Command, status: Status, drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        assert command.opcode == "forward"
        if not status.has_taken_off:
            raise SafetyCheckError("Forward command used when the drone has not been taken off")
        forward_meters, = command.operands
        move_direction = status.orientation_degrees
        status.time_used_seconds += forward_meters / drone_config.speed_mps
        status.x_meters += forward_meters * sin(radians(move_direction))
        status.y_meters += forward_meters * cos(radians(move_direction))
        safety_boundary.check_status(status)

    @staticmethod
    def __check_backward(command: Command, status: Status, drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        assert command.opcode == "backward"
        if not status.has_taken_off:
            raise SafetyCheckError("Backward command used when the drone has not been taken off")
        backward_meters, = command.operands
        move_direction = status.orientation_degrees + 180
        status.time_used_seconds += backward_meters / drone_config.speed_mps
        status.x_meters += backward_meters * sin(radians(move_direction))
        status.y_meters += backward_meters * cos(radians(move_direction))
        safety_boundary.check_status(status)

    @staticmethod
    def __check_rotate_left(command: Command, status: Status, drone_config: DroneConfig,
                            safety_boundary: SafetyBoundary):
        assert command.opcode == "rotate_left"
        if not status.has_taken_off:
            raise SafetyCheckError("Rotate_left command used when the drone has not been taken off")
        rotate_left_degrees, = command.operands
        status.time_used_seconds += rotate_left_degrees / drone_config.rotate_speed_dps
        status.orientation_degrees = (status.orientation_degrees - rotate_left_degrees) % 360
        safety_boundary.check_status(status)

    @staticmethod
    def __check_rotate_right(command: Command, status: Status, drone_config: DroneConfig,
                             safety_boundary: SafetyBoundary):
        assert command.opcode == "rotate_right"
        if not status.has_taken_off:
            raise SafetyCheckError("Rotate_right command used when the drone has not been taken off")
        rotate_right_degrees, = command.operands
        status.time_used_seconds += rotate_right_degrees / drone_config.rotate_speed_dps
        status.orientation_degrees = (status.orientation_degrees + rotate_right_degrees) % 360
        safety_boundary.check_status(status)

    @staticmethod
    def __check_wait(command: Command, status: Status, drone_config: DroneConfig, safety_boundary: SafetyBoundary):
        assert command.opcode == "wait"
        wait_seconds, = command.operands
        status.time_used_seconds += wait_seconds
        safety_boundary.check_status(status)
