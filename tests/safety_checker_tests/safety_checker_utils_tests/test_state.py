import unittest

from xdrone.visitors.safety_checker_utils.state import State


class StateTest(unittest.TestCase):
    def test_init_state(self):
        state = State.init_state()
        self.assertEqual(False, state.has_taken_off)
        self.assertEqual(0, state.time_used_seconds)
        self.assertEqual(0, state.x_meters)
        self.assertEqual(0, state.y_meters)
        self.assertEqual(0, state.z_meters)
        self.assertEqual(0, state.orientation_degrees)

    def test_set_values(self):
        state = State.init_state()
        state.has_taken_off = True
        state.time_used_seconds = 1
        state.x_meters = 1
        state.y_meters = 1
        state.z_meters = 1
        state.orientation_degrees = 1
        self.assertEqual(True, state.has_taken_off)
        self.assertEqual(1, state.time_used_seconds)
        self.assertEqual(1, state.x_meters)
        self.assertEqual(1, state.y_meters)
        self.assertEqual(1, state.z_meters)
        self.assertEqual(1, state.orientation_degrees)

    def test_str(self):
        state = State.init_state()
        self.assertEqual("State: { has_taken_off: False, time_used_seconds: 0, " +
                         "x_meters: 0, y_meters: 0, z_meters: 0, orientation_degrees: 0 }",
                         str(state))

    def test_eq(self):
        self.assertEqual(State.init_state(), State.init_state())
        self.assertNotEqual(State(time_used_seconds=False), State(has_taken_off=True))
        self.assertNotEqual(State(time_used_seconds=0), State(time_used_seconds=1))
        self.assertNotEqual(State(x_meters=0), State(x_meters=1))
        self.assertNotEqual(State(y_meters=0), State(y_meters=1))
        self.assertNotEqual(State(z_meters=0), State(z_meters=1))
        self.assertNotEqual(State(orientation_degrees=0), State(orientation_degrees=1))
        self.assertNotEqual(None, State.init_state())
