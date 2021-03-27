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
    def list_of(elem_type: Type) -> ListType:
        return ListType(elem_type)

    def __str__(self):
        return self.type_name

    def __eq__(self, other):
        if isinstance(other, Type):
            return other.type_name == self.type_name and other.default_value == self.default_value
        return False


class ListType(Type):
    def __init__(self, elem_type: Type):
        type_name = "list[" + elem_type.type_name + "]"
        super().__init__(type_name, [])
        self.elem_type = elem_type

    def __eq__(self, other):
        if isinstance(other, ListType):
            return other.type_name == self.type_name and other.default_value == self.default_value \
                    and other.elem_type == self.elem_type
        return False
