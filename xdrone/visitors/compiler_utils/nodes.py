import copy
from typing import Optional

from xdrone.visitors.compiler_utils.symbol_table import Variable
from xdrone.visitors.compiler_utils.type import ListType, Type


class Identifier:
    def __init__(self, ident: str, variable: Optional[Variable]):
        self._ident = ident
        self._variable = variable

    @property
    def ident(self):
        return copy.deepcopy(self._ident)

    def to_variable(self):
        return copy.deepcopy(self._variable)

class ListElem:
    def __init__(self, ident: Optional[str], container: Variable, index: int):
        assert isinstance(container.type, ListType)
        self._ident = ident
        self._container = container
        self._index = index
        self._variable = Variable(container.type.elem_type, container.value[index])

    @property
    def ident(self):
        return copy.deepcopy(self._ident)

    @property
    def container(self):
        return copy.deepcopy(self._container)

    @property
    def index(self):
        return copy.deepcopy(self._index)

    def to_variable(self):
        return copy.deepcopy(self._variable)

class VectorElem:
    def __init__(self, ident: Optional[str], container: Variable, index: int):
        assert container.type == Type.vector()
        self._ident = ident
        self._container = container
        self._index = index
        self._variable = Variable(Type.decimal(), container.value[index])

    @property
    def ident(self):
        return copy.deepcopy(self._ident)

    @property
    def container(self):
        return copy.deepcopy(self._container)

    @property
    def index(self):
        return copy.deepcopy(self._index)

    def to_variable(self):
        return copy.deepcopy(self._variable)
