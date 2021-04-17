import unittest

from xdrone import generate_simulation_json, SafetyChecker, SafetyConfig, StateUpdater, DroneConfig, DefaultSafetyConfig
from xdrone.visitors.state_safety_checker.safety_check_error import SafetyCheckError


class GenerateSimulationJsonTest(unittest.TestCase):
    def test_basic_program(self):
        commands = "main() {takeoff(); land();}"
        target = [{"action": "takeoff", "value": []},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))

    def test_square_no_turn(self):
        commands = "main() {takeoff(); forward(2); left(2); backward(2); right(2); land();}"
        target = [{"action": "takeoff", "value": []},
                  {"action": "forward", "value": [2]},
                  {"action": "left", "value": [2]},
                  {"action": "backward", "value": [2]},
                  {"action": "right", "value": [2]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))

    def test_square_with_turning(self):
        commands = "main() {takeoff(); forward(3); rotate_left(90); forward(3); rotate_left(90); forward(3); rotate_left(90); forward(3); rotate_left(90); land();}"
        target = [{"action": "takeoff", "value": []},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))

    def test_program_with_variable(self):
        commands = """
        main() {
            int distance <- 3;
            int angle <- 90;
            takeoff(); 
            forward(distance); 
            rotate_left(angle); 
            forward(distance); 
            rotate_left(angle);
            land();
        }
        """
        target = [{"action": "takeoff", "value": []},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))

    def test_program_with_list_variable(self):
        commands = """
        main() {
            list[int] distances <- [3, 4];
            list[int] angles <- [90, 180];
            takeoff(); 
            forward(distances[0]); 
            rotate_left(angles[0]); 
            forward(distances[1]); 
            rotate_left(angles[1]);
            distances[1] <- 3;
            angles[1] <- 90;
            forward(distances[1]); 
            rotate_left(angles[1]);
            land();
        }
        """
        target = [{"action": "takeoff", "value": []},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [4]},
                  {"action": "rotate_left", "value": [180]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))

    def test_square_using_repeat(self):
        commands = """
            main() {
              takeoff();
              repeat 4 times {
                forward(3); rotate_left(90);
              }
              land();
            }"""
        target = [{"action": "takeoff", "value": []},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))

    def test_square_using_two_repeats(self):
        commands = """
          main() {
            takeoff();
            repeat 2 times {
              repeat 2 times {
                forward(3); rotate_left(90);
              }
            }
            land();
          }"""
        target = [{"action": "takeoff", "value": []},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotate_left", "value": [90]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))

    def test_if_not_given_state_updater_should_use_default_to_update_state(self):
        commands = "main() {takeoff(); land();}"
        generate_simulation_json(commands, safety_checker=SafetyChecker(SafetyConfig(max_seconds=10, max_z_meters=1)))

    def test_if_given_state_updater_should_use_it_to_update_state(self):
        commands = "main() {takeoff(); land();}"
        with self.assertRaises(SafetyCheckError) as context:
            generate_simulation_json(commands,
                                     state_updater=StateUpdater(DroneConfig(speed_mps=1, rotate_speed_dps=90,
                                                                            takeoff_height_meters=10)),
                                     safety_checker=SafetyChecker(SafetyConfig(max_seconds=10, max_z_meters=1)))
        self.assertTrue("The z coordinate 10 will go beyond its upper limit 1" in str(context.exception))

    def test_if_not_given_safety_checker_should_not_check_safety(self):
        commands = "main() {up(1);}"
        generate_simulation_json(commands)

    def test_if_given_safety_checker_should_use_it_to_check_safety(self):
        commands = "main() {up(1);}"
        with self.assertRaises(SafetyCheckError) as context:
            generate_simulation_json(commands, safety_checker=SafetyChecker(DefaultSafetyConfig()))
        self.assertTrue("'up' command used when the drone has not been taken off" in str(context.exception))
