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
                        .format(Expression(Type.list_of(Type.int()), [1, 2], ident="a"), 2, 2)
                        in str(context.exception))

        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {{
                  list[int] a <- [1, 2];
                  a[-1] <- 1;
                }}
                """.format(type))

        self.assertTrue("List {} has length {}, but has been assessed with out-of-range index {}"
                        .format(Expression(Type.list_of(Type.int()), [1, 2], ident="a"), 2, -1)
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
                        .format(Expression(Type.list_of(Type.int()), [1, 2], ident="a"), 2, 2)
                        in str(context.exception))

        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {{
                  list[int] a <- [1, 2];
                  int b <- a[-1];
                }}
                """.format(type))

        self.assertTrue("List {} has length {}, but has been assessed with out-of-range index {}"
                        .format(Expression(Type.list_of(Type.int()), [1, 2], ident="a"), 2, -1)
                        in str(context.exception))


class ListInsertTest(unittest.TestCase):
    def test_list_insert_with_index_should_update_symbol_table(self):
        for index in [0, 1, 2, 3]:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                  list[int] a <- [1, 2, 3];
                  a.at({}).insert(0);
                }}
                """.format(index), actual)
            expected = SymbolTable()
            list = [1, 2, 3]
            list.insert(index, 0)
            expected.store("a", Expression(Type.list_of(Type.int()), list, ident="a"))
            self.assertEqual(expected, actual)

    def test_list_insert_without_index_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              list[int] a <- [1, 2, 3];
              a.insert(0);
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.list_of(Type.int()), [1, 2, 3, 0], ident="a"))
        self.assertEqual(expected, actual)

    def test_list_insert_to_empty_list_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              list[int] a <- [];
              a.insert(0);
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.list_of(Type.int()), [0], ident="a"))
        self.assertEqual(expected, actual)

    def test_list_insert_to_nested_list_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              list[list[int]] a <- [[1], [2], [3]];
              a[0].insert(0);
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.list_of(Type.list_of(Type.int())), [[1, 0], [2], [3]], ident="a"))
        self.assertEqual(expected, actual)

    def test_list_insert_to_temp_list_should_not_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              [1].insert(0);
            }
            """, actual)
        expected = SymbolTable()
        self.assertEqual(expected, actual)

    def test_list_insert_to_temp_empty_list_should_not_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              [].insert(0);
            }
            """, actual)
        expected = SymbolTable()
        self.assertEqual(expected, actual)

    def test_list_insert_with_wrong_type_index_should_give_error(self):
        types = [Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      list[int] b <- [1, 2, 3];
                      b.at(a).insert(0);
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type int, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_list_insert_to_non_list_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector()]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      a.insert(b);
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type list, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_list_insert_with_wrong_type_value_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        main () {{
                          {} a;
                          list[{}] b;
                          b.insert(a);
                        }}
                        """.format(t1, t2))
                self.assertTrue("List {} has been declared as {}, but inserted with element type {}"
                                .format(Expression(Type.list_of(t2), [], ident="b"), Type.list_of(t2), t1)
                                in str(context.exception))

    def test_list_insert_with_out_of_range_index_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  list[int] a <- [1, 2, 3];
                  a.at(-1).insert(0);
                }
                """)
        self.assertTrue("List {} has length {}, but has been inserted at out-of-range index {}"
                        .format(Expression(Type.list_of(Type.int()), [1, 2, 3], ident="a"), 3, -1)
                        in str(context.exception))

        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  list[int] a <- [1, 2, 3];
                  a.at(4).insert(0);
                }
                """)
        self.assertTrue("List {} has length {}, but has been inserted at out-of-range index {}"
                        .format(Expression(Type.list_of(Type.int()), [1, 2, 3], ident="a"), 3, 4)
                        in str(context.exception))


class ListRemoveTest(unittest.TestCase):
    def test_list_remove_with_index_should_update_symbol_table(self):
        for index in [0, 1, 2]:
            actual = SymbolTable()
            generate_commands("""
                main () {{
                  list[int] a <- [1, 2, 3];
                  a.at({}).remove();
                }}
                """.format(index), actual)
            expected = SymbolTable()
            list = [1, 2, 3]
            list.pop(index)
            expected.store("a", Expression(Type.list_of(Type.int()), list, ident="a"))
            self.assertEqual(expected, actual)

    def test_list_remove_without_index_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              list[int] a <- [1, 2, 3];
              a.remove();
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.list_of(Type.int()), [1, 2], ident="a"))
        self.assertEqual(expected, actual)

    def test_list_remove_from_empty_list_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  list[int] a <- [];
                  a.remove();
                }
                """)
        self.assertTrue("List {} has length {}, but has been removed at out-of-range index {}"
                        .format(Expression(Type.list_of(Type.int()), [], ident="a"), 0, -1)
                        in str(context.exception))

    def test_list_remove_from_nested_list_should_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              list[list[int]] a <- [[1], [2], [3]];
              a[0].remove();
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.list_of(Type.list_of(Type.int())), [[], [2], [3]], ident="a"))
        self.assertEqual(expected, actual)

    def test_list_remove_from_temp_list_should_not_update_symbol_table(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              [1].remove();
            }
            """, actual)
        expected = SymbolTable()
        self.assertEqual(expected, actual)

    def test_list_remove_from_temp_empty_list_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  [].remove();
                }
                """)
        self.assertTrue("List {} has length {}, but has been removed at out-of-range index {}"
                        .format(Expression(Type.empty_list(), []), 0, -1)
                        in str(context.exception))

    def test_list_remove_with_wrong_type_index_should_give_error(self):
        types = [Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      list[int] b <- [1, 2, 3];
                      b.at(a).remove();
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type int, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_list_remove_from_non_list_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector()]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      a.remove();
                    }}
                    """.format(type))

            self.assertTrue("Expression {} should have type list, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_list_remove_with_out_of_range_index_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  list[int] a <- [1, 2, 3];
                  a.at(-1).remove();
                }
                """)
        self.assertTrue("List {} has length {}, but has been removed at out-of-range index {}"
                        .format(Expression(Type.list_of(Type.int()), [1, 2, 3], ident="a"), 3, -1)
                        in str(context.exception))

        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  list[int] a <- [1, 2, 3];
                  a.at(3).remove();
                }
                """)
        self.assertTrue("List {} has length {}, but has been removed at out-of-range index {}"
                        .format(Expression(Type.list_of(Type.int()), [1, 2, 3], ident="a"), 3, 3 )
                        in str(context.exception))


class VectorTest(unittest.TestCase):
    def test_vector_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              vector a <- (1.0, 2.0, -3.0);
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.vector(), [1.0, 2.0, -3.0], ident="a"))
        self.assertEqual(expected, actual)

    def test_vector_with_wrong_type_should_give_error(self):
        types = [Type.int(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      vector b <- (a, 2.0, -3.0);
                    }}
                    """.format(type))
            self.assertTrue("Expression {} should have type decimal, but is {}"
                            .format(Expression(type, type.default_value, ident="a"), type.type_name)
                            in str(context.exception))

    def test_vector_elem_assign_should_update_symbol_table_correctly(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              vector a <- (1.0, 2.0, -3.0);
              a.x <- 1.1;
              a.y <- 2.2;
              a.z <- -3.3;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.vector(), [1.1, 2.2, -3.3], ident="a"))
        self.assertEqual(expected, actual)

    def test_vector_elem_assign_with_wrong_ident_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            for index in "xyz":
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        main () {{
                          {} a;
                          a.{} <- 1;
                        }}
                        """.format(type, index))

                self.assertTrue("Expression {} should have type vector, but is {}"
                                .format(Expression(type, type.default_value, ident="a"), type.type_name)
                                in str(context.exception))

    def test_vector_elem_expr_should_return_correct_value(self):
        actual = SymbolTable()
        generate_commands("""
            main () {
              vector a <- (1.0, 2.0, 3.0);
              decimal b <- a.x;
              decimal c <- a.y;
              decimal d <- a.z;
            }
            """, actual)
        expected = SymbolTable()
        expected.store("a", Expression(Type.vector(), [1.0, 2.0, 3.0], ident="a"))
        expected.store("b", Expression(Type.decimal(), 1.0, ident="b"))
        expected.store("c", Expression(Type.decimal(), 2.0, ident="c"))
        expected.store("d", Expression(Type.decimal(), 3.0, ident="d"))
        self.assertEqual(expected, actual)

    def test_list_elem_expr_with_wrong_ident_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            for index in "xyz":
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        main () {{
                          {} a;
                          decimal b <- a.{};
                        }}
                        """.format(type, index))

                self.assertTrue("Expression {} should have type vector, but is {}"
                                .format(Expression(type, type.default_value, ident="a"), type.type_name)
                                in str(context.exception))

