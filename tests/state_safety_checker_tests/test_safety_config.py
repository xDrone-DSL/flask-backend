import unittest

from xdrone import SafetyConfig
from xdrone.visitors.state_safety_checker.safety_check_error import SafetyCheckError
from xdrone.visitors.state_safety_checker.state import State


class SafetyConfigTest(unittest.TestCase):
    def test_init_with_wrong_parameter_should_give_error(self):
        with self.assertRaises(ValueError) as context:
            SafetyConfig(max_seconds=-1)
        self.assertTrue("max_seconds should >= 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            SafetyConfig(max_x_meters=-1, min_x_meters=1)
        self.assertTrue("max_x_meters should >= min_x_meters" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            SafetyConfig(max_y_meters=-1, min_y_meters=1)
        self.assertTrue("max_y_meters should >= min_y_meters" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            SafetyConfig(max_z_meters=-1, min_z_meters=1)
        self.assertTrue("max_z_meters should >= min_z_meters" in str(context.exception))

    def test_init_values(self):
        safety_config = SafetyConfig()
        self.assertEqual(float("inf"), safety_config._max_seconds)
        self.assertEqual(float("inf"), safety_config._max_x_meters)
        self.assertEqual(float("inf"), safety_config._max_y_meters)
        self.assertEqual(float("inf"), safety_config._max_z_meters)
        self.assertEqual(float("-inf"), safety_config._min_x_meters)
        self.assertEqual(float("-inf"), safety_config._min_y_meters)
        self.assertEqual(float("-inf"), safety_config._min_z_meters)

    def test_no_limit_values(self):
        safety_config = SafetyConfig.no_limit()
        self.assertEqual(float("inf"), safety_config._max_seconds)
        self.assertEqual(float("inf"), safety_config._max_x_meters)
        self.assertEqual(float("inf"), safety_config._max_y_meters)
        self.assertEqual(float("inf"), safety_config._max_z_meters)
        self.assertEqual(float("-inf"), safety_config._min_x_meters)
        self.assertEqual(float("-inf"), safety_config._min_y_meters)
        self.assertEqual(float("-inf"), safety_config._min_z_meters)

    def test_str(self):
        safety_config = SafetyConfig(max_seconds=1, max_x_meters=2, max_y_meters=3, max_z_meters=4,
                                     min_x_meters=-2, min_y_meters=-3, min_z_meters=-4)
        self.assertEqual("SafetyConfig: { max_seconds: 1, x_range_meters: (-2, 2), " +
                         "y_range_meters: (-3, 3), z_range_meters: (-4, 4) }",
                         str(safety_config))

    def test_eq(self):
        self.assertEqual(SafetyConfig(), SafetyConfig())
        self.assertNotEqual(SafetyConfig(max_seconds=0), SafetyConfig(max_seconds=1))
        self.assertNotEqual(SafetyConfig(max_x_meters=0), SafetyConfig(max_x_meters=1))
        self.assertNotEqual(SafetyConfig(max_y_meters=0), SafetyConfig(max_y_meters=1))
        self.assertNotEqual(SafetyConfig(max_z_meters=0), SafetyConfig(max_z_meters=1))
        self.assertNotEqual(SafetyConfig(min_x_meters=0), SafetyConfig(min_x_meters=-1))
        self.assertNotEqual(SafetyConfig(min_y_meters=0), SafetyConfig(min_y_meters=-1))
        self.assertNotEqual(SafetyConfig(min_z_meters=0), SafetyConfig(min_z_meters=-1))
        self.assertNotEqual(None, SafetyConfig())

    def test_check_state_if_beyond_limit_should_give_error(self):
        safety_config = SafetyConfig(max_seconds=0, max_x_meters=0, max_y_meters=0, max_z_meters=0,
                                     min_x_meters=0, min_y_meters=0, min_z_meters=0)
        with self.assertRaises(SafetyCheckError) as context:
            safety_config.check_state(State(x_meters=10))
        self.assertTrue("The x coordinate 10 will go beyond its upper limit 0" in str(context.exception))

        with self.assertRaises(SafetyCheckError) as context:
            safety_config.check_state(State(y_meters=10))
        self.assertTrue("The y coordinate 10 will go beyond its upper limit 0" in str(context.exception))

        with self.assertRaises(SafetyCheckError) as context:
            safety_config.check_state(State(z_meters=10))
        self.assertTrue("The z coordinate 10 will go beyond its upper limit 0" in str(context.exception))

        with self.assertRaises(SafetyCheckError) as context:
            safety_config.check_state(State(x_meters=-10))
        self.assertTrue("The x coordinate -10 will go beyond its lower limit 0" in str(context.exception))

        with self.assertRaises(SafetyCheckError) as context:
            safety_config.check_state(State(y_meters=-10))
        self.assertTrue("The y coordinate -10 will go beyond its lower limit 0" in str(context.exception))

        with self.assertRaises(SafetyCheckError) as context:
            safety_config.check_state(State(z_meters=-10))
        self.assertTrue("The z coordinate -10 will go beyond its lower limit 0" in str(context.exception))

        with self.assertRaises(SafetyCheckError) as context:
            safety_config.check_state(State(time_used_seconds=10))
        self.assertTrue("The time used 10 seconds will go beyond the time limit 0 seconds" in str(context.exception))

    def test_check_state_if_no_limit_should_not_give_error(self):
        safety_config = SafetyConfig()
        for number in [1e-5, 1e-3, 1e0, 1e3, 1e5, 1e10, float('inf')]:
            safety_config.check_state(State(x_meters=number))
            safety_config.check_state(State(y_meters=number))
            safety_config.check_state(State(z_meters=number))
            safety_config.check_state(State(x_meters=-number))
            safety_config.check_state(State(y_meters=-number))
            safety_config.check_state(State(z_meters=-number))
            safety_config.check_state(State(time_used_seconds=number))
