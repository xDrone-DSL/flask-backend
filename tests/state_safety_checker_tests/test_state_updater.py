import unittest
from math import sqrt

from xdrone import DroneConfig, StateUpdater, Command
from xdrone.visitors.state_safety_checker.state import State


class StateUpdaterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.drone_config = DroneConfig(speed_mps=0.5, rotate_speed_dps=45, takeoff_height_meters=1)
        self.state_updater = StateUpdater(drone_config=self.drone_config)

    def test_update_takeoff_should_update_state(self):
        state = State.init_state()
        actual = self.state_updater.update(Command.takeoff(), state)
        expected = State(has_taken_off=True, time_used_seconds=self.drone_config.takeoff_height_meters / 0.5,
                         z_meters=self.drone_config.takeoff_height_meters)
        self.assertEqual(expected, actual)

    def test_update_land_should_update_state(self):
        state = State(has_taken_off=True, z_meters=3)
        actual = self.state_updater.update(Command.land(), state)
        expected = State(has_taken_off=False, time_used_seconds=3 / 0.5, z_meters=0)
        self.assertEqual(expected, actual)

    def test_update_up_should_update_state(self):
        state = State(has_taken_off=True, z_meters=3)
        actual = self.state_updater.update(Command.up(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, z_meters=3 + 1)
        self.assertEqual(expected, actual)

    def test_update_down_should_update_state(self):
        state = State(has_taken_off=True, z_meters=3)
        actual = self.state_updater.update(Command.down(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, z_meters=3 - 1)
        self.assertEqual(expected, actual)

    def test_update_left_should_update_state(self):
        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        actual = self.state_updater.update(Command.left(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 - 0.5, y_meters=2 + sqrt(3) / 2,
                         z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, actual)

        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        actual = self.state_updater.update(Command.left(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 + 0.5, y_meters=2 - sqrt(3) / 2,
                         z_meters=3, orientation_degrees=240)
        self.assertEqual(expected, actual)

    def test_update_right_should_update_state(self):
        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        actual = self.state_updater.update(Command.right(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 + 0.5, y_meters=2 - sqrt(3) / 2,
                         z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, actual)

        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        actual = self.state_updater.update(Command.right(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 - 0.5, y_meters=2 + sqrt(3) / 2,
                         z_meters=3, orientation_degrees=240)
        self.assertEqual(expected, actual)

    def test_update_forward_should_update_state(self):
        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        actual = self.state_updater.update(Command.forward(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 + sqrt(3) / 2, y_meters=2 + 0.5,
                         z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, actual)

        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        actual = self.state_updater.update(Command.forward(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 - sqrt(3) / 2, y_meters=2 - 0.5,
                         z_meters=3, orientation_degrees=240)
        self.assertEqual(expected, actual)

    def test_update_backward_should_update_state(self):
        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        actual = self.state_updater.update(Command.backward(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 - sqrt(3) / 2, y_meters=2 - 0.5,
                         z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, actual)

        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        actual = self.state_updater.update(Command.backward(1), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 + sqrt(3) / 2, y_meters=2 + 0.5,
                         z_meters=3, orientation_degrees=240)
        self.assertEqual(expected, actual)

    def test_update_rotate_left_should_update_state(self):
        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        actual = self.state_updater.update(Command.rotate_left(90), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1, y_meters=2,
                         z_meters=3, orientation_degrees=330)
        self.assertEqual(expected, actual)

        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        actual = self.state_updater.update(Command.rotate_left(90), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1, y_meters=2,
                         z_meters=3, orientation_degrees=150)
        self.assertEqual(expected, actual)

    def test_update_rotate_right_should_update_state(self):
        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        actual = self.state_updater.update(Command.rotate_right(90), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1, y_meters=2,
                         z_meters=3, orientation_degrees=150)
        self.assertEqual(expected, actual)

        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        actual = self.state_updater.update(Command.rotate_right(90), state)
        expected = State(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1, y_meters=2,
                         z_meters=3, orientation_degrees=330)
        self.assertEqual(expected, actual)

    def test_update_wait_should_update_state(self):
        state = State(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        actual = self.state_updater.update(Command.wait(5), state)
        expected = State(has_taken_off=True, time_used_seconds=5, x_meters=1, y_meters=2,
                         z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, actual)
