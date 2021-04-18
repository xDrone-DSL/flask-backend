import unittest

from xdrone import generate_commands, Command
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.expressions import Expression
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable
from xdrone.visitors.compiler_utils.type import Type


class IfTest(unittest.TestCase):
    def test_if_true_without_else_should_run_correct_commands(self):
        actual_st = SymbolTable()
        actual_commands = generate_commands("""
            main () {
              takeoff();
              if true {
                int a <- 1;
                forward(1);
              }
              land();
            }
            """, symbol_table=actual_st)
        expected_st = SymbolTable()
        expected_st.store("a", Expression(Type.int(), 1, ident="a"))
        self.assertEqual(expected_st, actual_st)
        expected_commands = [Command.takeoff(), Command.forward(1), Command.land()]
        self.assertEqual(expected_commands, actual_commands)

    def test_if_true_with_else_should_run_correct_commands(self):
        actual = SymbolTable()
        actual_commands = generate_commands("""
            main () {
              takeoff();
              if true {
                int a <- 1;
                forward(1);
              } else {
                int a <- 2;
                forward(2);
              }
              land();
            }
            """, symbol_table=actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 1, ident="a"))
        self.assertEqual(expected, actual)
        expected_commands = [Command.takeoff(), Command.forward(1), Command.land()]
        self.assertEqual(expected_commands, actual_commands)

    def test_if_false_without_else_should_do_nothing(self):
        actual = SymbolTable()
        actual_commands = generate_commands("""
            main () {
              if false {
                int a <- 1;
              }
            }
            """, symbol_table=actual)
        expected = SymbolTable()
        self.assertEqual(expected, actual)
        expected_commands = []
        self.assertEqual(expected_commands, actual_commands)

    def test_if_false_with_else_should_run_correct_commands(self):
        actual = SymbolTable()
        actual_commands = generate_commands("""
            main () {
              takeoff();
              if false {
                int a <- 1;
                forward(1);
              } else {
                int a <- 2;
                int b <- 3;
                forward(3);
              }
              land();
            }
            """, symbol_table=actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 2, ident="a"))
        expected.store("b", Expression(Type.int(), 3, ident="b"))
        self.assertEqual(expected, actual)
        expected_commands = [Command.takeoff(), Command.forward(3), Command.land()]
        self.assertEqual(expected_commands, actual_commands)

    def test_if_with_error_commands_not_entering_should_not_give_error(self):
        actual_commands = generate_commands("""
            main () {
              takeoff();
              if false {
                int a <- "error";
                forward(1);
              }
              land();
            }
            """)
        expected_commands = [Command.takeoff(), Command.land()]
        self.assertEqual(expected_commands, actual_commands)

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
        actual_commands = generate_commands("""
            main () {
              takeoff();
              int a <- 1;
              while a < 5 {
                a <- a + 1;
                forward(a);
              }
              land();
            }
            """, symbol_table=actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 5, ident="a"))
        self.assertEqual(expected, actual)
        expected_commands = [Command.takeoff()] + [Command.forward(i) for i in [2, 3, 4, 5]] + [Command.land()]
        self.assertEqual(expected_commands, actual_commands)

    def test_while_false_should_not_enter_loop(self):
        actual = SymbolTable()
        actual_commands = generate_commands("""
            main () {
              takeoff();
              int a <- 10;
              while a < 5 {
                a <- a + 1;
                forward(a);
              }
              land();
            }
            """, symbol_table=actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 10, ident="a"))
        self.assertEqual(expected, actual)
        expected_commands = [Command.takeoff(), Command.land()]
        self.assertEqual(expected_commands, actual_commands)

    def test_while_with_error_command_not_entering_should_not_give_error(self):
        actual_commands = generate_commands("""
            main () {
              while false {
                int a <- "error";
              }
            }
            """)
        expected_commands = []
        self.assertEqual(expected_commands, actual_commands)

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


class ForTest(unittest.TestCase):
    def test_for_without_step_should_run_correct_commands_and_update_symbol_table(self):
        actual_st = SymbolTable()
        actual_commands = generate_commands("""
            main () {
              takeoff();
              int i;
              int a <- 0;
              for i from 0 to 5 {
                a <- a + 1;
                forward(i);
              }
              land();
            }
            """, symbol_table=actual_st)
        expected_st = SymbolTable()
        expected_st.store("i", Expression(Type.int(), 5, ident="i"))
        expected_st.store("a", Expression(Type.int(), 6, ident="a"))
        self.assertEqual(expected_st, actual_st)
        expected_commands = [Command.takeoff()] + [Command.forward(i) for i in [0, 1, 2, 3, 4, 5]] + [Command.land()]
        self.assertEqual(expected_commands, actual_commands)

    def test_for_with_step_should_run_correct_commands_and_update_symbol_table(self):
        actual_st = SymbolTable()
        actual_commands = generate_commands("""
            main () {
              takeoff();
              int i;
              int a <- 0;
              for i from 0 to 9 step 2 {
                a <- a + 1;
                forward(i);
              }
              land();
            }
            """, symbol_table=actual_st)
        expected_st = SymbolTable()
        expected_st.store("i", Expression(Type.int(), 8, ident="i"))
        expected_st.store("a", Expression(Type.int(), 5, ident="a"))
        self.assertEqual(expected_st, actual_st)
        expected_commands = [Command.takeoff()] + [Command.forward(i) for i in [0, 2, 4, 6, 8]] + [Command.land()]
        self.assertEqual(expected_commands, actual_commands)

    def test_for_not_entering_should_not_update_symbol_table(self):
        actual_st = SymbolTable()
        actual_commands = generate_commands("""
            main () {
              takeoff();
              int i;
              int a <- 0;
              for i from 10 to 5 {
                a <- a + 1;
                forward(i);
              }
              land();
            }
            """, symbol_table=actual_st)
        expected_st = SymbolTable()
        expected_st.store("i", Expression(Type.int(), 0, ident="i"))
        expected_st.store("a", Expression(Type.int(), 0, ident="a"))
        self.assertEqual(expected_st, actual_st)
        expected_commands = [Command.takeoff(), Command.land()]
        self.assertEqual(expected_commands, actual_commands)

    def test_for_with_error_commands_not_entering_should_not_give_error(self):
        actual_commands = generate_commands("""
            main () {
              int i;
              for i from 10 to 5 {
                int a <- "error";
              }
            }
            """)
        expected_commands = []
        self.assertEqual(expected_commands, actual_commands)

    def test_for_with_not_declared_ident_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  for i from 0 to 9 step 2 {
                  }
                }
                """)

        self.assertTrue("Identifier i has not been declared" in str(context.exception))

    def test_for_with_wrong_type_ident_should_give_error(self):
        types = [Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} i;
                      for i from 0 to 9 step 2 {{
                      }}
                    }}
                    """.format(type))

            self.assertTrue("Identifier i has been declared as {}, but assigned as int"
                            .format(type)
                            in str(context.exception))

    def test_for_with_wrong_type_from_expr_should_give_error(self):
        types = [Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            for with_step in ["", "step 2"]:
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        main () {{
                          int i;
                          {} a;
                          for i from a to 9 {} {{
                          }}
                        }}
                        """.format(type, with_step))

                self.assertTrue("Expression {} should have type int, but is {}"
                                .format(Expression(type, type.default_value, ident="a"), type.type_name)
                                in str(context.exception))

    def test_for_with_wrong_type_to_expr_should_give_error(self):
        types = [Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            for with_step in ["", "step 2"]:
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        main () {{
                          int i;
                          {} a;
                          for i from 0 to a {} {{
                          }}
                        }}
                        """.format(type, with_step))

                self.assertTrue("Expression {} should have type int, but is {}"
                                .format(Expression(type, type.default_value, ident="a"), type.type_name)
                                in str(context.exception))

    def test_for_with_wrong_type_step_expr_should_give_error(self):
        types = [Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      int i;
                      {} a;
                      for i from 0 to 9 step a {{
                      }}
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type int, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))


class RepeatTest(unittest.TestCase):
    def test_repeat_should_run_correct_commands(self):
        actual_commands = generate_commands("""
            main () {
              takeoff();
              repeat 4 times {
                forward(1);
              }
              land();
            }
            """)
        expected_commands = [Command.takeoff()] + [Command.forward(1) for _ in range(4)] + [Command.land()]
        self.assertEqual(expected_commands, actual_commands)

    def test_repeat_with_wrong_type_expr_should_give_error(self):
        types = [Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      repeat a times {{
                      }}
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type int, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))
