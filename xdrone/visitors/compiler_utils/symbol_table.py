from xdrone.visitors.compiler_utils.type import Type


class Variable:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Variable: {{ type: {}, value: {} }}".format(self.type, self.value)

    def __eq__(self, other):
        if isinstance(other, Variable):
            return other.type == self.type and other.value == self.value
        return False


class SymbolTable:
    def __init__(self):
        self.__symbol_table = {}

    def __contains__(self, ident: str) -> bool:
        return ident in self.__symbol_table

    def store(self, ident: str, type: Type, value: object):
        assert not self.__contains__(ident), "Variable already in symbol table, please use update() to update it"
        self.__symbol_table[ident] = Variable(type, value)

    def update(self, ident: str, value: object):
        assert self.__contains__(ident), "Variable not in symbol table, please use store() to store it first"
        self.__symbol_table[ident].value = value

    def get_type(self, ident: str) -> Type:
        assert self.__contains__(ident), "Variable not in symbol table"
        return self.__symbol_table[ident].type

    def get_value(self, ident: str) -> object:
        assert self.__contains__(ident), "Variable not in symbol table"
        return self.__symbol_table[ident].value
