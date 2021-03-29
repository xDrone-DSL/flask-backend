import copy
from typing import Union, Optional

from xdrone.visitors.compiler_utils.type import Type


class Variable:
    def __init__(self, type: Type, value: Union[int, float, str, bool, list], ident: Optional[str] = None):
        self._type = type
        self._value = value
        self._ident = ident

    @property
    def type(self):
        return copy.deepcopy(self._type)

    @property
    def value(self):
        return copy.deepcopy(self._value)

    @property
    def ident(self):
        return copy.deepcopy(self._ident)

    def __str__(self):
        return "Variable: {{ type: {}, value: {}, ident: {} }}".format(self._type, self._value, self._ident)

    def __eq__(self, other):
        if isinstance(other, Variable):
            return other._type == self._type and other._value == self._value and other.ident == self._ident
        return False


class SymbolTable:
    def __init__(self):
        self._symbol_table = {}

    def __str__(self):
        result = "SymbolTable: {\n"
        for ident, variable in self._symbol_table.items():
            result += "  " + ident + " -> " + str(variable) + "\n"
        result += "}"
        return result

    def __eq__(self, other):
        if isinstance(other, SymbolTable):
            return other._symbol_table == self._symbol_table
        return False

    def __contains__(self, ident: str) -> bool:
        return ident in self._symbol_table

    def store(self, ident: str, variable: Variable) -> None:
        assert not self.__contains__(ident), "Variable already in symbol table, please use update() to update it"
        self._symbol_table[ident] = variable

    def update(self, ident: str, value: Union[int, float, str, bool, list]) -> None:
        assert self.__contains__(ident), "Variable not in symbol table, please use store() to store it first"
        old_variable = self._symbol_table[ident]
        self._symbol_table[ident] = Variable(old_variable.type, value, ident=ident)

    def get_variable(self, ident: str) -> Variable:
        assert self.__contains__(ident), "Variable not in symbol table"
        return copy.deepcopy(self._symbol_table[ident])
