import unittest

from xdrone.visitors.compiler_utils.type import Type, ListType, EmptyList


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
        self.assertEqual([0, 0, 0], Type.vector().default_value)
        self.assertEqual("vector", str(Type.vector()))

    def test_list(self):
        list_type = Type.list_of(Type.int())
        self.assertEqual(Type.list_of(Type.int()), list_type)
        self.assertEqual(ListType(Type.int()), list_type)
        self.assertEqual("list[int]", list_type.type_name)
        self.assertEqual([], list_type.default_value)
        self.assertEqual(Type.int(), list_type.elem_type)
        self.assertEqual("list[int]", str(list_type))

    def test_nested_list(self):
        inner = Type.list_of(Type.int())
        outer = Type.list_of(inner)
        self.assertEqual(ListType(Type.list_of(Type.int())), outer)
        self.assertEqual("list[list[int]]", outer.type_name)
        self.assertEqual([], outer.default_value)
        self.assertEqual(Type.list_of(Type.int()), outer.elem_type)
        self.assertEqual("list[list[int]]", str(outer))

    def test_empty_list(self):
        empty_list = Type.empty_list()
        self.assertEqual(Type.empty_list(), empty_list)
        self.assertEqual(EmptyList(), empty_list)
        self.assertEqual("list[]", empty_list.type_name)
        self.assertEqual([], empty_list.default_value)
        self.assertEqual(Type("all", 0), empty_list.elem_type)
        self.assertEqual("list[]", str(empty_list))

    def test_eq(self):
        types1 = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(),
                  Type.list_of(Type.int()), Type.list_of(Type.decimal()),
                  Type.list_of(Type.list_of(Type.int())), Type.list_of(Type.list_of(Type.decimal()))]
        types2 = [Type.int(), Type.decimal(), Type.string(), Type.boolean(), Type.vector(),
                  Type.list_of(Type.int()), Type.list_of(Type.decimal()),
                  Type.list_of(Type.list_of(Type.int())), Type.list_of(Type.list_of(Type.decimal()))]
        for i, j in zip(range(len(types1)), range(len(types2))):
            if i == j:
                self.assertEqual(types1[i], types2[j])
            else:
                self.assertNotEqual(types1[i], types2[j])

        self.assertEqual(Type.empty_list(), Type.empty_list())
        for type in types1:
            if isinstance(type, ListType):
                self.assertEqual(Type.empty_list(), type)
                self.assertEqual(type, Type.empty_list())
            else:
                self.assertNotEqual(Type.empty_list(), type)
                self.assertNotEqual(type, Type.empty_list())

    def test_corrupted_type_not_equal_to_list_type(self):
        self.assertNotEqual(Type("list[int]", []), Type.list_of(Type.int()))
        self.assertNotEqual(Type("list[int]", []), ListType(Type.int()))

    def test_corrupted_type_not_affect_correct_type(self):
        int_type = Type.int()
        corrupted_type = Type.int()
        corrupted_type._type_name = "corrupted"
        self.assertNotEqual(int_type, corrupted_type)
        self.assertEqual("int", str(Type.int()))
        self.assertEqual(0, Type.int().default_value)
        self.assertEqual("corrupted", str(corrupted_type))
        self.assertEqual(0, corrupted_type.default_value)
