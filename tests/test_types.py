import unittest

from xdrone.visitors.compiler_utils.type import Type, ArrayType


class TestTypes(unittest.TestCase):
    def test_int(self):
        self.assertEqual(Type.int(), Type.int())
        self.assertEqual("int", Type.int().type_name)
        self.assertEqual(0, Type.int().default_value)
        self.assertEqual("int", str(Type.int()))

    def test_decimal(self):
        self.assertEqual(Type.decimal(), Type.decimal())
        self.assertEqual("decimal", Type.decimal().type_name)
        self.assertEqual(0.0, Type.decimal().default_value)
        self.assertEqual("decimal", str(Type.decimal()))

    def test_string(self):
        self.assertEqual(Type.string(), Type.string())
        self.assertEqual("string", Type.string().type_name)
        self.assertEqual("", Type.string().default_value)
        self.assertEqual("string", str(Type.string()))

    def test_boolean(self):
        self.assertEqual(Type.boolean(), Type.boolean())
        self.assertEqual("boolean", Type.boolean().type_name)
        self.assertEqual(False, Type.boolean().default_value)
        self.assertEqual("boolean", str(Type.boolean()))

    def test_vector(self):
        self.assertEqual(Type.vector(), Type.vector())
        self.assertEqual("vector", Type.vector().type_name)
        self.assertEqual((0, 0, 0), Type.vector().default_value)
        self.assertEqual("vector", str(Type.vector()))

    def test_array_of(self):
        array_type = Type.array_of(Type.int(), 5)
        self.assertEqual(Type.array_of(Type.int(), 5), array_type)
        self.assertNotEqual(Type.array_of(Type.int(), 4), array_type)
        self.assertNotEqual(Type.array_of(Type.decimal(), 5), array_type)
        self.assertEqual(Type("int[5]", [0 for _ in range(5)]), array_type)
        self.assertEqual("int[5]", array_type.type_name)
        self.assertEqual([0 for _ in range(5)], array_type.default_value)
        self.assertEqual(Type.int(), array_type.base_type)
        self.assertEqual((5,), array_type.size)
        self.assertEqual("int[5]", str(array_type))

    def test_nested_array(self):
        inner = Type.array_of(Type.int(), 5)
        outer = Type.array_of(inner, 3)
        self.assertEqual(ArrayType("int[3][5]", [[0 for _ in range(5)] for _ in range(3)], Type.int(), (3, 5)), outer)
        self.assertEqual("int[3][5]", outer.type_name)
        self.assertEqual([[0 for _ in range(5)] for _ in range(3)], outer.default_value)
        self.assertEqual(Type.int(), outer.base_type)
        self.assertEqual((3, 5), outer.size)
        self.assertEqual("int[3][5]", str(outer))

    def test_eq(self):
        types1 = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(),
                  Type.array_of(Type.int(), 5), Type.array_of(Type.decimal(), 5),
                  Type.array_of(Type.array_of(Type.int(), 2), 3), Type.array_of(Type.array_of(Type.int(), 5), 3)]
        types2 = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(),
                  Type.array_of(Type.int(), 5), Type.array_of(Type.decimal(), 5),
                  Type.array_of(Type.array_of(Type.int(), 2), 3), Type.array_of(Type.array_of(Type.int(), 5), 3)]
        for i, j in zip(range(len(types1)), range(len(types2))):
            if i == j:
                self.assertEqual(types1[i], types2[j])
            else:
                self.assertNotEqual(types1[i], types2[j])

    def test_corrupted_type(self):
        int_type = Type.int()
        corrupted_type = Type.int()
        corrupted_type.type_name = "corrupted"
        self.assertNotEqual(int_type, corrupted_type)
        self.assertEqual("int", str(Type.int()))
        self.assertEqual(0, Type.int().default_value)
