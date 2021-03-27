from lark import Transformer
from math import radians

from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable, Variable
from xdrone.visitors.compiler_utils.type import Type

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

    def expr(self, children):
        return children

    def int_expr(self, children):
        return Variable(Type.int(), int(children[0]))

    def decimal_expr(self, children):
        return Variable(Type.decimal(), float(children[0]))

    def string_expr(self, children):
        return Variable(Type.string(), str(children[0]))

    def true_expr(self, children):
        return Variable(Type.boolean(), True)

    def false_expr(self, children):
        return Variable(Type.boolean(), False)

    def int_type(self, children):
        return Type.int()

    def decimal_type(self, children):
        return Type.decimal()

    def string_type(self, children):
        return Type.string()

    def boolean_type(self, children):
        return Type.boolean()

    def vector_type(self, children):
        return Type.vector()

    def list_type(self, children):
        elem_type = children[0]
        return Type.list_of(elem_type)

    def ident(self, children):
        ident = children[0]
        return str(ident)

    def declare(self, children):
        type, ident = children
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        self.symbol_table.store(ident, type, type.default_value)
        return []

    def declare_assign(self, children):
        type, ident, assign_rhs = children
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        if assign_rhs.type != type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}".format(ident, type, assign_rhs.type))
        self.symbol_table.store(ident, type, assign_rhs)
        return []

    def assign(self, children):
        #TODO: assign lhs not only ident
        ident, assign_rhs = children
        if ident not in self.symbol_table:
            raise CompileError("Identifier {} has not been declared".format(ident))
        assigned_type = assign_rhs.type
        declared_type = self.symbol_table.get_type(ident)
        if assigned_type != declared_type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}".format(ident, declared_type, assigned_type))
        self.symbol_table.update(ident, assign_rhs.value)
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
