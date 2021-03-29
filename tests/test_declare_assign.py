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


class AssignIdentTest(unittest.TestCase):
    def test_assign_ident_int(self):
        gen_simulate_commands("""
            main () {
             int a;
             a <- 1;
            }
            """)
    #TODO: other types
    def test_assign_ident_vector(self):
        gen_simulate_commands("""
            main () {
             vector a;
             a <- (1.0, 1.0, 1.0);
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

class AssignVectorElemTest(unittest.TestCase):

    def test_assign_vector_elem(self):
        gen_simulate_commands("""
            main () {
             (0.0, 0.0, 0.0).x <- 1.0;
            }
            """)
    #TODO: check symble table
    def test_assign_vector_elem_to_variable(self):
        gen_simulate_commands("""
            main () {
             vector a;
             a.x <- 1.0;
            }
            """)

    def test_assign_vector_elem_not_declared_variable(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
            main () {
             a.x <- 1.0;
            }
            """)

        self.assertTrue("Identifier a has not been declared" in str(context.exception))

    def test_declare_and_then_assign_vector_elem_with_different_type(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
            main () {
             vector a;
             a.x <- 1;
            }
            """)

        self.assertTrue("Assigned value 1 should have type decimal, but is int" in str(context.exception))

class AssignListElemTest(unittest.TestCase):

    def test_assign_list_elem(self):
        gen_simulate_commands("""
            main () {
             [0.0][0] <- 1.0;
            }
            """)
        gen_simulate_commands("""
            main () {
             [0][0] <- 1;
            }
            """)
        gen_simulate_commands("""
            main () {
             [["a"]][0] <- ["b"];
            }
            """)
        gen_simulate_commands("""
            main () {
             [0.0, 1.0][0] <- 1.0;
            }
            """)

    #TODO: check symble table
    def test_assign_list_elem_to_variable(self):
        gen_simulate_commands("""
            main () {
             list[int] a <- [0, 1, 2];
             a[0] <- 1;
             a[2] <- a[0];
            }
            """)

    def test_assign_list_elem_not_declared_variable(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
            main () {
             a[0] <- 1;
            }
            """)

        self.assertTrue("Identifier a has not been declared" in str(context.exception))

    def test_declare_and_assign_list_elem_with_different_type(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
            main () {
             list[decimal] a <- [1];
            }
            """)

        self.assertTrue("Identifier a has been declared as list[decimal], but assigned as list[int]" in str(context.exception))

    def test_declare_and_then_assign_list_elem_with_different_type(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
            main () {
             list[decimal] a <- [1.0];
             a[0] <- 1;
            }
            """)

        self.assertTrue("Assigned value 1 should have type decimal, but is int" in str(context.exception))

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



