import unittest

from xdrone import SafetyConfig, SafetyChecker, Command
from xdrone.visitors.state_safety_checker.safety_check_error import SafetyCheckError
from xdrone.visitors.state_safety_checker.state import State


class SafetyCheckerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.safety_config = SafetyConfig(max_seconds=3, max_x_meters=5, max_y_meters=5, max_z_meters=5,
                                          min_x_meters=-5, min_y_meters=-5, min_z_meters=-5)

    def test_check_in_the_end_not_land_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.takeoff()], [State.init_state(),
                                                                          State(has_taken_off=True)])
        self.assertTrue("The drone did not land in the end" in str(context.exception))

    def test_check_takeoff_land_takeoff_land_should_not_give_error(self):
        SafetyChecker(self.safety_config).check([Command.takeoff(), Command.land(), Command.takeoff(), Command.land()],
                                                [State.init_state(),
                                                 State(has_taken_off=True), State(has_taken_off=False),
                                                 State(has_taken_off=True), State(has_taken_off=False)])

    def test_check_takeoff_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State.init_state()
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=3)
            SafetyChecker(self.safety_config)._check_takeoff(Command.takeoff(), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_takeoff_when_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.takeoff(), Command.takeoff()],
                                                    [State.init_state(), State(has_taken_off=True),
                                                     State(has_taken_off=True)])
        self.assertTrue("'takeoff' command used when the drone has already been taken off" in str(context.exception))

    def test_check_land_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=3)
            state_after = State(has_taken_off=True, time_used_seconds=4)
            SafetyChecker(self.safety_config)._check_land(Command.land(), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_land_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.land()],
                                                    [State.init_state(), State(has_taken_off=False)])
        self.assertTrue("'land' command used when the drone has not been taken off" in str(context.exception))

    def test_check_up_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=1)
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=3)
            SafetyChecker(self.safety_config)._check_up(Command.up(2), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_up_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.up(0)],
                                                    [State.init_state(), State(has_taken_off=False)])
        self.assertTrue("'up' command used when the drone has not been taken off" in str(context.exception))

    def test_check_down_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=3)
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=1)
            SafetyChecker(self.safety_config)._check_down(Command.down(2), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_down_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.down(0)],
                                                    [State.init_state(), State(has_taken_off=False)])
        self.assertTrue("'down' command used when the drone has not been taken off" in str(context.exception))

    def test_check_left_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=3)
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=3, x_meters=-2)
            SafetyChecker(self.safety_config)._check_left(Command.left(2), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_left_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.left(0)],
                                                    [State.init_state(), State(has_taken_off=False)])
        self.assertTrue("'left' command used when the drone has not been taken off" in str(context.exception))

    def test_check_right_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=3)
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=3, x_meters=2)
            SafetyChecker(self.safety_config)._check_right(Command.right(2), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_right_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.right(0)],
                                                    [State.init_state(), State(has_taken_off=False)])
        self.assertTrue("'right' command used when the drone has not been taken off" in str(context.exception))

    def test_check_forward_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=3)
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=3, y_meters=2)
            SafetyChecker(self.safety_config)._check_forward(Command.forward(2), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_forward_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.forward(0)],
                                                    [State.init_state(), State(has_taken_off=False)])
        self.assertTrue("'forward' command used when the drone has not been taken off" in str(context.exception))

    def test_check_backward_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=3)
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=3, y_meters=-2)
            SafetyChecker(self.safety_config)._check_backward(Command.backward(2), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_backward_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.backward(0)],
                                                    [State.init_state(), State(has_taken_off=False)])
        self.assertTrue("'backward' command used when the drone has not been taken off" in str(context.exception))

    def test_check_rotate_left_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=3)
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=3, orientation_degrees=270)
            SafetyChecker(self.safety_config)._check_rotate_left(Command.rotate_left(90), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_rotate_left_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.rotate_left(0)],
                                                    [State.init_state(), State(has_taken_off=False)])
        self.assertTrue("'rotate_left' command used when the drone has not been taken off" in str(context.exception))

    def test_check_rotate_right_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=3)
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=3, orientation_degrees=90)
            SafetyChecker(self.safety_config)._check_rotate_right(Command.rotate_right(90), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))

    def test_check_rotate_right_when_not_taken_off_should_give_error(self):
        with self.assertRaises(SafetyCheckError) as context:
            SafetyChecker(self.safety_config).check([Command.rotate_right(0)],
                                                    [State.init_state(), State(has_taken_off=False)])
        self.assertTrue("'rotate_right' command used when the drone has not been taken off" in str(context.exception))

    def test_check_wait_should_check_state(self):
        with self.assertRaises(SafetyCheckError) as context:
            state_before = State(has_taken_off=True, time_used_seconds=2, z_meters=3)
            state_after = State(has_taken_off=True, time_used_seconds=4, z_meters=3)
            SafetyChecker(self.safety_config)._check_wait(Command.wait(2), state_before, state_after)
        self.assertTrue("The time used 4 seconds will go beyond the time limit 3 seconds" in str(context.exception))
