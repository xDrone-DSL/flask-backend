import unittest

from xdrone.visitors.compiler_utils.symbol_table import SymbolTable
from xdrone.visitors.compiler_utils.expressions import Expression
from xdrone.visitors.compiler_utils.type import Type


class TestSymbolTable(unittest.TestCase):
    def test_contains(self):
        st = SymbolTable()
        self.assertFalse("a" in st)
        st.store("a", Expression(Type.int(), 0))
        self.assertTrue("a" in st)

    def test_eq(self):
        st1 = SymbolTable()
        st2 = SymbolTable()
        self.assertTrue(st1 == st2)
        st1.store("a", Expression(Type.int(), 0))
        self.assertFalse(st1 == st2)
        st2.store("a", Expression(Type.int(), 0))
        self.assertTrue(st1 == st2)

        self.assertNotEqual(SymbolTable(), None)

    def test_str(self):
        st = SymbolTable()
        st.store("a", Expression(Type.int(), 0))
        st.store("b", Expression(Type.list_of(Type.boolean()), [True]))
        expected = "SymbolTable: {\n" + \
            "  a -> Expression: { type: int, value: 0, ident: None }\n" + \
            "  b -> Expression: { type: list[boolean], value: [True], ident: None }\n" + \
            "}"
        self.assertEqual(expected, str(st))

    def test_store(self):
        st = SymbolTable()
        st.store("a", Expression(Type.int(), 1))
        self.assertTrue("a" in st)
        self.assertEqual(Type.int(), st.get_expression("a").type)
        self.assertEqual(1, st.get_expression("a").value)
        self.assertRaises(AssertionError, st.store, "a", Expression(Type.int(), 1))

    def test_update(self):
        st = SymbolTable()
        self.assertRaises(AssertionError, st.update, "a", 1)
        st.store("a", Expression(Type.int(), 1))
        st.update("a", 2)
        self.assertEqual(Type.int(), st.get_expression("a").type)
        self.assertEqual(2, st.get_expression("a").value)

    def test_delete(self):
        st = SymbolTable()
        st.store("a", Expression(Type.int(), 1))
        self.assertTrue("a" in st)
        st.delete("a")
        self.assertFalse("a" in st)

    def test_get_expression(self):
        st = SymbolTable()
        self.assertRaises(AssertionError, st.get_expression, "a")
        st.store("a", Expression(Type.list_of(Type.int()), [1]))
        self.assertEqual([1], st.get_expression("a").value)
        self.assertEqual(1, st.get_expression("a").value[0])
        self.assertEqual(Type.list_of(Type.int()), st.get_expression("a").type)
