import unittest

from xdrone import generate_commands
from xdrone.visitors.compiler_utils.command import Command
from xdrone.visitors.compiler_utils.compile_error import CompileError, XDroneSyntaxError


class GenerateCommandsTest(unittest.TestCase):
    def test_basic_program(self):
        commands = "main() {takeoff(); land();}"
        expected = [Command.takeoff(), Command.land()]
        self.assertEqual(expected, generate_commands(commands))

    def test_syntax_error_should_be_reported(self):
        commands = "main() {takeoff() land();}"
        with self.assertRaises(XDroneSyntaxError) as context:
            generate_commands(commands)
        self.assertTrue("missing ';' at 'land'" in str(context.exception))

    def test_all_syntax_errors_should_be_reported(self):
        commands = "main() {takeoff() land()}"
        with self.assertRaises(XDroneSyntaxError) as context:
            generate_commands(commands)
        self.assertTrue("missing ';' at 'land'" in str(context.exception))
        self.assertTrue("missing ';' at '}'" in str(context.exception))

    def test_compile_error_should_be_reported(self):
        commands = "main() {takeoff(); up(\"abc\"); land();}"
        with self.assertRaises(CompileError) as context:
            generate_commands(commands)
        self.assertTrue("should have type int or decimal, but is string" in str(context.exception))
