import pytest
from xdrone import gen_simulate_commands
from math import pi



def test_basic_program():
  commands = "fly() {TAKEOFF() LAND()}"
  target = [{"action": "takeoff", "value": []},
            {"action": "land", "value": []}]
  assert gen_simulate_commands(commands) == target


def test_square_no_turn():
  commands = "fly() {TAKEOFF() FORWARD(2) LEFT(2) BACKWARD(2) RIGHT(2) LAND()}"
  target = [{"action": "takeoff", "value": []},
            {"action": "forward", "value": [2]},
            {"action": "left", "value": [2]},
            {"action": "backward", "value": [2]},
            {"action": "right", "value": [2]},
            {"action": "land", "value": []}]
  assert gen_simulate_commands(commands) == target


def test_square_with_turning():
  commands = "fly() {TAKEOFF() FORWARD(3) ROTATELEFT(90) FORWARD(3) ROTATELEFT(90) FORWARD(3) ROTATELEFT(90) FORWARD(3) ROTATELEFT(90) LAND()}"
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
  fly() {
    TAKEOFF() 
    REPEAT 4 TIMES {
      FORWARD(3) ROTATELEFT(90)
    }
    LAND()
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
  fly() {
    TAKEOFF() 
    REPEAT 2 TIMES {
      REPEAT 2 TIMES {
        FORWARD(3) ROTATELEFT(90)
      }
    }
    LAND()
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
