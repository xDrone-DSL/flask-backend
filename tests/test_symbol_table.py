import unittest

from xdrone.visitors.compiler_utils.symbol_table import Variable, SymbolTable
from xdrone.visitors.compiler_utils.type import Type


class TestVariable(unittest.TestCase):
    def test_eq(self):
        variables1 = [Variable(Type.int(), 1), Variable(Type.decimal(), 1.1), Variable(Type.boolean(), False),
                      Variable(Type.vector(), (1.1, 2.2, -1.1)), Variable(Type.list_of(Type.int()), [1, 2, 3, 4]),
                      Variable(Type.list_of(Type.int()), []), (Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0]),
                      Variable(Type.list_of(Type.list_of(Type.vector())), [[(1.1, 2.2, -1.1), (1, 2, -1)]])]
        variables2 = [Variable(Type.int(), 1), Variable(Type.decimal(), 1.1), Variable(Type.boolean(), False),
                      Variable(Type.vector(), (1.1, 2.2, -1.1)), Variable(Type.list_of(Type.int()), [1, 2, 3, 4]),
                      Variable(Type.list_of(Type.int()), []), (Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0]),
                      Variable(Type.list_of(Type.list_of(Type.vector())), [[(1.1, 2.2, -1.1), (1, 2, -1)]])]
        for i, j in zip(range(len(variables1)), range(len(variables2))):
            if i == j:
                self.assertEqual(variables1[i], variables2[j])
            else:
                self.assertNotEqual(variables1[i], variables2[j])

    def test_str(self):
        self.assertEqual("Variable: { type: int, value: 1 }", str(Variable(Type.int(), 1)))
        self.assertEqual("Variable: { type: decimal, value: 1.1 }", str(Variable(Type.decimal(), 1.1)))
        self.assertEqual("Variable: { type: boolean, value: False }", str(Variable(Type.boolean(), False)))
        self.assertEqual("Variable: { type: vector, value: (1.1, 2.2, -1.1) }", str(Variable(Type.vector(), (1.1, 2.2, -1.1))))
        self.assertEqual("Variable: { type: list[int], value: [1, 2, 3, 4] }",
                         str(Variable(Type.list_of(Type.int()), [1, 2, 3, 4])))
        self.assertEqual("Variable: { type: list[list[vector]], value: [[(1.1, 2.2, -1.1), (1, 2, -1)]] }",
                         str(Variable(Type.list_of(Type.list_of(Type.vector())), [[(1.1, 2.2, -1.1), (1, 2, -1)]])))


class TestSymbolTable(unittest.TestCase):
    def test_contains(self):
        st = SymbolTable()
        self.assertFalse("a" in st)
        st.store("a", Type.int(), 0)
        self.assertTrue("a" in st)

    def test_store(self):
        st = SymbolTable()
        st.store("a", Type.int(), 1)
        self.assertTrue("a" in st)
        self.assertEqual(Type.int(), st.get_type("a"))
        self.assertEqual(1, st.get_value("a"))
        self.assertRaises(AssertionError, st.store, "a", Type.int(), 1)

    def test_update(self):
        st = SymbolTable()
        self.assertRaises(AssertionError, st.update, "a", 1)
        st.store("a", Type.int(), 1)
        st.update("a", 2)
        self.assertEqual(Type.int(), st.get_type("a"))
        self.assertEqual(2, st.get_value("a"))

    def test_get_value(self):
        st = SymbolTable()
        st.store("a", Type.list_of(Type.int()), [1])
        self.assertEqual([1], st.get_value("a"))

    def test_get_type(self):
        st = SymbolTable()
        st.store("a", Type.list_of(Type.int()), [1])
        self.assertEqual(Type.list_of(Type.int()), st.get_type("a"))
