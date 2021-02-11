from lark import Transformer
from math import radians
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable, Variable
from xdrone.visitors.compiler_utils.type import Type

def wrap_command(command, *val):
    return {"action": command, "value": list(val)}

class CompileError(Exception):
    pass

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
        return Variable(Type.INT, int(children[0]))

    def decimal_expr(self, children):
        return Variable(Type.DECIMAL, float(children[0]))

    def string_expr(self, children):
        return Variable(Type.STRING, str(children[0]))

    def true_expr(self, children):
        return Variable(Type.BOOLEAN, True)

    def false_expr(self, children):
        return Variable(Type.BOOLEAN, False)

    def int_type(self, children):
        return Type.INT

    def decimal_type(self, children):
        return Type.DECIMAL

    def string_type(self, children):
        return Type.STRING

    def boolean_type(self, children):
        return Type.BOOLEAN

    def vector_type(self, children):
        return Type.VECTOR

    def array_type(self, children):
        #TODO
        pass

    def array_declare_type(self, children):
        type, expr = children
        if expr.type != Type.INT:
            raise CompileError("Length of array should have type int, but {} found".format(expr.type))
        return Type.array_of(type, expr.value)

    def ident(self, children):
        ident = children[0]
        return str(ident)

    def declare(self, children):
        type_declare, ident = children
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        self.symbol_table.store(ident, type_declare, type_declare.default_value)
        return []

    def declare_assign(self, children):
        type_declare_assign, ident, assign_rhs = children
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        if assign_rhs.type != type_declare_assign:
            raise CompileError("Identifier {} has declared as {}, but assigned as {}".format(ident, type_declare_assign, assign_rhs.type))
        self.symbol_table.store(ident, type_declare_assign, assign_rhs)
        return []

    def assign(self, children):
        ident, assign_rhs = children
        if ident not in self.symbol_table:
            raise CompileError("Identifier {} has not been declared".format(ident))
        assigned_type = assign_rhs.type
        declared_type = self.symbol_table.get_type(ident)
        if assigned_type != declared_type:
            raise CompileError("Identifier {} has declared as {}, but assigned as {}".format(ident, declared_type, assigned_type))
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
