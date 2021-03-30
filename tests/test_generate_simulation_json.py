import unittest
from xdrone import generate_simulation_json
from math import pi


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
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
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
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
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
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [4]},
                  {"action": "rotateL", "value": [pi]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))

    def test_square_using_repeat(self):
        commands = """
            main() {
              takeoff();
              repeat 4 times {
                forward(3); rotate_left(90);
              };
              land();
            }"""
        target = [{"action": "takeoff", "value": []},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))

    def test_square_using_two_repeats(self):
        commands = """
          main() {
            takeoff();
            repeat 2 times {
              repeat 2 times {
                forward(3); rotate_left(90);
              };
            };
            land();
          }"""
        target = [{"action": "takeoff", "value": []},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "forward", "value": [3]},
                  {"action": "rotateL", "value": [pi / 2]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, generate_simulation_json(commands))
