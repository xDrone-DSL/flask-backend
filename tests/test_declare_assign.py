import unittest

from xdrone import generate_commands
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable, Variable
from xdrone.visitors.compiler_utils.type import Type


class DeclareTest(unittest.TestCase):
    def test_declare_int_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { int a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.int(), 0, ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_decimal_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { decimal a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.decimal(), 0, ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_string_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { string a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.string(), "", ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_boolean_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { boolean a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.boolean(), False, ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_vector_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { vector a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.vector(), [0, 0, 0], ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_list_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { list[int] a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.int()), [], ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_nested_list_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { list[list[int]] a; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.list_of(Type.int())), [], ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_with_different_variable_name_should_change_symbol_table(self):
        for name in ["a", "A", "_a", "_1", "_A", "abc", "Abc", "a12", "aA1", "_aA1"]:
            actual = SymbolTable()
            generate_commands("""
                main () {{ int {}; }}
                """.format(name), actual)
            expected = SymbolTable()
            expected.store(name, Variable(Type.int(), 0, ident=name))
            self.assertEqual(expected, actual)

    def test_repeated_declare_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                 int a;
                 int a;
                }
                """)

        self.assertTrue("Identifier a already declared" in str(context.exception))

    def test_repeated_declare_different_type_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                 int a;
                 decimal a;
                }
                """)

        self.assertTrue("Identifier a already declared" in str(context.exception))


class AssignIdentTest(unittest.TestCase):
    def test_assign_ident_int_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             int a;
             a <- -1;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.int(), -1, ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_ident_decimal_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             decimal a;
             a <- -1.5e10;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.decimal(), -1.5e10, ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_ident_string_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             string a;
             a <- "1";
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.string(), "1", ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_ident_boolean_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             boolean a;
             a <- true;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.boolean(), True, ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_ident_vector_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             vector a;
             a <- (1.0, -1.0, +1.0);
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.vector(), [1, -1, 1], ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_ident_list_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             list[int] a;
             a <- [1, -1, +1];
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.int()), [1, -1, 1], ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_ident_nested_list_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             list[list[int]] a;
             a <- [[1], [-1], [+1]];
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.list_of(Type.int())), [[1], [-1], [1]], ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_ident_empty_list_should_update_symbol_table(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(),
                 Type.list_of(Type.int()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                 list[{}] a;
                 a <- [];
                }}
                """.format(type.type_name), actual)
            expected = SymbolTable()
            expected.store("a", Variable(Type.list_of(type), [], ident="a"))
            self.assertEqual(expected, actual)

    def test_assign_not_declared_variable_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                 a <- true;
                }
            """)

        self.assertTrue("Identifier a has not been declared" in str(context.exception))

    def test_declare_and_then_assign_with_different_type_should_give_error(self):
        types = ["int", "decimal", "string", "boolean", "vector", "list[int]", "list[decimal]", "list[list[int]]"]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        main () {{
                         {} a;
                         {} b;
                         a <- b;
                        }}
                    """.format(t1, t2))

                self.assertTrue("Identifier a has been declared as {}, but assigned as {}"
                                .format(t1, t2) in str(context.exception))

    def test_declare_and_then_assign_with_same_type_should_success(self):
        for type in ["int", "decimal", "string", "boolean", "vector", "list[int]", "list[decimal]", "list[list[int]]"]:
            generate_commands("""
                main () {{
                 {} a;
                 {} b;
                 a <- b;
                }}
            """.format(type, type))


class AssignVectorElemTest(unittest.TestCase):

    def test_assign_vector_elem_to_temp_vector_should_not_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             (0.0, 0.0, 0.0).x <- 1.0;
            }
            """, actual)
        expected = SymbolTable()
        self.assertEqual(expected, actual)

    def test_assign_vector_elem_to_variable_should_update_symbol_table(self):
        for index, vector in zip(["x", "y", "z"], [[-1.0, 0, 0], [0, -2.0, 0], [0, 0, -3.0]]):
            actual = SymbolTable()
            generate_commands("""
                main () {{
                 vector a;
                 a.{} <- (-1.0, -2.0, -3.0).{};
                }}
                """.format(index, index), actual)
            expected = SymbolTable()
            expected.store("a", Variable(Type.vector(), vector, ident="a"))
            self.assertEqual(expected, actual)

    def test_assign_vector_elem_not_declared_variable_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
            main () {
             a.x <- 1.0;
            }
            """)

        self.assertTrue("Identifier a has not been declared" in str(context.exception))

    def test_declare_and_then_assign_vector_elem_with_different_type_should_give_error(self):
        for type in [Type.int(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                     Type.list_of(Type.list_of(Type.int()))]:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                     vector a;
                     {} b;
                     a.x <- b;
                    }}
                """.format(type.type_name))

            self.assertTrue("Assigned value {} should have type decimal, but is {}"
                            .format(type.default_value, type.type_name) in str(context.exception))


class AssignListElemTest(unittest.TestCase):

    def test_assign_list_elem_to_temp_vector_should_not_change_symbol_table(self):
        for code in ["[0.0][0] <- 1.0", "[0][0] <- 1", "[[\"a\"]][0] <- [\"b\"]", "[0.0, 1.0][0] <- 1.0"]:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                 {};
                }}
                """.format(code), actual)
            expected = SymbolTable()
            self.assertEqual(expected, actual)

    def test_assign_list_elem_to_variable_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             list[int] a <- [0, 1, 2];
             a[0] <- 1;
             a[2] <- a[0];
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.int()), [1, 1, 1], ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_list_elem_to_variable_nested_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             list[list[int]] a <- [[0, 1], [2, 3]];
             a[0] <- [4, 5];
             a[1][0] <- 6;
             a[1][1] <- 7;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.list_of(Type.int())), [[4, 5], [6, 7]], ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_list_elem_with_vector_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
             list[vector] a <- [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)];
             a[0] <- (7.0, 8.0, 9.0);
             a[1].x <- 10.0;
             a[1].y <- 11.0;
             a[1].z <- 12.0;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.vector()), [[7, 8, 9], [10, 11, 12]], ident="a"))
        self.assertEqual(expected, actual)

    def test_assign_list_elem_to_variable_out_of_bound_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                 list[int] a <- [];
                 a[0] <- 1;
                }
                """)

        self.assertTrue(
            "List a has length 0, but has been assessed with out-of-range index 0" in str(context.exception))

    def test_assess_list_elem_out_of_bound_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                 list[int] a <- [1];
                 a[0] <- a[1];
                }
                """)

        self.assertTrue(
            "List a has length 1, but has been assessed with out-of-range index 1" in str(context.exception))

    def test_assess_list_elem_nested_out_of_bound_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                 list[list[list[int]]] a <- [[[1], [2]]];
                 a[0][2] <- [1];
                }
                """)
        self.assertTrue(
            "List a[0] has length 2, but has been assessed with out-of-range index 2" in str(context.exception))

        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                 list[list[list[int]]] a <- [[[1], [2]]];
                 a[0][1][1] <- 1;
                }
                """)
        self.assertTrue(
            "List a[0][1] has length 1, but has been assessed with out-of-range index 1" in str(context.exception))

    def test_assign_list_elem_not_declared_variable_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
            main () {
             a[0] <- 1;
            }
            """)

        self.assertTrue("Identifier a has not been declared" in str(context.exception))

    def test_declare_and_assign_list_elem_with_different_type_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(),
                 Type.list_of(Type.int()), Type.list_of(Type.list_of(Type.int()))]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                    main () {{
                     {} a;
                     list[{}] b <- [a];
                    }}
                    """.format(t1, t2))

                self.assertTrue("Identifier b has been declared as list[{}], but assigned as list[{}]"
                                .format(t2, t1) in str(context.exception))

    def test_assign_list_elem_with_different_type_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(),
                 Type.list_of(Type.int()), Type.list_of(Type.list_of(Type.int()))]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                    main () {{
                     {} a;
                     {} b;
                     list[{}] c <- [a];
                     c[0] <- b;
                    }}
                    """.format(t1, t2, t1))

                self.assertTrue("Assigned value {} should have type {}, but is {}"
                                .format(t2.default_value, t1.type_name, t2.type_name) in str(context.exception))


class CombinedDeclareAssignTest(unittest.TestCase):

    def test_declare_and_assign_int_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { int a <- 1; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.int(), 1, ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_and_assign_decimal_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { decimal a <- 1.0; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.decimal(), 1.0, ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_and_assign_string_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { string a <- "\0a"; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.string(), "\0a", ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_and_assign_boolean_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { boolean a <- true; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.boolean(), True, ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_and_assign_vector_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { vector a <- (1.0, 2.0, -3.0); }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.vector(), [1, 2, -3], ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_and_assign_list_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { list[int] a <- [1, 2, -3]; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.int()), [1, 2, -3], ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_and_assign_nested_list_should_change_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () { list[list[int]] a <- [[1], [2]]; }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Variable(Type.list_of(Type.list_of(Type.int())), [[1], [2]], ident="a"))
        self.assertEqual(expected, actual)

    def test_declare_and_assign_ident_empty_list_should_update_symbol_table(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(),
                 Type.list_of(Type.int()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                 list[{}] a <- [];
                }}
                """.format(type.type_name), actual)
            expected = SymbolTable()
            expected.store("a", Variable(Type.list_of(type), [], ident="a"))
            self.assertEqual(expected, actual)

    def test_repeated_declare_and_assign_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                 int a;
                 int a <- 0;
                }
                """)

        self.assertTrue("Identifier a already declared" in str(context.exception))

    def test_declare_and_assign_with_different_type_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.list_of(Type.int()))]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                    main () {{
                     {} a;
                     {} b <- a;
                    }}
                    """.format(t1, t2))

                self.assertTrue("Identifier b has been declared as {}, but assigned as {}"
                                .format(t2.type_name, t1.type_name) in str(context.exception))
