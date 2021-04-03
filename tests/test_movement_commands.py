import unittest

from xdrone import generate_commands, Command
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.type import Type


class MovementCommandsTest(unittest.TestCase):
    def test_takeoff_should_return_correct_command(self):
        actual = generate_commands("""
            main() { takeoff(); }
        """)
        expected = [Command.takeoff()]
        self.assertEqual(expected, actual)

    def test_land_should_return_correct_command(self):
        actual = generate_commands("""
            main() { land(); }
        """)
        expected = [Command.land()]
        self.assertEqual(expected, actual)

    def test_up_with_int_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { up(1); }
        """)
        expected = [Command.up(1)]
        self.assertEqual(expected, actual)

    def test_up_with_decimal_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { up(1.0); }
        """)
        expected = [Command.up(1.0)]
        self.assertEqual(expected, actual)

    def test_up_with_incorrect_parameter_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main() {{
                      {} a;
                      up(a); 
                    }}
                """.format(type.type_name))

            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))

    def test_down_with_int_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { down(1); }
        """)
        expected = [Command.down(1)]
        self.assertEqual(expected, actual)

    def test_down_with_decimal_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { down(1.0); }
        """)
        expected = [Command.down(1.0)]
        self.assertEqual(expected, actual)

    def test_down_with_incorrect_parameter_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main() {{
                      {} a;
                      down(a); 
                    }}
                """.format(type.type_name))

            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))

    def test_left_with_int_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { left(1); }
        """)
        expected = [Command.left(1)]
        self.assertEqual(expected, actual)

    def test_left_with_decimal_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { left(1.0); }
        """)
        expected = [Command.left(1.0)]
        self.assertEqual(expected, actual)

    def test_left_with_incorrect_parameter_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main() {{
                      {} a;
                      left(a); 
                    }}
                """.format(type.type_name))

            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))

    def test_right_with_int_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { right(1); }
        """)
        expected = [Command.right(1)]
        self.assertEqual(expected, actual)

    def test_right_with_decimal_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { right(1.0); }
        """)
        expected = [Command.right(1.0)]
        self.assertEqual(expected, actual)

    def test_right_with_incorrect_parameter_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main() {{
                      {} a;
                      right(a); 
                    }}
                """.format(type.type_name))

            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))

    def test_forward_with_int_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { forward(1); }
        """)
        expected = [Command.forward(1)]
        self.assertEqual(expected, actual)

    def test_forward_with_decimal_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { forward(1.0); }
        """)
        expected = [Command.forward(1.0)]
        self.assertEqual(expected, actual)

    def test_forward_with_incorrect_parameter_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main() {{
                      {} a;
                      forward(a); 
                    }}
                """.format(type.type_name))

            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))

    def test_backward_with_int_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { backward(1); }
        """)
        expected = [Command.backward(1)]
        self.assertEqual(expected, actual)

    def test_backward_with_decimal_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { backward(1.0); }
        """)
        expected = [Command.backward(1.0)]
        self.assertEqual(expected, actual)

    def test_backward_with_incorrect_parameter_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main() {{
                      {} a;
                      backward(a); 
                    }}
                """.format(type.type_name))

            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))

    def test_rotate_left_with_int_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { rotate_left(1); }
        """)
        expected = [Command.rotate_left(1)]
        self.assertEqual(expected, actual)

    def test_rotate_left_with_decimal_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { rotate_left(1.0); }
        """)
        expected = [Command.rotate_left(1.0)]
        self.assertEqual(expected, actual)

    def test_rotate_left_with_incorrect_parameter_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main() {{
                      {} a;
                      rotate_left(a); 
                    }}
                """.format(type.type_name))

            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))

    def test_rotate_right_with_int_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { rotate_right(1); }
        """)
        expected = [Command.rotate_right(1)]
        self.assertEqual(expected, actual)

    def test_rotate_right_with_decimal_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { rotate_right(1.0); }
        """)
        expected = [Command.rotate_right(1.0)]
        self.assertEqual(expected, actual)

    def test_rotate_right_with_incorrect_parameter_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main() {{
                      {} a;
                      rotate_right(a); 
                    }}
                """.format(type.type_name))

            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))

    def test_wait_with_int_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { wait(1); }
        """)
        expected = [Command.wait(1)]
        self.assertEqual(expected, actual)

    def test_wait_with_decimal_parameter_should_return_correct_command(self):
        actual = generate_commands("""
            main() { wait(1.0); }
        """)
        expected = [Command.wait(1.0)]
        self.assertEqual(expected, actual)

    def test_wait_with_incorrect_parameter_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main() {{
                      {} a;
                      wait(a); 
                    }}
                """.format(type.type_name))

            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))

    def test_multiple_commands_should_return_correct_command(self):
        actual = generate_commands("""
            main() {
             takeoff();
             up(1);
             down(2);
             left(3);
             right(4);
             forward(5);
             backward(6);
             rotate_left(7);
             rotate_right(8);
             wait(9);
             land(); 
            }
        """)
        expected = [Command.takeoff(), Command.up(1), Command.down(2), Command.left(3), Command.right(4),
                    Command.forward(5), Command.backward(6), Command.rotate_left(7), Command.rotate_right(8),
                    Command.wait(9), Command.land()]
        self.assertEqual(expected, actual)
