from typing import List

from lark import Transformer

from xdrone.visitors.compiler_utils.command import Command
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.expressions import Identifier, ListElem, VectorElem, Expression, AbstractExpression
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable
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
        return [Command.takeoff()]

    def land(self, children) -> List[Command]:
        return [Command.land()]

    def up(self, children) -> List[Command]:
        expr, = children
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.up(expr.value)]

    def down(self, children) -> List[Command]:
        expr, = children
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.down(expr.value)]

    def left(self, children) -> List[Command]:
        expr, = children
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.left(expr.value)]

    def right(self, children) -> List[Command]:
        expr, = children
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.right(expr.value)]

    def forward(self, children) -> List[Command]:
        expr, = children
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.forward(expr.value)]

    def backward(self, children) -> List[Command]:
        expr, = children
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.backward(expr.value)]

    def rotate_left(self, children) -> List[Command]:
        expr, = children
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.rotate_left(expr.value)]

    def rotate_right(self, children) -> List[Command]:
        expr, = children
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.rotate_right(expr.value)]

    def wait(self, children) -> List[Command]:
        expr, = children
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.wait(expr.value)]

    def declare(self, children) -> List[Command]:
        type, identifier = children
        ident = identifier.ident
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        self.symbol_table.store(ident, Expression(type, type.default_value, ident=ident))
        return []

    def declare_assign(self, children) -> List[Command]:
        type, identifier, expr = children
        ident = identifier.ident
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        if expr.type != type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}"
                               .format(ident, type, expr.type))
        expr_with_ident = Expression(expr.type, expr.value, ident)
        self.symbol_table.store(ident, expr_with_ident)
        return []

    def assign_ident(self, children) -> List[Command]:
        identifier, expr = children
        ident = identifier.ident
        if ident not in self.symbol_table:
            raise CompileError("Identifier {} has not been declared".format(ident))
        assigned_type = expr.type
        declared_type = self.symbol_table.get_expression(ident).type
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
            new_list = self.symbol_table.get_expression(ident).value
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
                               .format(expr, declared_type, assigned_type))
        self._update_nested_ident(ident, expr, index)
        return []

    def assign_vector_elem(self, children) -> List[Command]:
        vector_elem, expr = children
        ident = vector_elem.ident
        vector = vector_elem.container
        index = vector_elem.index
        if expr.type != Type.decimal():
            raise CompileError("Assigned value {} should have type decimal, but is {}".format(expr, expr.type))
        self._update_nested_ident(ident, expr, index)
        return []

    def repeat(self, children) -> List[Command]:
        expr = children[0]
        commands = children[1:]
        if expr.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr, expr.type))
        times = expr.value
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
        ident = "".join([str(child) for child in children])
        if ident in self.symbol_table:
            return Identifier(str(ident), self.symbol_table.get_expression(ident))
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
        expr, = children
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 0)

    def vector_y(self, children) -> VectorElem:
        expr, = children
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 1)

    def vector_z(self, children) -> VectorElem:
        expr, = children
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
        elem_type, = children
        return Type.list_of(elem_type)

    ######## expr ########

    def expr(self, children) -> Expression:
        child, = children
        assert isinstance(child, AbstractExpression)
        if isinstance(child, Identifier) and child.ident not in self.symbol_table:
            # child.expression is None iff child.ident not in self.symbol_table
            raise CompileError("Identifier {} has not been declared".format(child.ident))
        expr = child.to_expression()
        assert expr is not None and isinstance(expr, Expression)
        return expr

    def int_expr(self, children) -> Expression:
        signed_int, = children
        return Expression(Type.int(), int(signed_int))

    def decimal_expr(self, children) -> Expression:
        signed_float, = children
        return Expression(Type.decimal(), float(signed_float))

    def string_expr(self, children) -> Expression:
        escaped_string, = children
        quotation_removed = str(escaped_string)[1:-1]
        return Expression(Type.string(), quotation_removed)

    def true_expr(self, children) -> Expression:
        return Expression(Type.boolean(), True)

    def false_expr(self, children) -> Expression:
        return Expression(Type.boolean(), False)

    def list(self, children) -> Expression:
        exprs = children
        if len(exprs) == 0:
            return Expression(Type.empty_list(), [])
        if not all(e.type == exprs[0].type for e in exprs):
            raise CompileError("Elements in list {} should have the same type".format(exprs))
        return Expression(Type.list_of(exprs[0].type), [e.value for e in exprs])

    def vector(self, children) -> Expression:
        expr1, expr2, expr3 = children
        for expr in [expr1, expr2, expr3]:
            if expr.type != Type.decimal():
                raise CompileError("Expression {} should have type decimal, but is {}".format(expr, expr.type))
        return Expression(Type.vector(), [expr1.value, expr2.value, expr3.value])
