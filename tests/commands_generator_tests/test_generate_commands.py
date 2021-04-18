import unittest

from xdrone import generate_commands, SafetyChecker, DefaultSafetyConfig, SafetyConfig, DroneConfig, StateUpdater
from xdrone.visitors.compiler_utils.command import Command
from xdrone.visitors.compiler_utils.compile_error import CompileError, XDroneSyntaxError
from xdrone.visitors.state_safety_checker.safety_check_error import SafetyCheckError


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

    def test_if_not_given_state_updater_should_use_default_to_update_state(self):
        commands = "main() {takeoff(); land();}"
        generate_commands(commands, safety_checker=SafetyChecker(SafetyConfig(max_seconds=10, max_z_meters=1)))

    def test_if_given_state_updater_should_use_it_to_update_state(self):
        commands = "main() {takeoff(); land();}"
        with self.assertRaises(SafetyCheckError) as context:
            generate_commands(commands,
                              state_updater=StateUpdater(DroneConfig(speed_mps=1, rotate_speed_dps=90,
                                                                     takeoff_height_meters=10)),
                              safety_checker=SafetyChecker(SafetyConfig(max_seconds=10, max_z_meters=1)))
        self.assertTrue("The z coordinate 10 will go beyond its upper limit 1" in str(context.exception))

    def test_if_not_given_safety_checker_should_use_default_to_check_safety(self):
        commands = "main() {takeoff(); wait(1000); up(1000); land();}"
        generate_commands(commands)

    def test_if_given_safety_checker_should_use_it_to_check_safety(self):
        commands = "main() {takeoff(); up(1000); land();}"
        with self.assertRaises(SafetyCheckError) as context:
            generate_commands(commands, safety_checker=SafetyChecker(SafetyConfig(max_seconds=10000, max_z_meters=1)))
        self.assertTrue("The z coordinate 1001 will go beyond its upper limit 1" in str(context.exception))
