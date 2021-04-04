import unittest

from xdrone import generate_commands
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable
from xdrone.visitors.compiler_utils.expressions import Expression
from xdrone.visitors.compiler_utils.type import Type


class ListTest(unittest.TestCase):
    def test_list_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              list[int] a <- [];
              list[boolean] b <- [true, false];
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.list_of(Type.int()), [], ident="a"))
        expected.store("b", Expression(Type.list_of(Type.boolean()), [True, False], ident="b"))
        self.assertEqual(expected, actual)

    def test_list_with_inconsistent_type_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  list[int] a <- [1, 1.0];
                }
                """)
        self.assertTrue("Elements in list {} should have the same type"
                        .format([str(Expression(Type.int(), 1, None)), str(Expression(Type.decimal(), 1.0, None))])
                        in str(context.exception))

    def test_list_elem_assign_should_update_symbol_table_correctly(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              list[int] a <- [1, 2, 3];
              a[0] <- 4;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.list_of(Type.int()), [4, 2, 3], ident="a"))
        self.assertEqual(expected, actual)

    def test_list_elem_assign_with_wrong_ident_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector()]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      a[0] <- 1;
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type list, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_list_elem_assign_with_wrong_index_should_give_error(self):
        types = [Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      list[int] b;
                      b[a] <- 1;
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type int, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_list_elem_assign_out_of_range_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {{
                  list[int] a <- [1, 2];
                  a[2] <- 1;
                }}
                """.format(type))

        self.assertTrue("List {} has length {}, but has been assessed with out-of-range index {}"
                        .format("a", 2, 2)
                        in str(context.exception))

    def test_list_elem_expr_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              list[int] a <- [1, 2, 3];
              int b <- a[0];
              int c <- a[1];
              int d <- a[2];
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.list_of(Type.int()), [1, 2, 3], ident="a"))
        expected.store("b", Expression(Type.int(), 1, ident="b"))
        expected.store("c", Expression(Type.int(), 2, ident="c"))
        expected.store("d", Expression(Type.int(), 3, ident="d"))
        self.assertEqual(expected, actual)

    def test_list_elem_expr_with_wrong_ident_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector()]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- a[0];
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type list, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_list_elem_expr_with_wrong_index_should_give_error(self):
        types = [Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      list[int] b;
                      int c <- b[a];
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type int, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_list_elem_expr_out_of_range_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {{
                  list[int] a <- [1, 2];
                  int b <- a[2];
                }}
                """.format(type))

        self.assertTrue("List {} has length {}, but has been assessed with out-of-range index {}"
                        .format("a", 2, 2)
                        in str(context.exception))

