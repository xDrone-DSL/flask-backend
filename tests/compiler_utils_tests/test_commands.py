import unittest

from xdrone.visitors.compiler_utils.command import *


class TestCommands(unittest.TestCase):

    def test_takeoff(self):
        self.assertEqual(Command.takeoff(), Command.takeoff())
        self.assertEqual("takeoff", Command.takeoff().opcode)
        self.assertEqual([], Command.takeoff().operands)
        self.assertEqual("Command: { opcode: takeoff, operands: [] }", str(Command.takeoff()))
        self.assertEqual({"action": "takeoff", "value": []}, Command.takeoff().to_simulation_json())

    def test_land(self):
        self.assertEqual(Command.land(), Command.land())
        self.assertEqual("land", Command.land().opcode)
        self.assertEqual([], Command.land().operands)
        self.assertEqual("Command: { opcode: land, operands: [] }", str(Command.land()))
        self.assertEqual({"action": "land", "value": []}, Command.land().to_simulation_json())

    def test_up(self):
        self.assertEqual(Command.up(1), Command.up(1))
        self.assertEqual("up", Command.up(1).opcode)
        self.assertEqual([1], Command.up(1).operands)
        self.assertEqual("Command: { opcode: up, operands: [1] }", str(Command.up(1)))
        self.assertEqual({"action": "up", "value": [1]}, Command.up(1).to_simulation_json())

    def test_down(self):
        self.assertEqual(Command.down(1), Command.down(1))
        self.assertEqual("down", Command.down(1).opcode)
        self.assertEqual([1], Command.down(1).operands)
        self.assertEqual("Command: { opcode: down, operands: [1] }", str(Command.down(1)))
        self.assertEqual({"action": "down", "value": [1]}, Command.down(1).to_simulation_json())

    def test_left(self):
        self.assertEqual(Command.left(1), Command.left(1))
        self.assertEqual("left", Command.left(1).opcode)
        self.assertEqual([1], Command.left(1).operands)
        self.assertEqual("Command: { opcode: left, operands: [1] }", str(Command.left(1)))
        self.assertEqual({"action": "left", "value": [1]}, Command.left(1).to_simulation_json())

    def test_right(self):
        self.assertEqual(Command.right(1), Command.right(1))
        self.assertEqual("right", Command.right(1).opcode)
        self.assertEqual([1], Command.right(1).operands)
        self.assertEqual("Command: { opcode: right, operands: [1] }", str(Command.right(1)))
        self.assertEqual({"action": "right", "value": [1]}, Command.right(1).to_simulation_json())

    def test_forward(self):
        self.assertEqual(Command.forward(1), Command.forward(1))
        self.assertEqual("forward", Command.forward(1).opcode)
        self.assertEqual([1], Command.forward(1).operands)
        self.assertEqual("Command: { opcode: forward, operands: [1] }", str(Command.forward(1)))
        self.assertEqual({"action": "forward", "value": [1]}, Command.forward(1).to_simulation_json())

    def test_backward(self):
        self.assertEqual(Command.backward(1), Command.backward(1))
        self.assertEqual("backward", Command.backward(1).opcode)
        self.assertEqual([1], Command.backward(1).operands)
        self.assertEqual("Command: { opcode: backward, operands: [1] }", str(Command.backward(1)))
        self.assertEqual({"action": "backward", "value": [1]}, Command.backward(1).to_simulation_json())

    def test_rotate_left(self):
        self.assertEqual(Command.rotate_left(1), Command.rotate_left(1))
        self.assertEqual("rotateL", Command.rotate_left(1).opcode)
        self.assertEqual([1], Command.rotate_left(1).operands)
        self.assertEqual("Command: { opcode: rotateL, operands: [1] }", str(Command.rotate_left(1)))
        self.assertEqual({"action": "rotateL", "value": [1]}, Command.rotate_left(1).to_simulation_json())

    def test_rotate_right(self):
        self.assertEqual(Command.rotate_right(1), Command.rotate_right(1))
        self.assertEqual("rotateR", Command.rotate_right(1).opcode)
        self.assertEqual([1], Command.rotate_right(1).operands)
        self.assertEqual("Command: { opcode: rotateR, operands: [1] }", str(Command.rotate_right(1)))
        self.assertEqual({"action": "rotateR", "value": [1]}, Command.rotate_right(1).to_simulation_json())

    def test_wait(self):
        self.assertEqual(Command.wait(1), Command.wait(1))
        self.assertEqual("wait", Command.wait(1).opcode)
        self.assertEqual([1], Command.wait(1).operands)
        self.assertEqual("Command: { opcode: wait, operands: [1] }", str(Command.wait(1)))
        self.assertEqual({"action": "wait", "value": [1]}, Command.wait(1).to_simulation_json())

    def test_eq(self):
        commands1 = [Command.takeoff(), Command.land(),
                  Command.up(1), Command.down(1), Command.left(1), Command.right(1), Command.forward(1),
                  Command.backward(1), Command.rotate_left(1), Command.rotate_right(1), Command.wait(1),
                  Command.up(2), Command.down(2), Command.left(2), Command.right(2), Command.forward(2),
                  Command.backward(2), Command.rotate_left(2), Command.rotate_right(2), Command.wait(2)]
        commands2 = [Command.takeoff(), Command.land(),
                  Command.up(1), Command.down(1), Command.left(1), Command.right(1), Command.forward(1),
                  Command.backward(1), Command.rotate_left(1), Command.rotate_right(1), Command.wait(1),
                  Command.up(2), Command.down(2), Command.left(2), Command.right(2), Command.forward(2),
                  Command.backward(2), Command.rotate_left(2), Command.rotate_right(2), Command.wait(2)]
        for i, j in zip(range(len(commands1)), range(len(commands2))):
            if i == j:
                self.assertEqual(commands1[i], commands2[j])
            else:
                self.assertNotEqual(commands1[i], commands2[j])

    def test_corrupted_command_not_affect_correct_type(self):
        command = Command.forward(1)
        corrupted_command = Command.forward(1)
        corrupted_command._opcode = "corrupted"
        self.assertNotEqual(command, corrupted_command)
        self.assertEqual("forward", Command.forward(1).opcode)
        self.assertEqual([1], Command.forward(1).operands)
        self.assertEqual("corrupted", corrupted_command.opcode)
        self.assertEqual([1], corrupted_command.operands)
