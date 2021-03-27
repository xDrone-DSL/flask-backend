import unittest

from xdrone import gen_simulate_commands
from xdrone.visitors.compiler_utils.compile_error import CompileError


class DeclareTest(unittest.TestCase):
    def test_declare(self):
        gen_simulate_commands("""
            main () { int a; }
            """)

    def test_repeated_declare(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
                main () {
                 int a;
                 int a;
                }
                """)

        self.assertTrue("Identifier a already declared" in str(context.exception))


class AssignTest(unittest.TestCase):
    def test_assign(self):
        gen_simulate_commands("""
            main () {
             int a;
             a <- 1;
             }
            """)

    def test_assign_not_declared_variable(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
            main () {
             a <- true;
             }
            """)

        self.assertTrue("Identifier a has not been declared" in str(context.exception))

    def test_declare_and_then_assign_with_different_type(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
            main () {
             int a;
             a <- true;
             }
            """)

        self.assertTrue("Identifier a has been declared as int, but assigned as boolean" in str(context.exception))

class CombinedDeclareAssignTest(unittest.TestCase):
    def test_declare_and_assign(self):
        gen_simulate_commands("""
            main () { int a <- 0; }
            """)

    def test_repeated_declare_assign(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
                main () {
                 int a;
                 int a <- 0;
                }
                """)

        self.assertTrue("Identifier a already declared" in str(context.exception))

    def test_declare_and_assign_with_different_type(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
            main () { int a <- true; }
            """)

        self.assertTrue("Identifier a has been declared as int, but assigned as boolean" in str(context.exception))



