import unittest

from xdrone import generate_commands
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable
from xdrone.visitors.compiler_utils.expressions import Expression
from xdrone.visitors.compiler_utils.type import Type


class EscapedStringTest(unittest.TestCase):
    def test_normal_string_should_be_parsed_to_correct_expr(self):
        for string in ["", "abc", " ", "abc 123"]:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                  string a <- "{}";
                }}
                """.format(string), actual)
            expected = SymbolTable()
            expected.store("a", Expression(Type.string(), string, ident="a"))
            self.assertEqual(expected, actual)

    def test_escaped_string_should_be_parsed_to_correct_expr(self):
        for escaped, unescaped in [(r"\0", "\0"), (r"\n", "\n"), (r" \"", " \"")]:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                  string a <- "{}";
                }}
                """.format(escaped), actual)
            expected = SymbolTable()
            expected.store("a", Expression(Type.string(), unescaped, ident="a"))
            self.assertEqual(expected, actual)


class BooleanOperationTest(unittest.TestCase):
    def test_bool_or_should_return_correct_value(self):
        for b1, b2 in [("true", "true"), ("true", "false"), ("false", "true"), ("false", "false")]:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                  boolean a <- {} or {};
                }}
                """.format(b1, b2), actual)
            expected = SymbolTable()
            expected.store("a", Expression(Type.boolean(), (b1 == 'true') or (b2 == 'true'), ident="a"))
            self.assertEqual(expected, actual)

    def test_bool_or_with_wrong_type_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- a or true;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type boolean, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- true or a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type boolean, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_bool_and_should_return_correct_value(self):
        for b1, b2 in [("true", "true"), ("true", "false"), ("false", "true"), ("false", "false")]:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                  boolean a <- {} and {};
                }}
                """.format(b1, b2), actual)
            expected = SymbolTable()
            expected.store("a", Expression(Type.boolean(), (b1 == 'true') and (b2 == 'true'), ident="a"))
            self.assertEqual(expected, actual)

    def test_bool_and_with_wrong_type_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- a and false;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type boolean, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- false and a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type boolean, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- a or false;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type boolean, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- false or a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type boolean, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_bool_not_should_return_correct_value(self):
        for b1 in ["true", "false"]:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                  boolean a <- not {};
                }}
                """.format(b1), actual)
            expected = SymbolTable()
            expected.store("a", Expression(Type.boolean(), not (b1 == 'true'), ident="a"))
            self.assertEqual(expected, actual)

    def test_bool_not_with_wrong_type_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- not a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type boolean, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))


class ComparisonOperationTest(unittest.TestCase):
    def test_greater_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- 1 > -1;
              boolean b <- 1 > -1.0;
              boolean c <- 1.0 > -1;
              boolean d <- 1.0 > -1.0;
              boolean e <- 0 > 0;
              boolean f <- 0.0 > 0.0;
              boolean g <- -1 > 1;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), True, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        expected.store("c", Expression(Type.boolean(), True, ident="c"))
        expected.store("d", Expression(Type.boolean(), True, ident="d"))
        expected.store("e", Expression(Type.boolean(), False, ident="e"))
        expected.store("f", Expression(Type.boolean(), False, ident="f"))
        expected.store("g", Expression(Type.boolean(), False, ident="g"))
        self.assertEqual(expected, actual)

    def test_greater_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- a > 1;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- 1 > a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_greater_equal_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- 1 >= -1;
              boolean b <- 1 >= -1.0;
              boolean c <- 1.0 >= -1;
              boolean d <- 1.0 >= -1.0;
              boolean e <- 0 >= 0;
              boolean f <- 0.0 >= 0.0;
              boolean g <- -1 >= 1;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), True, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        expected.store("c", Expression(Type.boolean(), True, ident="c"))
        expected.store("d", Expression(Type.boolean(), True, ident="d"))
        expected.store("e", Expression(Type.boolean(), True, ident="e"))
        expected.store("f", Expression(Type.boolean(), True, ident="f"))
        expected.store("g", Expression(Type.boolean(), False, ident="g"))
        self.assertEqual(expected, actual)

    def test_greater_equal_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- a >= 1;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- 1 >= a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_less_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- -1 < 1;
              boolean b <- -1 < 1.0;
              boolean c <- -1.0 < 1;
              boolean d <- -1.0 < 1.0;
              boolean e <- 0 < 0;
              boolean f <- 0.0 < 0.0;
              boolean g <- 1 < -1;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), True, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        expected.store("c", Expression(Type.boolean(), True, ident="c"))
        expected.store("d", Expression(Type.boolean(), True, ident="d"))
        expected.store("e", Expression(Type.boolean(), False, ident="e"))
        expected.store("f", Expression(Type.boolean(), False, ident="f"))
        expected.store("g", Expression(Type.boolean(), False, ident="g"))
        self.assertEqual(expected, actual)

    def test_less_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- a < 1;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- 1 < a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_less_equal_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- -1 <= 1;
              boolean b <- -1 <= 1.0;
              boolean c <- -1.0 <= 1;
              boolean d <- -1.0 <= 1.0;
              boolean e <- 0 <= 0;
              boolean f <- 0.0 <= 0.0;
              boolean g <- 1 <= -1;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), True, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        expected.store("c", Expression(Type.boolean(), True, ident="c"))
        expected.store("d", Expression(Type.boolean(), True, ident="d"))
        expected.store("e", Expression(Type.boolean(), True, ident="e"))
        expected.store("f", Expression(Type.boolean(), True, ident="f"))
        expected.store("g", Expression(Type.boolean(), False, ident="g"))
        self.assertEqual(expected, actual)

    def test_less_equal_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- a <= 1;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      boolean b <- 1 <= a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_equal_should_return_correct_value(self):
        types = [Type.int(), Type.decimal(), Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            st = SymbolTable()
            generate_commands("""
                main () {{
                  {} a;
                  {} b;
                  boolean c <- a == b;
                }}
                """.format(type, type), st)
            self.assertEqual(Expression(Type.boolean(), True, ident="c"), st.get_expression("c"))

        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- (1.0, 2.0, -3.0) == (1.0, 2.0, -3.0);
              boolean b <- [1, 2] == [1, 2];
              boolean c <- [[1], [2]] == [[1], [2]];
              boolean d <- [] == [];
              boolean e <- "a" == "a";
              boolean f <- 1 == 2;
              boolean g <- 1.0 == 2.0;
              boolean h <- true == false;
              boolean i <- "a" == "b";
              boolean j <- (5.0, 2.0, -3.0) == (1.0, 2.0, -3.0);
              boolean k <- [5, 2] == [1, 2];
              boolean l <- [[5], [2]] == [[1], [2]];
            }
            """, actual)
        expected = SymbolTable()
        for i in "abcde":
            expected.store(i, Expression(Type.boolean(), True, ident=i))
        for i in "fghijkl":
            expected.store(i, Expression(Type.boolean(), False, ident=i))
        self.assertEqual(expected, actual)

    def test_equal_diff_types_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        main () {{
                          {} a;
                          {} b;
                          boolean c <- a == b;
                        }}
                        """.format(t1, t2))
                self.assertTrue("Expressions {} and {} should have the same type"
                                .format(Expression(t1, t1.default_value, ident="a"),
                                        Expression(t2, t2.default_value, ident="b"))
                                in str(context.exception))

    def test_not_equal_should_return_correct_value(self):
        types = [Type.int(), Type.decimal(), Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            st = SymbolTable()
            generate_commands("""
                main () {{
                  {} a;
                  {} b;
                  boolean c <- a =/= b;
                }}
                """.format(type, type), st)
            self.assertEqual(Expression(Type.boolean(), False, ident="c"), st.get_expression("c"))

        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- (1.0, 2.0, -3.0) =/= (1.0, 2.0, -3.0);
              boolean b <- [1, 2] =/= [1, 2];
              boolean c <- [[1], [2]] =/= [[1], [2]];
              boolean d <- [] =/= [];
              boolean e <- "a" =/= "a";
              boolean f <- 1 =/= 2;
              boolean g <- 1.0 =/= 2.0;
              boolean h <- true =/= false;
              boolean i <- "a" =/= "b";
              boolean j <- (5.0, 2.0, -3.0) =/= (1.0, 2.0, -3.0);
              boolean k <- [5, 2] =/= [1, 2];
              boolean l <- [[5], [2]] =/= [[1], [2]];
            }
            """, actual)
        expected = SymbolTable()
        for i in "abcde":
            expected.store(i, Expression(Type.boolean(), False, ident=i))
        for i in "fghijkl":
            expected.store(i, Expression(Type.boolean(), True, ident=i))
        self.assertEqual(expected, actual)

    def test_not_equal_diff_types_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        main () {{
                          {} a;
                          {} b;
                          boolean c <- a =/= b;
                        }}
                        """.format(t1, t2))
                self.assertTrue("Expressions {} and {} should have the same type"
                                .format(Expression(t1, t1.default_value, ident="a"),
                                        Expression(t2, t2.default_value, ident="b"))
                                in str(context.exception))


class ArithmeticOperationTest(unittest.TestCase):
    def test_plus_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 1 + 1;
              decimal b <- 1 + 1.0;
              decimal c <- 1.0 + 1;
              decimal d <- 1.0 + 1.0;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 2, ident="a"))
        expected.store("b", Expression(Type.decimal(), 2.0, ident="b"))
        expected.store("c", Expression(Type.decimal(), 2.0, ident="c"))
        expected.store("d", Expression(Type.decimal(), 2.0, ident="d"))
        self.assertEqual(expected, actual)

    def test_plus_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- a + 1;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- 1 + a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_minus_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 3 - 1;
              decimal b <- 3 - 1.0;
              decimal c <- 3.0 - 1;
              decimal d <- 3.0 - 1.0;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 2, ident="a"))
        expected.store("b", Expression(Type.decimal(), 2.0, ident="b"))
        expected.store("c", Expression(Type.decimal(), 2.0, ident="c"))
        expected.store("d", Expression(Type.decimal(), 2.0, ident="d"))
        self.assertEqual(expected, actual)

    def test_minus_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- a - 1;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- 1 - a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_multi_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 2 * 1;
              decimal b <- 2 * 1.0;
              decimal c <- 2.0 * 1;
              decimal d <- 2.0 * 1.0;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 2, ident="a"))
        expected.store("b", Expression(Type.decimal(), 2.0, ident="b"))
        expected.store("c", Expression(Type.decimal(), 2.0, ident="c"))
        expected.store("d", Expression(Type.decimal(), 2.0, ident="d"))
        self.assertEqual(expected, actual)

    def test_multi_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- a * 1;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- 1 * a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_divide_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 2 / 1;
              decimal b <- 2 / 1.0;
              decimal c <- 2.0 / 1;
              decimal d <- 2.0 / 1.0;
              int e <- 1 / 2;
              decimal f <- 1 / 2.0;
              decimal g <- 1.0 / 2;
              decimal h <- 1.0 / 2.0;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 2, ident="a"))
        expected.store("b", Expression(Type.decimal(), 2.0, ident="b"))
        expected.store("c", Expression(Type.decimal(), 2.0, ident="c"))
        expected.store("d", Expression(Type.decimal(), 2.0, ident="d"))
        expected.store("e", Expression(Type.int(), 0, ident="e"))
        expected.store("f", Expression(Type.decimal(), 0.5, ident="f"))
        expected.store("g", Expression(Type.decimal(), 0.5, ident="g"))
        expected.store("h", Expression(Type.decimal(), 0.5, ident="h"))
        self.assertEqual(expected, actual)

    def test_divide_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- a / 1;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- 1 / a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_divide_by_zero_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {{
                  int a <- 1 / 0;
                }}
                """.format(type))
        self.assertTrue("Division by zero" in str(context.exception))

        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {{
                  decimal a <- 1.0 / 0.0;
                }}
                """.format(type))
        self.assertTrue("Division by zero" in str(context.exception))

    def test_posit_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- + 1;
              decimal b <- + 1.0;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 1, ident="a"))
        expected.store("b", Expression(Type.decimal(), 1.0, ident="b"))
        self.assertEqual(expected, actual)

    def test_posit_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      {} b <- + a;
                    }}
                    """.format(type, type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_negate_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- - 1;
              decimal b <- - 1.0;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), -1, ident="a"))
        expected.store("b", Expression(Type.decimal(), -1.0, ident="b"))
        self.assertEqual(expected, actual)

    def test_negate_with_wrong_type_should_give_error(self):
        types = [Type.boolean(), Type.string(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      {} b <- - a;
                    }}
                    """.format(type, type))
            self.assertTrue("Expression {} should have type int or decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))


class OtherOperationTest(unittest.TestCase):
    def test_size_of_list_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              list[int] a <- [1, 2];
              int b <- a.size;
              int c <- [1.0].size;
              int d <- [].size;
              int e <- [[], [], []].size;
              int f <- [[[], []], [[], []]].size;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.list_of(Type.int()), [1, 2], ident="a"))
        expected.store("b", Expression(Type.int(), 2, ident="b"))
        expected.store("c", Expression(Type.int(), 1, ident="c"))
        expected.store("d", Expression(Type.int(), 0, ident="d"))
        expected.store("e", Expression(Type.int(), 3, ident="e"))
        expected.store("f", Expression(Type.int(), 2, ident="f"))
        self.assertEqual(expected, actual)

    def test_size_of_wrong_type_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.boolean(), Type.string(), Type.vector()]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      int b <- a.size;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type list, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_concat_of_strings_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              string a <- "a";
              string b <- a & "b";
              string c <- "abc" & "";
              string d <- "" & "abcd";
              string e <- "" & "";
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.string(), "a", ident="a"))
        expected.store("b", Expression(Type.string(), "ab", ident="b"))
        expected.store("c", Expression(Type.string(), "abc", ident="c"))
        expected.store("d", Expression(Type.string(), "abcd", ident="d"))
        expected.store("e", Expression(Type.string(), "", ident="e"))
        self.assertEqual(expected, actual)

    def test_concat_of_wrong_types_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      string b <- a & "";
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type string, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      string b <- "" & a;
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type string, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_parentheses_should_visit_content(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- (1);
              decimal b <- (1.2);
              string c <- ("a");
              boolean d <- (true);
              vector e <- ((1.0, 2.0, (3.0)));
              list[int] f <- ([(1), 2]);
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 1, ident="a"))
        expected.store("b", Expression(Type.decimal(), 1.2, ident="b"))
        expected.store("c", Expression(Type.string(), "a", ident="c"))
        expected.store("d", Expression(Type.boolean(), True, ident="d"))
        expected.store("e", Expression(Type.vector(), [1.0, 2.0, 3.0], ident="e"))
        expected.store("f", Expression(Type.list_of(Type.int()), [1, 2], ident="f"))
        self.assertEqual(expected, actual)


class OperationPrecedenceTest(unittest.TestCase):
    def test_parentheses_higher_than_other(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- (2 + 3) * 4;
              int b <- (2 + 3) / 4;
              int c <- 1 - (2 - 3);
              boolean d <- not (true and false);
              boolean e <- not (false or true);
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 20, ident="a"))
        expected.store("b", Expression(Type.int(), 1, ident="b"))
        expected.store("c", Expression(Type.int(), 2, ident="c"))
        expected.store("d", Expression(Type.boolean(), True, ident="d"))
        expected.store("e", Expression(Type.boolean(), False, ident="e"))
        self.assertEqual(expected, actual)

    def test_negate_higher_than_plus_minus(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- - 2 + 3;
              int b <- - 2 - 3;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 1, ident="a"))
        expected.store("b", Expression(Type.int(), -5, ident="b"))
        self.assertEqual(expected, actual)

    def test_multi_divide_same_precedence(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 2 * 2 / 3;
              int b <- 2 / 2 * 3;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 1, ident="a"))
        expected.store("b", Expression(Type.int(), 3, ident="b"))
        self.assertEqual(expected, actual)

    def test_plus_minus_same_precedence(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 1 - 2 + 3;
              int b <- 1 + 2 - 3;
              int c <- 1 - 2 - 3;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 2, ident="a"))
        expected.store("b", Expression(Type.int(), 0, ident="b"))
        expected.store("c", Expression(Type.int(), -4, ident="c"))
        self.assertEqual(expected, actual)

    def test_multi_divide_higher_than_plus_minus(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 2 + 3 * 4;
              int b <- 2 - 3 * 4;
              int c <- 2 + 3 / 4;
              int d <- 2 - 3 / 4;
              int e <- 3 * 4 + 2;
              int f <- 3 * 4 - 2;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 14, ident="a"))
        expected.store("b", Expression(Type.int(), -10, ident="b"))
        expected.store("c", Expression(Type.int(), 2, ident="c"))
        expected.store("d", Expression(Type.int(), 2, ident="d"))
        expected.store("e", Expression(Type.int(), 14, ident="e"))
        expected.store("f", Expression(Type.int(), 10, ident="f"))
        self.assertEqual(expected, actual)

    def test_arithmetic_higher_than_comparison(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- 2 + 3 == 5;
              boolean b <- 2 * 3 =/= 5;
              boolean c <- 2 - 3 <= 5;
              boolean d <- 2 - 3 < 5;
              boolean e <- 2 / 3 >= 5;
              boolean f <- 2 / 3 > 5;
              boolean g <- 5 == 2 + 3;
              boolean h <- 5 =/= 2 * 3;
              boolean i <- 5 <= 2 - 3;
              boolean j <- 5 < 2 - 3;
              boolean k <- 5 >= 2 / 3;
              boolean l <- 5 > 2 / 3;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), True, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        expected.store("c", Expression(Type.boolean(), True, ident="c"))
        expected.store("d", Expression(Type.boolean(), True, ident="d"))
        expected.store("e", Expression(Type.boolean(), False, ident="e"))
        expected.store("f", Expression(Type.boolean(), False, ident="f"))
        expected.store("g", Expression(Type.boolean(), True, ident="g"))
        expected.store("h", Expression(Type.boolean(), True, ident="h"))
        expected.store("i", Expression(Type.boolean(), False, ident="i"))
        expected.store("j", Expression(Type.boolean(), False, ident="j"))
        expected.store("k", Expression(Type.boolean(), True, ident="k"))
        expected.store("l", Expression(Type.boolean(), True, ident="l"))
        self.assertEqual(expected, actual)

    def test_comparison_higher_than_equality(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- true == 6 > 5;
              boolean b <- true == 6 >= 5;
              boolean c <- true == 6 < 5;
              boolean d <- true == 6 <= 5;
              boolean e <- 6 < 5 =/= true;
              boolean f <- 6 <= 5 =/= true;
              boolean g <- 6 > 5 =/= true;
              boolean h <- 6 >= 5 =/= true;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), True, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        expected.store("c", Expression(Type.boolean(), False, ident="c"))
        expected.store("d", Expression(Type.boolean(), False, ident="d"))
        expected.store("e", Expression(Type.boolean(), True, ident="e"))
        expected.store("f", Expression(Type.boolean(), True, ident="f"))
        expected.store("g", Expression(Type.boolean(), False, ident="g"))
        expected.store("h", Expression(Type.boolean(), False, ident="h"))
        self.assertEqual(expected, actual)

    def test_equality_same_precedence(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- 2 + 3 == 5 == true;
              boolean b <- 2 * 3 =/= 5 =/= false;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), True, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        self.assertEqual(expected, actual)

    def test_comparison_higher_than_bool_operation(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- true and 1 == 1;
              boolean b <- false or 1 == 1;
              boolean c <- 1 == 1 and true;
              boolean d <- 1 == 1 or false;
              boolean e <- true and 1 >= 1;
              boolean f <- false or 1 <= 1;
              boolean g <- 1 > 1 and true;
              boolean h <- 1 < 1 or false;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), True, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        expected.store("c", Expression(Type.boolean(), True, ident="c"))
        expected.store("d", Expression(Type.boolean(), True, ident="d"))
        expected.store("e", Expression(Type.boolean(), True, ident="e"))
        expected.store("f", Expression(Type.boolean(), True, ident="f"))
        expected.store("g", Expression(Type.boolean(), False, ident="g"))
        expected.store("h", Expression(Type.boolean(), False, ident="h"))
        self.assertEqual(expected, actual)

    def test_concat_higher_than_eq_operation(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- "a" & "b" == "ab";
              boolean b <- "ab" == "a" & "b";
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), True, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        self.assertEqual(expected, actual)

    def test_not_higher_than_and_or(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              boolean a <- not true and false;
              boolean b <- not false or true;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.boolean(), False, ident="a"))
        expected.store("b", Expression(Type.boolean(), True, ident="b"))
        self.assertEqual(expected, actual)


class OperationConfusionTest(unittest.TestCase):
    def test_posit_not_confused_with_plus(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 1 + 2;
              int b <- 1+2;
              int c <- +2;
              int d <- 1++2;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), 3, ident="a"))
        expected.store("b", Expression(Type.int(), 3, ident="b"))
        expected.store("c", Expression(Type.int(), 2, ident="c"))
        expected.store("d", Expression(Type.int(), 3, ident="d"))
        self.assertEqual(expected, actual)

    def test_negate_not_confused_with_minus(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              int a <- 1 - 2;
              int b <- 1-2;
              int c <- -2;
              int d <- 1--2;
              int e <- 1---2;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.int(), -1, ident="a"))
        expected.store("b", Expression(Type.int(), -1, ident="b"))
        expected.store("c", Expression(Type.int(), -2, ident="c"))
        expected.store("d", Expression(Type.int(), 3, ident="d"))
        expected.store("e", Expression(Type.int(), -1, ident="e"))
        self.assertEqual(expected, actual)
