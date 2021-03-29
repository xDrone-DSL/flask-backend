from lark import Transformer
from math import radians

from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.nodes import Identifier, ListElem, VectorElem
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable, Variable
from xdrone.visitors.compiler_utils.type import Type, ListType


def wrap_command(command, *val):
    return {"action": command, "value": list(val)}

class Simulate(Transformer):

    def __init__(self):
        super().__init__()
        self.symbol_table = SymbolTable()

    # def __default__(self, command, children, meta):
    #     logging.error("Ignoring unsupported command %s with children %s" % (command, children))
    #     raise Discard()

    def prog(self, children):
        return children

    def commands(self, children):
        return children

    def func(self, children):
        # TODO add to table
        return []

    def __process_child(self, child) -> Variable:
        # TODO turn plus minus etc to variable
        if isinstance(child, Identifier) and child.ident not in self.symbol_table:
            raise CompileError("Identifier {} has not been declared".format(child.ident))
        if not isinstance(child, Variable):
            return child.to_variable()
        assert isinstance(child, Variable)
        return child

    def expr(self, children) -> Variable:
        return self.__process_child(children[0])

    def int_expr(self, children) -> Variable:
        return Variable(Type.int(), int(children[0]))

    def decimal_expr(self, children) -> Variable:
        return Variable(Type.decimal(), float(children[0]))

    def string_expr(self, children) -> Variable:
        return Variable(Type.string(), str(children[0]))

    def true_expr(self, children) -> Variable:
        return Variable(Type.boolean(), True)

    def false_expr(self, children) -> Variable:
        return Variable(Type.boolean(), False)

    #TODO test
    def list_elem(self, children) -> ListElem:
        expr1, expr2 = children
        if not isinstance(expr1.type, ListType):
            raise CompileError("Expression {} has type {} is not a list".format(expr1, expr1.type))
        if expr2.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr2, expr2.type))
        return ListElem(expr1, expr2.value)

    def vector_x(self, children) -> VectorElem:
        expr = children[0]
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr, 0)

    def vector_y(self, children) -> VectorElem:
        expr = children[0]
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr, 1)

    def vector_z(self, children) -> VectorElem:
        expr = children[0]
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr, 2)

    def list(self, children) -> Variable:
        exprs = children
        if len(exprs) == 0:
            #TODO: empty list
            pass

        if not all(e.type == exprs[0].type for e in exprs):
            raise CompileError("Elements in list {} should have the same type".format(exprs))
        return Variable(Type.list_of(exprs[0].type), [e.value for e in exprs])

    def vector(self, children) -> Variable:
        expr1, expr2, expr3 = children
        for expr in [expr1, expr2, expr3]:
            if expr.type != Type.decimal():
                raise CompileError("Expression {} should have type decimal, but is {}".format(expr, expr.type))
        return Variable(Type.vector(), [expr1.value, expr2.value, expr3.value])

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

    def ident(self, children) -> Identifier:
        ident = children[0]
        if ident in self.symbol_table:
            return Identifier(str(ident), self.symbol_table.get_variable(ident))
        return Identifier(str(ident), None)

    def declare(self, children):
        type, identifier = children
        ident = identifier.ident
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        self.symbol_table.store(ident, Variable(type, type.default_value))
        return []

    def declare_assign(self, children):
        type, identifier, expr = children
        ident = identifier.ident
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        if expr.type != type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}".format(ident, type, expr.type))
        self.symbol_table.store(ident, expr)
        return []

    def assign_ident(self, children):
        identifier, expr = children
        ident = identifier.ident
        if ident not in self.symbol_table:
            raise CompileError("Identifier {} has not been declared".format(ident))
        assigned_type = expr.type
        declared_type = self.symbol_table.get_variable(ident).type
        if assigned_type != declared_type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}".format(ident, declared_type, assigned_type))
        self.symbol_table.update(ident, expr.value)
        return []

    def assign_list_elem(self, children):
        list_elem, expr = children
        list = list_elem.container
        index = list_elem.index
        assigned_type = expr.type
        declared_type = list.type.elem_type
        if assigned_type != declared_type:
            raise CompileError("Assigned value {} should have type {}, but is {}".format(expr.value, declared_type, assigned_type))
        list.value[index] = expr.value
        return []

    def assign_vector_elem(self, children):
        vector_elem, expr = children
        vector = vector_elem.container
        index = vector_elem.index
        if expr.type != Type.decimal():
            raise CompileError("Assigned value {} should have type decimal, but is {}".format(expr.value, expr.type))
        vector.value[index] = expr.value
        return []


    def takeoff(self, children):
        return wrap_command("takeoff")

    def land(self, children):
        return wrap_command("land")

    def up(self, children):
        expr = children[0]
        return wrap_command("up", expr.value)

    def down(self, children):
        expr = children[0]
        return wrap_command("down", expr.value)

    def left(self, children):
        expr = children[0]
        return wrap_command("left", expr.value)

    def right(self, children):
        expr = children[0]
        return wrap_command("right", expr.value)

    def forward(self, children):
        expr = children[0]
        return wrap_command("forward", expr.value)

    def backward(self, children):
        expr = children[0]
        return wrap_command("backward", expr.value)

    def rotatel(self, children):
        expr, = children
        return wrap_command("rotateL", radians(expr.value))

    def rotater(self, children):
        expr, = children
        return wrap_command("rotateR", radians(expr.value))

    def wait(self, children):
        expr = children[0]
        return wrap_command("wait", expr.value)

    def repeat(self, children):
        expr = children[0]
        times = expr.value
        commands = children[1:]
        return commands * times
