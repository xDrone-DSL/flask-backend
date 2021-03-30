import unittest

from xdrone.visitors.compiler_utils.expressions import Expression, AbstractExpression, Identifier, ListElem, VectorElem
from xdrone.visitors.compiler_utils.type import Type


class TestAbstractExpression(unittest.TestCase):
    def test_to_expression(self):
        with self.assertRaises(NotImplementedError) as context:
            AbstractExpression().to_expression()


class TestExpression(unittest.TestCase):
    def test_to_expression_should_equal_self(self):
        expressions = [Expression(Type.int(), 1), Expression(Type.decimal(), 1.1), Expression(Type.boolean(), False),
                       Expression(Type.vector(), [1.1, 2.2, -1.1]), Expression(Type.list_of(Type.int()), [1, 2, 3, 4]),
                       Expression(Type.list_of(Type.int()), []),
                       Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0]),
                       Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]]),
                       Expression(Type.int(), 1, "a"), Expression(Type.decimal(), 1.1, "a"),
                       Expression(Type.boolean(), False, "a"),
                       Expression(Type.vector(), [1.1, 2.2, -1.1], "a"),
                       Expression(Type.list_of(Type.int()), [1, 2, 3, 4], "a"),
                       Expression(Type.list_of(Type.int()), [], "a"),
                       Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "a"),
                       Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]], "a")]
        for expression in expressions:
            self.assertEqual(expression, expression.to_expression())

    def test_eq(self):
        expressions1 = [Expression(Type.int(), 1), Expression(Type.decimal(), 1.1), Expression(Type.boolean(), False),
                        Expression(Type.vector(), [1.1, 2.2, -1.1]), Expression(Type.list_of(Type.int()), [1, 2, 3, 4]),
                        Expression(Type.list_of(Type.int()), []),
                        Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0]),
                        Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]]),
                        Expression(Type.int(), 1, "a"), Expression(Type.decimal(), 1.1, "a"),
                        Expression(Type.boolean(), False, "a"),
                        Expression(Type.vector(), [1.1, 2.2, -1.1], "a"),
                        Expression(Type.list_of(Type.int()), [1, 2, 3, 4], "a"),
                        Expression(Type.list_of(Type.int()), [], "a"),
                        Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "a"),
                        Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]], "a")]
        expressions2 = [Expression(Type.int(), 1), Expression(Type.decimal(), 1.1), Expression(Type.boolean(), False),
                        Expression(Type.vector(), [1.1, 2.2, -1.1]), Expression(Type.list_of(Type.int()), [1, 2, 3, 4]),
                        Expression(Type.list_of(Type.int()), []),
                        Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0]),
                        Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]]),
                        Expression(Type.int(), 1, "a"), Expression(Type.decimal(), 1.1, "a"),
                        Expression(Type.boolean(), False, "a"),
                        Expression(Type.vector(), [1.1, 2.2, -1.1], "a"),
                        Expression(Type.list_of(Type.int()), [1, 2, 3, 4], "a"),
                        Expression(Type.list_of(Type.int()), [], "a"),
                        Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "a"),
                        Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]], "a")]
        for i, j in zip(range(len(expressions1)), range(len(expressions2))):
            if i == j:
                self.assertEqual(expressions1[i], expressions2[j])
            else:
                self.assertNotEqual(expressions1[i], expressions2[j])

    def test_str(self):
        self.assertEqual("Expression: { type: int, value: 1, ident: None }", str(Expression(Type.int(), 1)))
        self.assertEqual("Expression: { type: decimal, value: 1.1, ident: None }", str(Expression(Type.decimal(), 1.1)))
        self.assertEqual("Expression: { type: boolean, value: False, ident: None }",
                         str(Expression(Type.boolean(), False)))
        self.assertEqual("Expression: { type: vector, value: [1.1, 2.2, -1.1], ident: None }",
                         str(Expression(Type.vector(), [1.1, 2.2, -1.1])))
        self.assertEqual("Expression: { type: list[int], value: [1, 2, 3, 4], ident: None }",
                         str(Expression(Type.list_of(Type.int()), [1, 2, 3, 4])))
        self.assertEqual("Expression: { type: list[int], value: [], ident: None }",
                         str(Expression(Type.list_of(Type.int()), [])))
        self.assertEqual(
            "Expression: { type: list[list[vector]], value: [[[1.1, 2.2, -1.1], [1, 2, -1]]], ident: None }",
            str(Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]])))

        self.assertEqual("Expression: { type: int, value: 1, ident: a }", str(Expression(Type.int(), 1, "a")))
        self.assertEqual("Expression: { type: decimal, value: 1.1, ident: a }",
                         str(Expression(Type.decimal(), 1.1, "a")))
        self.assertEqual("Expression: { type: boolean, value: False, ident: a }",
                         str(Expression(Type.boolean(), False, "a")))
        self.assertEqual("Expression: { type: vector, value: [1.1, 2.2, -1.1], ident: a }",
                         str(Expression(Type.vector(), [1.1, 2.2, -1.1], "a")))
        self.assertEqual("Expression: { type: list[int], value: [1, 2, 3, 4], ident: a }",
                         str(Expression(Type.list_of(Type.int()), [1, 2, 3, 4], "a")))
        self.assertEqual("Expression: { type: list[int], value: [], ident: a }",
                         str(Expression(Type.list_of(Type.int()), [], "a")))
        self.assertEqual("Expression: { type: list[list[vector]], value: [[[1.1, 2.2, -1.1], [1, 2, -1]]], ident: a }",
                         str(Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]],
                                        "a")))


class TestIdentifier(unittest.TestCase):
    def test_to_expression_should_return_correct_value(self):
        expressions = [None, Expression(Type.int(), 1, "a"), Expression(Type.decimal(), 1.1, "a"),
                       Expression(Type.boolean(), False, "a"),
                       Expression(Type.vector(), [1.1, 2.2, -1.1], "a"),
                       Expression(Type.list_of(Type.int()), [1, 2, 3, 4], "a"),
                       Expression(Type.list_of(Type.int()), [], "a"),
                       Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "a"),
                       Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]], "a")]
        for expression in expressions:
            self.assertEqual(expression, Identifier("a", expression).to_expression())

    def test_eq(self):
        identifiers1 = [Identifier("a", None), Identifier("a", Expression(Type.int(), 1, "a")),
                        Identifier("a", Expression(Type.decimal(), 1.1, "a")),
                        Identifier("b", Expression(Type.int(), 1, "b")),
                        Identifier("b", Expression(Type.list_of(Type.int()), [], "b"))]
        identifiers2 = [Identifier("a", None), Identifier("a", Expression(Type.int(), 1, "a")),
                        Identifier("a", Expression(Type.decimal(), 1.1, "a")),
                        Identifier("b", Expression(Type.int(), 1, "b")),
                        Identifier("b", Expression(Type.list_of(Type.int()), [], "b"))]
        for i, j in zip(range(len(identifiers1)), range(len(identifiers2))):
            if i == j:
                self.assertEqual(identifiers1[i], identifiers2[j])
            else:
                self.assertNotEqual(identifiers1[i], identifiers2[j])

    def test_str(self):
        self.assertEqual("Identifier: { ident: a, expression: None }", str(Identifier("a", None)))
        self.assertEqual("Identifier: { ident: a1, expression: Expression: { type: int, value: 1, ident: a1 } }",
                         str(Identifier("a1", Expression(Type.int(), 1, ident="a1"))))


class TestListElem(unittest.TestCase):
    def test_container_not_list_should_give_error(self):
        none_list_exprs = [Expression(Type.int(), 1, "a"), Expression(Type.decimal(), 1.0, "a"),
                           Expression(Type.boolean(), True, "a"), Expression(Type.string(), "abc", "a"),
                           Expression(Type.vector(), [1.0, 1.0, 1.0], "a")]
        for none_list_expr in none_list_exprs:
            with self.assertRaises(AssertionError) as context:
                ListElem("a", none_list_expr, 0)

    def test_to_expression_should_return_correct_value(self):
        expression = Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "a")
        expected = Expression(Type.decimal(), 1.0, "a[0]")
        self.assertEqual(expected, ListElem("a", expression, 0).to_expression())

        expression = Expression(Type.list_of(Type.list_of(Type.vector())), [[[1.1, 2.2, -1.1], [1, 2, -1]]], "a")
        expected = Expression(Type.list_of(Type.vector()), [[1.1, 2.2, -1.1], [1, 2, -1]], "a[0]")
        self.assertEqual(expected, ListElem("a", expression, 0).to_expression())

        expression = Expression(Type.list_of(Type.boolean()), [True, False], "b[1]")
        expected = Expression(Type.boolean(), False, "b[1][1]")
        self.assertEqual(expected, ListElem("b[1]", expression, 1).to_expression())

    def test_eq(self):
        list_elems1 = [ListElem("a", Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "a"), 0),
                       ListElem("b", Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "b"), 0),
                       ListElem("a", Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0], "a"), 0),
                       ListElem("a", Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "a"), 1),
                       ListElem("a", Expression(Type.list_of(Type.list_of(Type.int())), [[[1], [1]]], "a"), 0),
                       ListElem("b[1]", Expression(Type.list_of(Type.boolean()), [True, False], "b[1]"), 0)]
        list_elems2 = [ListElem("a", Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "a"), 0),
                       ListElem("b", Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "b"), 0),
                       ListElem("a", Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0], "a"), 0),
                       ListElem("a", Expression(Type.list_of(Type.decimal()), [1.0, 2.0, 3.0, 4.0], "a"), 1),
                       ListElem("a", Expression(Type.list_of(Type.list_of(Type.int())), [[[1], [1]]], "a"), 0),
                       ListElem("b[1]", Expression(Type.list_of(Type.boolean()), [True, False], "b[1]"), 0)]
        for i, j in zip(range(len(list_elems1)), range(len(list_elems2))):
            if i == j:
                self.assertEqual(list_elems1[i], list_elems2[j])
            else:
                self.assertNotEqual(list_elems1[i], list_elems2[j])

    def test_str(self):
        self.assertEqual("ListElem: { ident: a, " +
                         "container: Expression: { type: list[int], value: [1, 2, 3, 4], ident: a }, " +
                         "index: 0, expression: Expression: { type: int, value: 1, ident: a[0] } }",
                         str(ListElem("a", Expression(Type.list_of(Type.int()), [1, 2, 3, 4], "a"), 0)))


class TestVectorElem(unittest.TestCase):
    def test_container_not_vector_should_give_error(self):
        none_vector_exprs = [Expression(Type.int(), 1, "a"), Expression(Type.decimal(), 1.0, "a"),
                             Expression(Type.boolean(), True, "a"), Expression(Type.string(), "abc", "a"),
                             Expression(Type.list_of(Type.decimal()), [1.0, 1.0, 1.0], "a"),
                             Expression(Type.list_of(Type.list_of(Type.decimal())), [[1.0, 1.0, 1.0]], "a")]
        for none_vector_expr in none_vector_exprs:
            with self.assertRaises(AssertionError) as context:
                VectorElem("a", none_vector_expr, 0)

    def test_to_expression_should_return_correct_value(self):
        expression = Expression(Type.vector(), [1.0, 2.0, 3.0], "a")
        expected = Expression(Type.decimal(), 1.0)
        self.assertEqual(expected, VectorElem("a", expression, 0).to_expression())

        expression = Expression(Type.vector(), [1.0, 2.0, 3.0], "b[1]")
        expected = Expression(Type.decimal(), 3.0)
        self.assertEqual(expected, VectorElem("b[1]", expression, 2).to_expression())

    def test_eq(self):
        vector_elems1 = [VectorElem("a", Expression(Type.vector(), [1.0, 2.0, 3.0], "a"), 0),
                         VectorElem("b", Expression(Type.vector(), [1.0, 2.0, 3.0], "b"), 0),
                         VectorElem("a", Expression(Type.vector(), [2.0, 2.0, 3.0], "a"), 0),
                         VectorElem("a", Expression(Type.vector(), [1.0, 2.0, 3.0], "a"), 1),
                         VectorElem("b[1]", Expression(Type.vector(), [1.0, 2.0, 3.0], "a"), 0)]
        vector_elems2 = [VectorElem("a", Expression(Type.vector(), [1.0, 2.0, 3.0], "a"), 0),
                         VectorElem("b", Expression(Type.vector(), [1.0, 2.0, 3.0], "b"), 0),
                         VectorElem("a", Expression(Type.vector(), [2.0, 2.0, 3.0], "a"), 0),
                         VectorElem("a", Expression(Type.vector(), [1.0, 2.0, 3.0], "a"), 1),
                         VectorElem("b[1]", Expression(Type.vector(), [1.0, 2.0, 3.0], "a"), 0)]
        for i, j in zip(range(len(vector_elems1)), range(len(vector_elems2))):
            if i == j:
                self.assertEqual(vector_elems1[i], vector_elems2[j])
            else:
                self.assertNotEqual(vector_elems1[i], vector_elems2[j])

    def test_str(self):
        self.assertEqual("ListElem: { ident: a, " +
                         "container: Expression: { type: vector, value: [1.0, 2.0, 3.0], ident: a }, " +
                         "index: 0, expression: Expression: { type: decimal, value: 1.0, ident: None } }",
                         str(VectorElem("a", Expression(Type.vector(), [1.0, 2.0, 3.0], "a"), 0)))
