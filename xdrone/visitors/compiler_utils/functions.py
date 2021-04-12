import copy
from typing import List, Optional

from xdrone.visitors.compiler_utils.type import Type


class FunctionIdentifier:
    def __init__(self, ident: str):
        self._ident = ident

    @property
    def ident(self) -> str:
        return copy.deepcopy(self._ident)

    def __str__(self):
        return "FunctionIdentifier: {{ ident: {} }}".format(self._ident)

    def __eq__(self, other):
        if isinstance(other, FunctionIdentifier):
            return other._ident == self._ident
        return False


class Parameter:
    def __init__(self, ident: str, type: Type):
        self._ident = ident
        self._type = type

    @property
    def ident(self) -> str:
        return copy.deepcopy(self._ident)

    @property
    def type(self) -> Type:
        return copy.deepcopy(self._type)

    def __str__(self):
        return "Parameter: {{ ident: {}, type: {} }}".format(self._ident, self._type)

    def __eq__(self, other):
        if isinstance(other, Parameter):
            return other._ident == self._ident and other._type == self._type
        return False


class Function:
    """
    Note that the attribute `commands` is a list of antlr contexts, which is difficult to compare and copy,
    so we do NOT regard the attribute `commands` as a property of a Function object,
    e.g. in __eq__ the attribute `commands` will not be compared,
    in __str__ the attribute `commands` will not be printed
    """
    def __init__(self, ident: str, param_list: List[Parameter], return_type: Optional[Type], commands: list):
        self._ident = ident
        self._param_list = param_list
        self._return_type = return_type
        self._commands = commands

    @property
    def ident(self) -> str:
        return copy.deepcopy(self._ident)

    @property
    def param_list(self) -> List[Parameter]:
        return copy.deepcopy(self._param_list)

    @property
    def return_type(self) -> Type:
        return copy.deepcopy(self._return_type)

    def get_commands(self) -> list:
        # deepcopy will give error, so use shallow copy
        return self._commands

    def __str__(self):
        param_list_str = "[" + ", ".join(map(str, self._param_list)) + "]"
        return "Function: {{ ident: {}, param_list: {}, return_type: {} }}"\
            .format(self._ident, param_list_str, self._return_type)

    def __eq__(self, other):
        if isinstance(other, Function):
            return other._ident == self._ident and other._param_list == self._param_list\
                   and other._return_type == self._return_type
        return False


class FunctionTable:
    def __init__(self):
        self._function_table = {}

    def __str__(self):
        result = "FunctionTable: {\n"
        for ident, function in self._function_table.items():
            result += "  " + ident + " -> " + str(function) + "\n"
        result += "}"
        return result

    def __eq__(self, other):
        if isinstance(other, FunctionTable):
            return other._function_table == self._function_table
        return False

    def __contains__(self, ident: str) -> bool:
        return ident in self._function_table

    def store(self, ident: str, function: Function) -> None:
        assert not self.__contains__(ident), "Function already in function table"
        self._function_table[ident] = function

    def get_function(self, ident: str) -> Function:
        assert self.__contains__(ident), "Function not in symbol table"
        # deepcopy will give error due to `commands` in Function, so use shallow copy
        return self._function_table[ident]
