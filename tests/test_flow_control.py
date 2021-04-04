import unittest

from xdrone import generate_commands
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable
from xdrone.visitors.compiler_utils.expressions import Expression
from xdrone.visitors.compiler_utils.type import Type


class IfTest(unittest.TestCase):
    def test_if_true_without_else_should_run_correct_commands(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              if true {
                int a <- 1;
              }
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 1, ident="a"))
        self.assertEqual(expected, actual)

    def test_if_true_with_else_should_run_correct_commands(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              if true {
                int a <- 1;
              } else {
                int a <- 2;
              }
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 1, ident="a"))
        self.assertEqual(expected, actual)

    def test_if_false_without_else_should_do_nothing(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              if false {
                int a <- 1;
              }
            }
            """, actual)
        expected = SymbolTable()
        self.assertEqual(expected, actual)

    def test_if_false_with_else_should_run_correct_commands(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              if false {
                int a <- 1;
              } else {
                int a <- 2;
                int b <- 3;
              }
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 2, ident="a"))
        expected.store("b", Expression(Type.int(), 3, ident="b"))
        self.assertEqual(expected, actual)

    def test_if_wrong_type_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      if a {{
                        int b <- 1;
                      }} else {{
                        int b <- 2;
                      }}
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type boolean, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))


class WhileTest(unittest.TestCase):
    def test_while_should_run_correct_commands(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 1;
              while a < 5 {
                a <- a + 1;
              }
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 5, ident="a"))
        self.assertEqual(expected, actual)

    def test_while_false_should_not_enter_loop(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 10;
              while a < 5 {
                a <- a + 1;
              }
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 10, ident="a"))
        self.assertEqual(expected, actual)

    def test_while_wrong_type_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- 1;
                      while a {{
                        b <- b + 1;
                      }}
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type boolean, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))
