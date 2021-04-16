import unittest
from math import sqrt

from xdrone import DroneConfig, SafetyConfig, SafetyChecker, Command
from xdrone.visitors.safety_checker_utils.safety_check_error import SafetyCheckError
from xdrone.visitors.safety_checker_utils.status import Status


class SafetyCheckerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.drone_config = DroneConfig(speed_mps=0.5, rotate_speed_dps=45, takeoff_height_meters=1)
        self.safety_config = SafetyConfig(max_seconds=10, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                          min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)

    def test_check_in_the_end_not_land_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.takeoff()], self.drone_config, self.safety_config)
        self.assertTrue("The drone did not land in the end" in str(context.exception))

    def test_check_takeoff_land_takeoff_land_should_not_give_error(self):
        SafetyChecker().check([Command.takeoff(), Command.land(), Command.takeoff(), Command.land()],
                              self.drone_config, self.safety_config)

    def test_check_takeoff_should_update_status(self):
        status = Status.init_state()
        SafetyChecker._check_takeoff(Command.takeoff(), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=self.drone_config.takeoff_height_meters / 0.5,
                          z_meters=self.drone_config.takeoff_height_meters)
        self.assertEqual(expected, status)

    def test_check_takeoff_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status.init_state()
            safety_config = SafetyConfig(max_seconds=0, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_takeoff(Command.takeoff(), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 0 seconds"
                        .format(self.drone_config.takeoff_height_meters / 0.5)
                        in str(context.exception))

    def test_check_takeoff_when_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.takeoff(), Command.takeoff()], self.drone_config, self.safety_config)
        self.assertTrue("'takeoff' command used when the drone has already been taken off" in str(context.exception))

    def test_check_land_should_update_status(self):
        status = Status(has_taken_off=True, z_meters=3)
        SafetyChecker()._check_land(Command.land(), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=False, time_used_seconds=3 / 0.5, z_meters=0)
        self.assertEqual(expected, status)

    def test_check_land_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_land(Command.land(), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 3 / 0.5)
                        in str(context.exception))

    def test_check_land_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.land()], self.drone_config, self.safety_config)
        self.assertTrue("'land' command used when the drone has not been taken off" in str(context.exception))

    def test_check_up_should_update_status(self):
        status = Status(has_taken_off=True, z_meters=3)
        SafetyChecker()._check_up(Command.up(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, z_meters=3 + 1)
        self.assertEqual(expected, status)

    def test_check_up_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_up(Command.up(2), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 2 / 0.5)
                        in str(context.exception))

    def test_check_up_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.up(1)], self.drone_config, self.safety_config)
        self.assertTrue("'up' command used when the drone has not been taken off" in str(context.exception))

    def test_check_down_should_update_status(self):
        status = Status(has_taken_off=True, z_meters=3)
        SafetyChecker()._check_down(Command.down(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, z_meters=3 - 1)
        self.assertEqual(expected, status)

    def test_check_down_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_down(Command.down(2), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 2 / 0.5)
                        in str(context.exception))

    def test_check_down_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.down(1)], self.drone_config, self.safety_config)
        self.assertTrue("'down' command used when the drone has not been taken off" in str(context.exception))

    def test_check_left_should_update_status(self):
        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        SafetyChecker()._check_left(Command.left(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 - 0.5, y_meters=2 + sqrt(3) / 2,
                          z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, status)

        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        SafetyChecker()._check_left(Command.left(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 + 0.5, y_meters=2 - sqrt(3) / 2,
                          z_meters=3, orientation_degrees=240)
        self.assertEqual(expected, status)

    def test_check_left_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_left(Command.left(2), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 2 / 0.5)
                        in str(context.exception))

    def test_check_left_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.left(1)], self.drone_config, self.safety_config)
        self.assertTrue("'left' command used when the drone has not been taken off" in str(context.exception))

    def test_check_right_should_update_status(self):
        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        SafetyChecker()._check_right(Command.right(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 + 0.5, y_meters=2 - sqrt(3) / 2,
                          z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, status)

        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        SafetyChecker()._check_right(Command.right(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 - 0.5, y_meters=2 + sqrt(3) / 2,
                          z_meters=3, orientation_degrees=240)
        self.assertEqual(expected, status)

    def test_check_right_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_right(Command.right(2), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 2 / 0.5)
                        in str(context.exception))

    def test_check_right_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.right(1)], self.drone_config, self.safety_config)
        self.assertTrue("'right' command used when the drone has not been taken off" in str(context.exception))

    def test_check_forward_should_update_status(self):
        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        SafetyChecker()._check_forward(Command.forward(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 + sqrt(3) / 2, y_meters=2 + 0.5,
                          z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, status)

        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        SafetyChecker()._check_forward(Command.forward(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 - sqrt(3) / 2, y_meters=2 - 0.5,
                          z_meters=3, orientation_degrees=240)
        self.assertEqual(expected, status)

    def test_check_forward_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_forward(Command.forward(2), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 2 / 0.5)
                        in str(context.exception))

    def test_check_forward_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.forward(1)], self.drone_config, self.safety_config)
        self.assertTrue("'forward' command used when the drone has not been taken off" in str(context.exception))

    def test_check_backward_should_update_status(self):
        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        SafetyChecker()._check_backward(Command.backward(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 - sqrt(3) / 2, y_meters=2 - 0.5,
                          z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, status)

        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        SafetyChecker()._check_backward(Command.backward(1), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1 + sqrt(3) / 2, y_meters=2 + 0.5,
                          z_meters=3, orientation_degrees=240)
        self.assertEqual(expected, status)

    def test_check_backward_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_backward(Command.backward(2), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 2 / 0.5)
                        in str(context.exception))

    def test_check_backward_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.backward(1)], self.drone_config, self.safety_config)
        self.assertTrue("'backward' command used when the drone has not been taken off" in str(context.exception))

    def test_check_rotate_left_should_update_status(self):
        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        SafetyChecker()._check_rotate_left(Command.rotate_left(90), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1, y_meters=2,
                          z_meters=3, orientation_degrees=330)
        self.assertEqual(expected, status)

        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        SafetyChecker()._check_rotate_left(Command.rotate_left(90), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1, y_meters=2,
                          z_meters=3, orientation_degrees=150)
        self.assertEqual(expected, status)

    def test_check_rotate_left_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_rotate_left(Command.rotate_left(90), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 90 / 45)
                        in str(context.exception))

    def test_check_rotate_left_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.rotate_left(90)], self.drone_config, self.safety_config)
        self.assertTrue("'rotate_left' command used when the drone has not been taken off" in str(context.exception))

    def test_check_rotate_right_should_update_status(self):
        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        SafetyChecker()._check_rotate_right(Command.rotate_right(90), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1, y_meters=2,
                          z_meters=3, orientation_degrees=150)
        self.assertEqual(expected, status)

        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=240)
        SafetyChecker()._check_rotate_right(Command.rotate_right(90), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=1 / 0.5, x_meters=1, y_meters=2,
                          z_meters=3, orientation_degrees=330)
        self.assertEqual(expected, status)

    def test_check_rotate_right_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_rotate_right(Command.rotate_right(90), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 90 / 45)
                        in str(context.exception))

    def test_check_rotate_right_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker().check([Command.rotate_right(90)], self.drone_config, self.safety_config)
        self.assertTrue("'rotate_right' command used when the drone has not been taken off" in str(context.exception))

    def test_check_wait_should_update_status(self):
        status = Status(has_taken_off=True, x_meters=1, y_meters=2, z_meters=3, orientation_degrees=60)
        SafetyChecker()._check_wait(Command.wait(5), status, self.drone_config, self.safety_config)
        expected = Status(has_taken_off=True, time_used_seconds=5, x_meters=1, y_meters=2,
                          z_meters=3, orientation_degrees=60)
        self.assertEqual(expected, status)

    def test_check_wait_should_check_status(self):
        with self.assertRaises(SafetyCheckError) as context:
            status = Status(has_taken_off=True, time_used_seconds=2, z_meters=3)
            safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                         min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)
            SafetyChecker._check_wait(Command.wait(2), status, self.drone_config, safety_config)
        self.assertTrue("The time used {} seconds will go beyond the time limit 3 seconds"
                        .format(2 + 2)
                        in str(context.exception))
