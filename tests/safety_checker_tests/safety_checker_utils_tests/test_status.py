import unittest

from xdrone.visitors.safety_checker_utils.status import Status


class StatusTest(unittest.TestCase):
    def test_init_state(self):
        status = Status.init_state()
        self.assertEqual(False, status.has_taken_off)
        self.assertEqual(0, status.time_used_seconds)
        self.assertEqual(0, status.x_meters)
        self.assertEqual(0, status.y_meters)
        self.assertEqual(0, status.z_meters)
        self.assertEqual(0, status.orientation_degrees)

    def test_set_values(self):
        status = Status.init_state()
        status.has_taken_off = True
        status.time_used_seconds = 1
        status.x_meters = 1
        status.y_meters = 1
        status.z_meters = 1
        status.orientation_degrees = 1
        self.assertEqual(True, status.has_taken_off)
        self.assertEqual(1, status.time_used_seconds)
        self.assertEqual(1, status.x_meters)
        self.assertEqual(1, status.y_meters)
        self.assertEqual(1, status.z_meters)
        self.assertEqual(1, status.orientation_degrees)

    def test_str(self):
        status = Status.init_state()
        self.assertEqual("Status: { has_taken_off: False, time_used_seconds: 0, " +
                         "x_meters: 0, y_meters: 0, z_meters: 0, orientation_degrees: 0 }",
                         str(status))

    def test_eq(self):
        self.assertEqual(Status.init_state(), Status.init_state())
        self.assertNotEqual(Status(time_used_seconds=False), Status(has_taken_off=True))
        self.assertNotEqual(Status(time_used_seconds=0), Status(time_used_seconds=1))
        self.assertNotEqual(Status(x_meters=0), Status(x_meters=1))
        self.assertNotEqual(Status(y_meters=0), Status(y_meters=1))
        self.assertNotEqual(Status(z_meters=0), Status(z_meters=1))
        self.assertNotEqual(Status(orientation_degrees=0), Status(orientation_degrees=1))
        self.assertNotEqual(None, Status.init_state())
