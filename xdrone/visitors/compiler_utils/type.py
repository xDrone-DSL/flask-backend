from __future__ import annotations

class Type:

    def __init__(self, type_name: str, default_value: object):
        self.type_name = type_name
        self.default_value = default_value

    @staticmethod
    def int() -> Type:
        return Type("int", 0)

    @staticmethod
    def decimal() -> Type:
        return Type("decimal", 0.0)

    @staticmethod
    def string() -> Type:
        return Type("string", "")

    @staticmethod
    def boolean() -> Type:
        return Type("boolean", False)

    @staticmethod
    def vector() -> Type:
        return Type("vector", (0, 0, 0))

    @staticmethod
    def array_of(elem_type: Type, length: int) -> ArrayType:
        if isinstance(elem_type, ArrayType):
            new_size = (length,) + elem_type.size
            base_type = elem_type.base_type
        else:
            new_size = (length,)
            base_type = elem_type

        type_name = base_type.type_name + "".join(map(lambda i: "[{}]".format(i), new_size))
        default_value = [elem_type.default_value for _ in range(length)]
        base_type = base_type
        size = new_size
        return ArrayType(type_name, default_value, base_type, size)

    def __str__(self):
        return self.type_name

    def __eq__(self, other):
        if isinstance(other, Type):
            return other.type_name == self.type_name and other.default_value == self.default_value
        return False


class ArrayType(Type):
    def __init__(self, type_name: str, default_value: object, base_type: Type, size: tuple):
        super().__init__(type_name, default_value)
        self.base_type = base_type
        self.size = size

    def __eq__(self, other):
        if isinstance(other, ArrayType):
            return other.type_name == self.type_name and other.default_value == self.default_value \
                    and other.base_type == self.base_type and other.size == self.size
        return False
