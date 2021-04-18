import unittest

from xdrone import generate_commands, Command
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.expressions import Expression
from xdrone.visitors.compiler_utils.functions import FunctionTable, Function, Parameter
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable
from xdrone.visitors.compiler_utils.type import Type


class FunctionDefinitionTest(unittest.TestCase):
    def test_define_functions_should_change_function_table(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            actual = FunctionTable()
            generate_commands("""
                function func() return {} {{}}
                procedure proc() {{}}
                main () {{}}
                """.format(type), function_table=actual)
            expected = FunctionTable()
            expected.store("func", Function("func", [], type, []))
            expected.store("proc", Function("proc", [], None, []))
            self.assertEqual(expected, actual)

    def test_define_functions_with_parameter_should_change_function_table(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type1 in types:
            for type2 in types:
                actual = FunctionTable()
                generate_commands("""
                    function func({} a, {} b) return int {{}}
                    procedure proc({} a, {} b) {{}}
                    main () {{}}
                    """.format(type1, type2, type1, type2), function_table=actual)
                expected = FunctionTable()
                expected.store("func", Function("func", [Parameter("a", type1), Parameter("b", type2)], Type.int(), []))
                expected.store("proc", Function("proc", [Parameter("a", type1), Parameter("b", type2)], None, []))
                self.assertEqual(expected, actual)

    def test_define_functions_with_duplicated_parameter_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type1 in types:
            for type2 in types:
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        function func({} a, {} a) return int {{}}
                        main () {{}}
                        """.format(type1, type2, type1, type2))
                self.assertTrue("Parameter names are duplicated in ['a', 'a']" in str(context.exception))

                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        procedure proc({} a, {} a) {{}}
                        main () {{}}
                        """.format(type1, type2, type1, type2))
                self.assertTrue("Parameter names are duplicated in ['a', 'a']" in str(context.exception))

    def test_define_existed_function_should_give_error(self):
        lines = ["function func() return int {}", "procedure func() {}"]
        for line1 in lines:
            for line2 in lines:
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        {}
                        {}
                        main () {{}}
                        """.format(line1, line2))

                self.assertTrue("Function or procedure func already defined" in str(context.exception))


class ReturnTest(unittest.TestCase):
    def test_return_correct_type_in_function_should_return_correct_value(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            actual = SymbolTable()
            generate_commands("""
                function func() return {} {{
                  {} a;
                  return a;
                }}
                main () {{
                  {} a <- func();
                }}
                """.format(type, type, type), symbol_table=actual)
            expected = SymbolTable()
            expected.store("a", Expression(type, type.default_value, ident="a"))
            self.assertEqual(expected, actual)

    def test_return_in_function_should_exit_early(self):
        commands = generate_commands("""
            function func() return int {
              return 1;
              up(100);
            }
            main () {
              int a <- func();
            }
            """)
        self.assertEqual([], commands)

    def test_return_wrong_type_in_function_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        function func() return {} {{
                          {} a;
                          return a;
                        }}
                        main () {{
                          {} a <- func();
                        }}
                        """.format(t1, t2, t1))
                self.assertTrue("Function func has returned type {}, but {} is returned"
                                .format(t1, t2)
                                in str(context.exception))

    def test_return_empty_in_function_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    function func() return {} {{
                      return;
                    }}
                    main () {{
                      {} a <- func();
                    }}
                    """.format(type, type))
            self.assertTrue("Function func has returned type {}, but nothing is returned"
                            .format(type)
                            in str(context.exception))

    def test_return_not_exist_in_function_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    function func() return {} {{
                    }}
                    main () {{
                      {} a <- func();
                    }}
                    """.format(type, type))
            self.assertTrue("Function func has returned type {}, but nothing is returned"
                            .format(type)
                            in str(context.exception))

    def test_return_empty_in_procedure_should_exit_early(self):
        commands = generate_commands("""
            procedure proc() {
              return;
              up(100);
            }
            main () {
              proc();
            }
            """)
        self.assertEqual([], commands)

    def test_do_not_return_in_procedure_should_success(self):
        commands = generate_commands("""
            procedure proc() {
            }
            main () {
              proc();
            }
            """)
        self.assertEqual([], commands)

    def test_return_value_in_procedure_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    procedure proc() {{
                      {} a;
                      return a;
                    }}
                    main () {{
                      proc();
                    }}
                    """.format(type))
            self.assertTrue("Procedure proc should not return anything, but {} is returned"
                            .format(Expression(type, type.default_value, ident=None))
                            in str(context.exception))

    def test_return_in_main_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for type in types:
            with self.assertRaises(CompileError) as context:
                generate_commands("""
                    main () {{
                      {} a;
                      return a;
                    }}
                    """.format(type))
            self.assertTrue("Cannot return in the Main function" in str(context.exception))

    def test_return_empty_in_main_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  return;
                }
                """)
        self.assertTrue("Cannot return in the Main function" in str(context.exception))


class ProcedureCallTest(unittest.TestCase):
    def test_call_procedure_should_run_commands(self):
        commands = generate_commands("""
            procedure proc(int i, int j) {
              up(i + j);
              down(i);
            }
            main () {
              takeoff();
              proc(100, 200);
              land();
            }
            """)
        self.assertEqual([Command.takeoff(), Command.up(300), Command.down(100), Command.land()], commands)

    def test_procedure_error_but_not_called_should_not_give_error(self):
        commands = generate_commands("""
            procedure error() {
              int a <- "error";
            }
            main () {
            }
            """)
        self.assertEqual([], commands)

    def test_call_not_defined_procedure_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  proc(100, 200);
                }
                """)
        self.assertTrue("Function or procedure proc has not been defined" in str(context.exception))

    def test_call_procedure_with_wrong_number_argument_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                procedure proc(int i, int j) {
                  up(i + j);
                  down(i);
                }
                main () {
                  takeoff();
                  proc(100);
                  land();
                }
                """)
        self.assertTrue("Arguments when calling function or procedure proc should have types {}, but is {}"
                        .format("['int', 'int']", "['int']")
                        in str(context.exception))

    def test_call_procedure_with_wrong_type_argument_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        procedure proc({} i) {{
                          down(i);
                        }}
                        main () {{
                          takeoff();
                          {} a;
                          proc(a);
                          land();
                        }}
                        """.format(t1, t2))
                self.assertTrue("Arguments when calling function or procedure proc should have types ['{}'], "
                                "but is ['{}']".format(t1, t2)
                                in str(context.exception))

    def test_call_procedure_but_ident_is_function_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                function func() return int {
                  return 1;
                }
                main () {
                  func();
                }
                """)
        self.assertTrue("Procedure call should not return any expression, but {} is returned"
                        .format(Expression(Type.int(), 1, ident=None))
                        in str(context.exception))


class FunctionCallTest(unittest.TestCase):
    def test_call_function_should_run_commands_and_return(self):
        commands = generate_commands("""
            function func(int i, int j) return int {
              up(i + j);
              down(i);
              return i + j;
            }
            main () {
              takeoff();
              forward(func(100, 200));
              land();
            }
            """)
        self.assertEqual([Command.takeoff(), Command.up(300), Command.down(100), Command.forward(300), Command.land()],
                         commands)

    def test_function_error_but_not_called_should_not_give_error(self):
        commands = generate_commands("""
            function func() return int {
              int a <- "error";
            }
            main () {
            }
            """)
        self.assertEqual([], commands)

    def test_call_not_defined_function_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                main () {
                  func(100, 200);
                }
                """)
        self.assertTrue("Function or procedure func has not been defined" in str(context.exception))

    def test_call_function_with_wrong_number_argument_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                function func(int i, int j) return int {
                  return i + j;
                }
                main () {
                  takeoff();
                  forward(func(100));
                  land();
                }
                """)
        self.assertTrue("Arguments when calling function or procedure func should have types {}, but is {}"
                        .format("['int', 'int']", "['int']")
                        in str(context.exception))

    def test_call_function_with_wrong_type_argument_should_give_error(self):
        types = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(), Type.list_of(Type.int()),
                 Type.list_of(Type.decimal()), Type.list_of(Type.list_of(Type.int()))]
        for t1 in types:
            for t2 in types:
                if t1 == t2:
                    continue
                with self.assertRaises(CompileError) as context:
                    generate_commands("""
                        function func({} i) return {} {{
                          return(i);
                        }}
                        main () {{
                          {} a;
                          {} b <- func(a);
                        }}
                        """.format(t1, t1, t2, t1))
                self.assertTrue("Arguments when calling function or procedure func should have types ['{}'], "
                                "but is ['{}']".format(t1, t2)
                                in str(context.exception))

    def test_call_function_but_ident_is_procedure_should_give_error(self):
        with self.assertRaises(CompileError) as context:
            generate_commands("""
                procedure proc() {
                }
                main () {
                  int a <- proc();
                }
                """)
        self.assertTrue("Function call should return an expression, but nothing is returned" in str(context.exception))


class ComplexFunctionTest(unittest.TestCase):
    def test_recursion(self):
        commands = generate_commands("""
            function func(int i) return int {
              if i >= 10 {
                return 10;
              }
              return func(i + 1);
            }
            main () {
              takeoff();
              forward(func(1));
              land();
            }
            """)
        self.assertEqual([Command.takeoff(), Command.forward(10), Command.land()], commands)

    def test_loops_in_function(self):
        commands = generate_commands("""
            function func(int i) return int {
              while i < 10 {
                i <- i + 1;
              }
              return i;
            }
            main () {
              takeoff();
              forward(func(1));
              land();
            }
            """)
        self.assertEqual([Command.takeoff(), Command.forward(10), Command.land()], commands)

    def test_function_procedure_in_function(self):
        commands = generate_commands("""
            function func(int i) return int {
              while i < 10 {
                i <- i + 1;
              }
              return i;
            }
            procedure proc(int i) {
              forward(i * i);
            }
            function func2(int i) return int {
              proc(func(i));
              return func(i) * func(i);
            }
            main () {
              takeoff();
              forward(func2(1));
              land();
            }
            """)
        self.assertEqual([Command.takeoff(), Command.forward(100), Command.forward(100), Command.land()], commands)

    def test_scope(self):
        actual = SymbolTable()
        commands = generate_commands("""
            function func(int i) return int {
              int j <- 100;
              while i < 10 {
                i <- i + 1;
              }
              return i;
            }
            main () {
              takeoff();
              int i <- 1;
              forward(func(i));
              land();
            }
            """, symbol_table=actual)
        self.assertEqual([Command.takeoff(), Command.forward(10), Command.land()], commands)
        expected = SymbolTable()
        expected.store("i", Expression(Type.int(), 1, ident="i"))
        self.assertEqual(expected, actual)


class ComplexProcedureTest(unittest.TestCase):
    def test_recursion(self):
        commands = generate_commands("""
            procedure proc(int i) {
              if i >= 10 {
                forward(10);
                return;
              }
              proc(i + 1);
            }
            main () {
              takeoff();
              proc(1);
              land();
            }
            """)
        self.assertEqual([Command.takeoff(), Command.forward(10), Command.land()], commands)

    def test_loops_in_function(self):
        commands = generate_commands("""
            procedure proc(int i) {
              while i < 10 {
                i <- i + 1;
              }
              forward(i);
            }
            main () {
              takeoff();
              proc(1);
              land();
            }
            """)
        self.assertEqual([Command.takeoff(), Command.forward(10), Command.land()], commands)

    def test_function_procedure_in_procedure(self):
        commands = generate_commands("""
            function func(int i) return int {
              return i * i;
            }
            procedure proc(int i) {
              forward(i);
            }
            procedure proc2() {
              takeoff();
              proc(func(10));
              proc(func(10));
              land();
            }
            main () {
              proc2();
            }
            """)
        self.assertEqual([Command.takeoff(), Command.forward(100), Command.forward(100), Command.land()], commands)

    def test_scope(self):
        actual = SymbolTable()
        generate_commands("""
            procedure proc(int i) {
              int j <- 100;
              while i < 10 {
                i <- i + 1;
              }
            }
            main () {
              int i <- 1;
              proc(i);
            }
            """, symbol_table=actual)
        expected = SymbolTable()
        expected.store("i", Expression(Type.int(), 1, ident="i"))
        self.assertEqual(expected, actual)
