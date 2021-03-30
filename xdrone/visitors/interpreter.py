from typing import List

from lark import Transformer
from math import radians

from xdrone.visitors.compiler_utils.commands import *
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.nodes import Identifier, ListElem, VectorElem
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable, Variable
from xdrone.visitors.compiler_utils.type import Type, ListType


class Interpreter(Transformer):

    def __init__(self, symbol_table):
        super().__init__()
        self.symbol_table = SymbolTable() if symbol_table is None else symbol_table

    # def __default__(self, command, children, meta):
    #     logging.error("Ignoring unsupported command %s with children %s" % (command, children))
    #     raise Discard()

    ######## prog ########

    def prog(self, children):
        return children

    ######## commands ########

    def commands(self, children):
        return children

    ######## command ########

    def takeoff(self, children) -> List[Command]:
        return [Takeoff()]

    def land(self, children) -> List[Command]:
        return [Land()]

    def up(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int() and expr.type != Type.vector():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr.value, expr.type))
        return [Up(expr.value)]

    def down(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int() and expr.type != Type.vector():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr.value, expr.type))
        return [Down(expr.value)]

    def left(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int() and expr.type != Type.vector():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr.value, expr.type))
        return [Left(expr.value)]

    def right(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int() and expr.type != Type.vector():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr.value, expr.type))
        return [Right(expr.value)]

    def forward(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int() and expr.type != Type.vector():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr.value, expr.type))
        return [Forward(expr.value)]

    def backward(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int() and expr.type != Type.vector():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr.value, expr.type))
        return [Backward(expr.value)]

    def rotatel(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int() and expr.type != Type.vector():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr.value, expr.type))
        return [RotateLeft(radians(expr.value))]

    def rotater(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int() and expr.type != Type.vector():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr.value, expr.type))
        return [RotateRight(radians(expr.value))]

    def wait(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int() and expr.type != Type.vector():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr.value, expr.type))
        return [Wait(expr.value)]

    def declare(self, children) -> List[Command]:
        type, identifier = children
        ident = identifier.ident
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        self.symbol_table.store(ident, Variable(type, type.default_value, ident=ident))
        return []

    def declare_assign(self, children) -> List[Command]:
        type, identifier, expr = children
        ident = identifier.ident
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        if expr.type != type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}"
                               .format(ident, type, expr.type))
        expr_with_ident = Variable(expr.type, expr.value, ident)
        self.symbol_table.store(ident, expr_with_ident)
        return []

    def assign_ident(self, children) -> List[Command]:
        identifier, expr = children
        ident = identifier.ident
        if ident not in self.symbol_table:
            raise CompileError("Identifier {} has not been declared".format(ident))
        assigned_type = expr.type
        declared_type = self.symbol_table.get_variable(ident).type
        if assigned_type != declared_type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}"
                               .format(ident, declared_type, assigned_type))
        self.symbol_table.update(ident, expr.value)
        return []

    def _update_nested_ident(self, ident, expr, index) -> None:
        if ident is not None:
            if "[" in ident:
                tokens = ident.split("[")
                ident = tokens[0]
                indices = [int(token.replace("]", "")) for token in tokens[1:]]
            else:
                indices = []
            assert ident in self.symbol_table
            variable = self.symbol_table.get_variable(ident)
            new_list = variable.value
            curr = new_list
            for i in indices:
                curr = curr[i]
            curr[index] = expr.value
            self.symbol_table.update(ident, new_list)

    def assign_list_elem(self, children) -> List[Command]:
        list_elem, expr = children
        ident = list_elem.ident
        list = list_elem.container
        index = list_elem.index
        assigned_type = expr.type
        declared_type = list.type.elem_type
        if assigned_type != declared_type:
            raise CompileError("Assigned value {} should have type {}, but is {}"
                               .format(expr.value, declared_type, assigned_type))
        self._update_nested_ident(ident, expr, index)
        return []

    def assign_vector_elem(self, children) -> List[Command]:
        vector_elem, expr = children
        ident = vector_elem.ident
        vector = vector_elem.container
        index = vector_elem.index
        if expr.type != Type.decimal():
            raise CompileError("Assigned value {} should have type decimal, but is {}".format(expr.value, expr.type))
        self._update_nested_ident(ident, expr, index)
        return []

    def repeat(self, children) -> List[Command]:
        expr = children[0]
        if expr.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr.value, expr.type))
        times = expr.value
        commands = children[1:]
        return commands * times

    ######## func ########
    # TODO

    ######## func_command ########
    # TODO

    ######## param_list ########
    # TODO

    ######## func_call ########
    # TODO

    ######## arg_list ########
    # TODO

    ######## ident ########

    def ident(self, children) -> Identifier:
        ident = children[0]
        if ident in self.symbol_table:
            return Identifier(str(ident), self.symbol_table.get_variable(ident))
        return Identifier(str(ident), None)

    ######## list_elem ########

    def list_elem(self, children) -> ListElem:
        expr1, expr2 = children
        if not isinstance(expr1.type, ListType):
            raise CompileError("Expression {} has type {} is not a list".format(expr1, expr1.type))
        if expr2.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr2, expr2.type))
        if expr2.value >= len(expr1.value):
            raise CompileError("List {} has length {}, but has been assessed with out-of-range index {}"
                               .format(expr1.ident, len(expr1.value), expr2.value))
        return ListElem(expr1.ident, expr1, expr2.value)

    ######## vector_elem ########

    def vector_x(self, children) -> VectorElem:
        expr = children[0]
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 0)

    def vector_y(self, children) -> VectorElem:
        expr = children[0]
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 1)

    def vector_z(self, children) -> VectorElem:
        expr = children[0]
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 2)

    ######## type ########

    def int_type(self, children) -> Type:
        return Type.int()

    def decimal_type(self, children) -> Type:
        return Type.decimal()

    def string_type(self, children) -> Type:
        return Type.string()

    def boolean_type(self, children) -> Type:
        return Type.boolean()

    def vector_type(self, children) -> Type:
        return Type.vector()

    def list_type(self, children) -> Type:
        elem_type = children[0]
        return Type.list_of(elem_type)

    ######## expr ########

    def _process_child(self, child) -> Variable:
        # TODO turn plus minus etc to variable
        if isinstance(child, Identifier) and child.ident not in self.symbol_table:
            raise CompileError("Identifier {} has not been declared".format(child.ident))
        if not isinstance(child, Variable):
            return child.to_variable()
        assert isinstance(child, Variable)
        return child

    def expr(self, children) -> Variable:
        return self._process_child(children[0])

    def int_expr(self, children) -> Variable:
        return Variable(Type.int(), int(children[0]))

    def decimal_expr(self, children) -> Variable:
        return Variable(Type.decimal(), float(children[0]))

    def string_expr(self, children) -> Variable:
        quotation_removed = str(children[0])[1:-1]
        return Variable(Type.string(), quotation_removed)

    def true_expr(self, children) -> Variable:
        return Variable(Type.boolean(), True)

    def false_expr(self, children) -> Variable:
        return Variable(Type.boolean(), False)

    def list(self, children) -> Variable:
        exprs = children
        if len(exprs) == 0:
            return Variable(Type.empty_list(), [])
        if not all(e.type == exprs[0].type for e in exprs):
            raise CompileError("Elements in list {} should have the same type".format(exprs))
        return Variable(Type.list_of(exprs[0].type), [e.value for e in exprs])

    def vector(self, children) -> Variable:
        expr1, expr2, expr3 = children
        for expr in [expr1, expr2, expr3]:
            if expr.type != Type.decimal():
                raise CompileError("Expression {} should have type decimal, but is {}".format(expr, expr.type))
        return Variable(Type.vector(), [expr1.value, expr2.value, expr3.value])
