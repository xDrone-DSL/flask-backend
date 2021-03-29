from xdrone.visitors.compiler_utils.symbol_table import Variable
from xdrone.visitors.compiler_utils.type import ListType, Type


class Identifier:
    def __init__(self, ident: str, variable: Variable):
        self.ident = ident
        self.variable = variable

    def to_variable(self):
        return self.variable

class ListElem:
    def __init__(self, container: Variable, index: int):
        assert isinstance(container.type, ListType)
        self.container = container
        self.index = index
        self.variable = Variable(container.type.elem_type, container.value[index])

    def to_variable(self):
        return self.variable

class VectorElem:
    def __init__(self, container: Variable, index: int):
        assert container.type == Type.vector()
        self.container = container
        self.index = index
        self.variable = Variable(Type.decimal(), container.value[index])

    def to_variable(self):
        return self.variable
