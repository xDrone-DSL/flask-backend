import pytest
from xdrone import gen_simulate_commands
from math import pi



def test_basic_program():
  commands = "main() {takeoff() land()}"
  target = [{"action": "takeoff", "value": []},
            {"action": "land", "value": []}]
  assert gen_simulate_commands(commands) == target


def test_square_no_turn():
  commands = "main() {takeoff() forward(2) left(2) backward(2) right(2) land()}"
  target = [{"action": "takeoff", "value": []},
            {"action": "forward", "value": [2]},
            {"action": "left", "value": [2]},
            {"action": "backward", "value": [2]},
            {"action": "right", "value": [2]},
            {"action": "land", "value": []}]
  assert gen_simulate_commands(commands) == target


def test_square_with_turning():
  commands = "main() {takeoff() forward(3) rotate_left(90) forward(3) rotate_left(90) forward(3) rotate_left(90) forward(3) rotate_left(90) land()}"
  target = [{"action": "takeoff", "value": []},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "land", "value": []}]
  assert gen_simulate_commands(commands) == target


def test_square_using_repeat():
  commands = """
  main() {
    takeoff() 
    REPEAT 4 TIMES {
      forward(3) rotate_left(90)
    }
    land()
  }"""
  target = [{"action": "takeoff", "value": []},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "land", "value": []}]
  assert gen_simulate_commands(commands) == target

def test_square_using_two_repeats():
  commands = """
  main() {
    takeoff() 
    REPEAT 2 TIMES {
      REPEAT 2 TIMES {
        forward(3) rotate_left(90)
      }
    }
    land()
  }"""
  target = [{"action": "takeoff", "value": []},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "forward", "value": [3]},
            {"action": "rotateL", "value": [pi/2]},
            {"action": "land", "value": []}]
  assert gen_simulate_commands(commands) == target
