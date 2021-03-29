import unittest

from xdrone import gen_simulate_commands
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable, Variable
from xdrone.visitors.compiler_utils.type import Type


class DeclareTest(unittest.TestCase):
    def test_declare_int_should_change_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () { int a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.int(), 0))
        self.assertEqual(expected, actual)

    def test_declare_decimal_should_change_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () { decimal a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.decimal(), 0))
        self.assertEqual(expected, actual)

    def test_declare_string_should_change_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () { string a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.string(), ""))
        self.assertEqual(expected, actual)

    def test_declare_boolean_should_change_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () { boolean a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.boolean(), False))
        self.assertEqual(expected, actual)

    def test_declare_vector_should_change_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () { vector a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.vector(), [0, 0, 0]))
        self.assertEqual(expected, actual)

    def test_declare_list_should_change_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () { list[int] a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.int()), []))
        self.assertEqual(expected, actual)

    def test_declare_nested_list_should_change_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () { list[list[int]] a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.list_of(Type.int())), []))
        self.assertEqual(expected, actual)

    def test_repeated_declare_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
                main () {
                 int a;
                 int a;
                }
                """)

        self.assertTrue("Identifier a already declared" in str(context.exception))

    def test_repeated_declare_different_type_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
                main () {
                 int a;
                 decimal a;
                }
                """)

        self.assertTrue("Identifier a already declared" in str(context.exception))


class AssignIdentTest(unittest.TestCase):
    def test_assign_ident_int_should_update_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () {
             int a;
             a <- -1;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.int(), -1))
        self.assertEqual(expected, actual)

    def test_assign_ident_decimal_should_update_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () {
             decimal a;
             a <- -1.5e10;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.decimal(), -1.5e10))
        self.assertEqual(expected, actual)

    def test_assign_ident_string_should_update_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () {
             string a;
             a <- "1";
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.string(), "1"))
        self.assertEqual(expected, actual)

    def test_assign_ident_boolean_should_update_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () {
             boolean a;
             a <- true;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.boolean(), True))
        self.assertEqual(expected, actual)

    def test_assign_ident_vector_should_update_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () {
             vector a;
             a <- (1.0, -1.0, +1.0);
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.vector(), [1, -1, 1]))
        self.assertEqual(expected, actual)

    def test_assign_ident_list_should_update_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () {
             list[int] a;
             a <- [1, -1, +1];
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.int()), [1, -1, 1]))
        self.assertEqual(expected, actual)

    def test_assign_ident_nested_list_should_update_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () {
             list[list[int]] a;
             a <- [[1], [-1], [+1]];
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.list_of(Type.int())), [[1], [-1], [1]]))
        self.assertEqual(expected, actual)

    def test_assign_not_declared_variable_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
                main () {
                 a <- true;
                }
            """)

        self.assertTrue("Identifier a has not been declared" in str(context.exception))

    def test_declare_and_then_assign_with_different_type_should_give_error(self):
        types = ["int", "decimal", "string", "boolean", "vector", "list[int]", "list[decimal]", "list[list[int]]"]
        for t1, t2 in zip(types, types):
            if t1 != t2:
                with self.assertRaises(CompileError) as context:
                    gen_simulate_commands("""
                        main () {{
                         {} a;
                         {} b;
                         a <- b;
                        }}
                    """.format(t1, t2))

                self.assertTrue("Identifier a has been declared as {}, but assigned as {}".format(t1, t2) in str(context.exception))

    def test_declare_and_then_assign_with_same_type_should_success(self):
        for type in ["int", "decimal", "string", "boolean", "vector", "list[int]", "list[decimal]", "list[list[int]]"]:
            gen_simulate_commands("""
                main () {{
                 {} a;
                 {} b;
                 a <- b;
                }}
            """.format(type, type))

class AssignVectorElemTest(unittest.TestCase):

    def test_assign_vector_elem_to_temp_vector_should_not_change_symbol_table(self):
        actual = SymbolTable()
        gen_simulate_commands("""
            main () {
             (0.0, 0.0, 0.0).x <- 1.0;
            }
            """, actual)
        expected = SymbolTable()
        self.assertEqual(expected, actual)

    def test_assign_vector_elem_to_variable_should_change_symbol_table(self):
        for index, vector in zip(["x", "y", "z"], [[-1.0, 0, 0], [0, -1.0, 0], [0, 0, -1.0]]):
            actual = SymbolTable()
            gen_simulate_commands("""
                main () {{
                 vector a;
                 a.{} <- -1.0;
                }}
                """.format(index), actual)
            expected = SymbolTable()
            expected.store("a", Variable(Type.vector(), vector))
            print(expected)
            print(actual)
            self.assertEqual(expected, actual)

    def test_assign_vector_elem_not_declared_variable_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            gen_simulate_commands("""
            main () {
             a.x <- 1.0;
            }
            """)

        self.assertTrue("Identifier a has not been declared" in str(context.exception))


    def test_declare_and_then_assign_vector_elem_with_different_type_should_give_error(self):
        for type in [Type.int(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()), Type.list_of(Type.list_of(Type.int()))]:
            with self.assertRaises(CompileError) as context:
                gen_simulate_commands("""
                    main () {{
                     vector a;
                     {} b;
                     a.x <- b;
                    }}
                """.format(type.type_name))

            self.assertTrue("Assigned value {} should have type decimal, but is {}".format(type.default_value, type.type_name) in str(context.exception))

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



