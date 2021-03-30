from __future__ import annotations

import copy
from typing import Optional, Union

from xdrone.visitors.compiler_utils.type import ListType, Type


class AbstractExpression:
    def to_expression(self) -> Optional[Expression]:
        raise NotImplementedError("to_expression not supported in AbstractExpression")


class Expression(AbstractExpression):
    def __init__(self, type: Type, value: Union[int, float, str, bool, list], ident: Optional[str] = None):
        self._type = type
        self._value = value
        self._ident = ident

    @property
    def type(self) -> Type:
        return copy.deepcopy(self._type)

    @property
    def value(self) -> Union[int, float, str, bool, list]:
        return copy.deepcopy(self._value)

    @property
    def ident(self) -> Optional[str]:
        return copy.deepcopy(self._ident)

    def to_expression(self) -> Optional[Expression]:
        return Expression(self._type, self._value, self._ident)

    def __str__(self):
        return "Expression: {{ type: {}, value: {}, ident: {} }}".format(self._type, self._value, self._ident)

    def __eq__(self, other):
        if isinstance(other, Expression):
            return other._type == self._type and other._value == self._value and other.ident == self._ident
        return False


class Identifier(AbstractExpression):
    def __init__(self, ident: str, expression: Optional[Expression]):
        self._ident = ident
        self._expression = expression

    @property
    def ident(self) -> str:
        return copy.deepcopy(self._ident)

    def to_expression(self) -> Optional[Expression]:
        return copy.deepcopy(self._expression)

    def __str__(self):
        return "Identifier: {{ ident: {}, expression: {} }}".format(self._ident, self._expression)

    def __eq__(self, other):
        if isinstance(other, Identifier):
            return other._ident == self._ident and other._expression == self._expression
        return False


class ListElem(AbstractExpression):
    def __init__(self, ident: str, container: Expression, index: int):
        assert isinstance(container.type, ListType)
        self._ident = ident
        self._container = container
        self._index = index
        self._expression = Expression(container.type.elem_type, container.value[index],
                                      ident="{}[{}]".format(ident, index))

    @property
    def ident(self) -> str:
        return copy.deepcopy(self._ident)

    @property
    def container(self) -> Expression:
        return copy.deepcopy(self._container)

    @property
    def index(self) -> int:
        return copy.deepcopy(self._index)

    def to_expression(self) -> Optional[Expression]:
        return copy.deepcopy(self._expression)

    def __str__(self):
        return "ListElem: {{ ident: {}, container: {}, index: {}, expression: {} }}".format(
            self._ident, self._container, self.index, self._expression)

    def __eq__(self, other):
        if isinstance(other, ListElem):
            return other._ident == self._ident and other._container == self._container \
                   and other._index == self._index and other._expression == self._expression
        return False


class VectorElem(AbstractExpression):
    def __init__(self, ident: str, container: Expression, index: int):
        assert container.type == Type.vector()
        self._ident = ident
        self._container = container
        self._index = index
        self._expression = Expression(Type.decimal(), container.value[index])

    @property
    def ident(self) -> str:
        return copy.deepcopy(self._ident)

    @property
    def container(self) -> Expression:
        return copy.deepcopy(self._container)

    @property
    def index(self) -> int:
        return copy.deepcopy(self._index)

    def to_expression(self) -> Optional[Expression]:
        return copy.deepcopy(self._expression)

    def __str__(self):
        return "ListElem: {{ ident: {}, container: {}, index: {}, expression: {} }}".format(
            self._ident, self._container, self.index, self._expression)

    def __eq__(self, other):
        if isinstance(other, VectorElem):
            return other._ident == self._ident and other._container == self._container \
                   and other._index == self._index and other._expression == self._expression
        return False
