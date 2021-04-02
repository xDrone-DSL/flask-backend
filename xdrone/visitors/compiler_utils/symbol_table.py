import copy
from typing import Union

from xdrone.visitors.compiler_utils.expressions import Expression


class SymbolTable:
    def __init__(self):
        self._symbol_table = {}

    def __str__(self):
        result = "SymbolTable: {\n"
        for ident, expression in self._symbol_table.items():
            result += "  " + ident + " -> " + str(expression) + "\n"
        result += "}"
        return result

    def __eq__(self, other):
        if isinstance(other, SymbolTable):
            return other._symbol_table == self._symbol_table
        return False

    def __contains__(self, ident: str) -> bool:
        return ident in self._symbol_table

    def store(self, ident: str, expression: Expression) -> None:
        assert not self.__contains__(ident), "Expression already in symbol table, please use update() to update it"
        self._symbol_table[ident] = expression

    def update(self, ident: str, value: Union[int, float, str, bool, list]) -> None:
        assert self.__contains__(ident), "Expression not in symbol table, please use store() to store it first"
        old_expression = self._symbol_table[ident]
        self._symbol_table[ident] = Expression(old_expression.type, value, ident=ident)

    def get_expression(self, ident: str) -> Expression:
        assert self.__contains__(ident), "Expression not in symbol table"
        return copy.deepcopy(self._symbol_table[ident])
