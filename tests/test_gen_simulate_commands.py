import unittest
from xdrone import gen_simulate_commands
from math import pi


class GenSimulateCommandsTest(unittest.TestCase):
    def test_basic_program(self):
        commands = "main() {takeoff(); land();}"
        target = [{"action": "takeoff", "value": []},
                  {"action": "land", "value": []}]
        self.assertEqual(target, gen_simulate_commands(commands))

    def test_square_no_turn(self):
        commands = "main() {takeoff(); forward(2); left(2); backward(2); right(2); land();}"
        target = [{"action": "takeoff", "value": []},
                  {"action": "forward", "value": [2]},
                  {"action": "left", "value": [2]},
                  {"action": "backward", "value": [2]},
                  {"action": "right", "value": [2]},
                  {"action": "land", "value": []}]
        self.assertEqual(target, gen_simulate_commands(commands))

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
        self.assertEqual(target, gen_simulate_commands(commands))

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
        self.assertEqual(target, gen_simulate_commands(commands))

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
        self.assertEqual(target, gen_simulate_commands(commands))
