import unittest

from xdrone.visitors.compiler_utils.functions import FunctionIdentifier, Parameter, Function, FunctionTable
from xdrone.visitors.compiler_utils.type import Type


class TestFunctionIdentifier(unittest.TestCase):
    def test_property(self):
        self.assertEqual("a", FunctionIdentifier("a").ident)

    def test_str(self):
        self.assertEqual("FunctionIdentifier: { ident: a }", str(FunctionIdentifier("a")))

    def test_eq(self):
        self.assertEqual(FunctionIdentifier("a"), FunctionIdentifier("a"))
        self.assertNotEqual(FunctionIdentifier("a"), FunctionIdentifier("abc"))
        self.assertNotEqual(FunctionIdentifier("a"), None)


class TestParameter(unittest.TestCase):
    def test_property(self):
        self.assertEqual("a", Parameter("a", Type.int()).ident)
        self.assertEqual(Type.int(), Parameter("a", Type.int()).type)

    def test_str(self):
        self.assertEqual("Parameter: { ident: a, type: int }", str(Parameter("a", Type.int())))

    def test_eq(self):
        self.assertEqual(Parameter("a", Type.int()), Parameter("a", Type.int()))
        self.assertNotEqual(Parameter("a", Type.int()), Parameter("abc", Type.int()))
        self.assertNotEqual(Parameter("a", Type.int()), Parameter("a", Type.list_of(Type.int())))
        self.assertNotEqual(Parameter("a", Type.int()), None)


class TestFunction(unittest.TestCase):
    def test_property(self):
        self.assertEqual("a", Function("a", [], Type.int(), []).ident)
        self.assertEqual([Parameter("a", Type.int())],
                         Function("a", [Parameter("a", Type.int())], Type.int(), []).param_list)
        self.assertEqual(Type.int(), Function("a", [], Type.int(), []).return_type)

    def test_get_commands(self):
        self.assertEqual([], Function("a", [Parameter("a", Type.int())], Type.int(), []).get_commands())

    def test_str(self):
        self.assertEqual("Function: { ident: a, param_list: [], return_type: int }",
                         str(Function("a", [], Type.int(), [])))
        self.assertEqual("Function: { ident: a, param_list: [Parameter: { ident: a, type: int }, "
                         "Parameter: { ident: b, type: string }], "
                         "return_type: None }",
                         str(Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, [])))

    def test_eq(self):
        self.assertEqual(Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []),
                         Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []))
        self.assertNotEqual(Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []),
                            Function("b", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []))
        self.assertNotEqual(Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []),
                            Function("a", [Parameter("a", Type.int())], None, []))
        self.assertNotEqual(Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []),
                            Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], Type.int(), []))
        # Note that `commands` will not be compared
        self.assertEqual(Function("a", [Parameter("a", Type.int())], None, []),
                         Function("a", [Parameter("a", Type.int())], None, ['dummy command']))
        self.assertNotEqual(Function("a", [Parameter("a", Type.int())], None, []),
                            None)


class TestFunctionTable(unittest.TestCase):
    def test_str(self):
        ft = FunctionTable()
        ft.store("a", Function("a", [], None, []))
        expected = "FunctionTable: {\n" \
                   + "  a -> Function: { ident: a, param_list: [], return_type: None }\n" \
                   + "}"
        self.assertEqual(expected, str(ft))

    def test_eq(self):
        ft1 = FunctionTable()
        ft2 = FunctionTable()
        self.assertEqual(ft1, ft2)
        ft1.store("a", Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []))
        self.assertNotEqual(ft1, ft2)
        # Note that `commands` in Function will not be compared
        ft2.store("a", Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, ["dummy"]))
        self.assertEqual(ft1, ft2)

        self.assertNotEqual(FunctionTable(), None)

    def test_contains(self):
        ft = FunctionTable()
        self.assertFalse("a" in ft)
        ft.store("a", Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []))
        self.assertTrue("a" in ft)

    def test_store(self):
        ft = FunctionTable()
        ft.store("a", Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []))
        self.assertTrue("a" in ft)
        self.assertEqual(Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []),
                         ft.get_function("a"))
        self.assertRaises(AssertionError, ft.store, "a",
                          Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []))

    def test_get_function(self):
        ft = FunctionTable()
        self.assertRaises(AssertionError, ft.get_function, "a", )
        ft.store("a", Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []))
        self.assertTrue("a" in ft)
        self.assertEqual(Function("a", [Parameter("a", Type.int()), Parameter("b", Type.string())], None, []),
                         ft.get_function("a"))
