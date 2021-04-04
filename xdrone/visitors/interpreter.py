from typing import List, Callable

from antlr.xDroneParser import xDroneParser
from antlr.xDroneParserVisitor import xDroneParserVisitor
from xdrone import NestedCommands
from xdrone.visitors.compiler_utils.command import Command
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.expressions import Identifier, ListElem, VectorElem, Expression, AbstractExpression
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable
from xdrone.visitors.compiler_utils.type import Type, ListType


class Interpreter(xDroneParserVisitor):

    def __init__(self, symbol_table):
        super().__init__()
        self.symbol_table = SymbolTable() if symbol_table is None else symbol_table

    ######## prog ########

    def visitProg(self, ctx: xDroneParser.ProgContext) -> List[NestedCommands]:
        # #TODO visit functions
        commands = self.visit(ctx.commands())
        return commands

    ######## commands ########

    def visitCommands(self, ctx: xDroneParser.CommandsContext) -> List[NestedCommands]:
        commands = [self.visit(c) for c in ctx.command()]
        return commands

    ######## command ########

    def visitTakeoff(self, ctx: xDroneParser.TakeoffContext) -> List[Command]:
        return [Command.takeoff()]

    def visitLand(self, ctx: xDroneParser.LandContext) -> List[Command]:
        return [Command.land()]

    def visitUp(self, ctx: xDroneParser.UpContext) -> List[Command]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.up(expr.value)]

    def visitDown(self, ctx: xDroneParser.DownContext) -> List[Command]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.down(expr.value)]

    def visitLeft(self, ctx: xDroneParser.LeftContext) -> List[Command]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.left(expr.value)]

    def visitRight(self, ctx: xDroneParser.RightContext) -> List[Command]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.right(expr.value)]

    def visitForward(self, ctx: xDroneParser.ForwardContext) -> List[Command]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.forward(expr.value)]

    def visitBackward(self, ctx: xDroneParser.BackwardContext) -> List[Command]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.backward(expr.value)]

    def visitRotateLeft(self, ctx: xDroneParser.RotateLeftContext) -> List[Command]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.rotate_left(expr.value)]

    def visitRotateRight(self, ctx: xDroneParser.RotateRightContext) -> List[Command]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.rotate_right(expr.value)]

    def visitWait(self, ctx: xDroneParser.WaitContext) -> List[Command]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return [Command.wait(expr.value)]

    def visitDeclare(self, ctx: xDroneParser.DeclareContext) -> List[Command]:
        type, identifier = self.visit(ctx.type_()), self.visit(ctx.ident())
        ident = identifier.ident
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        self.symbol_table.store(ident, Expression(type, type.default_value, ident=ident))
        return []

    def visitDeclareAssign(self, ctx: xDroneParser.DeclareAssignContext) -> List[Command]:
        type, identifier, expr = self.visit(ctx.type_()), self.visit(ctx.ident()), self.visit(ctx.expr())
        ident = identifier.ident
        if ident in self.symbol_table:
            raise CompileError("Identifier {} already declared".format(ident))
        if expr.type != type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}"
                               .format(ident, type, expr.type))
        expr_with_ident = Expression(expr.type, expr.value, ident)
        self.symbol_table.store(ident, expr_with_ident)
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

    def visitAssignVectorElem(self, ctx: xDroneParser.AssignVectorElemContext) -> List[Command]:
        vector_elem, expr = self.visit(ctx.vectorElem()), self.visit(ctx.expr())
        ident = vector_elem.ident
        vector = vector_elem.container
        index = vector_elem.index
        if expr.type != Type.decimal():
            raise CompileError("Assigned value {} should have type decimal, but is {}".format(expr, expr.type))
        self._update_nested_ident(ident, expr, index)
        return []

    def visitAssignListElem(self, ctx: xDroneParser.AssignListElemContext) -> List[Command]:
        list_elem, expr = self.visit(ctx.listElem()), self.visit(ctx.expr())
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

    def visitAssignIdent(self, ctx: xDroneParser.AssignIdentContext) -> List[Command]:
        identifier, expr = self.visit(ctx.ident()), self.visit(ctx.expr())
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

    def visitInsert(self, ctx: xDroneParser.InsertContext):
        # TODO
        return self.visitChildren(ctx)

    def visitRemove(self, ctx: xDroneParser.RemoveContext):
        # TODO
        return self.visitChildren(ctx)

    def visitProcedureCall(self, ctx: xDroneParser.ProcedureCallContext):
        # TODO
        return self.visitChildren(ctx)

    def visitIf(self, ctx: xDroneParser.IfContext) -> List[NestedCommands]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.boolean():
            raise CompileError("Expression {} should have type boolean, but is {}".format(expr, expr.type))
        if expr.value:
            return self.visit(ctx.commands(0))
        else:
            if ctx.ELSE():
                return self.visit(ctx.commands(1))
            else:
                return []

    def visitWhile(self, ctx: xDroneParser.WhileContext) -> List[NestedCommands]:
        expr = self.visit(ctx.expr())
        if expr.type != Type.boolean():
            raise CompileError("Expression {} should have type boolean, but is {}".format(expr, expr.type))
        commands = []
        while expr.value:
            commands.append(self.visit(ctx.commands()))
            expr = self.visit(ctx.expr())
        return commands

    def visitFor(self, ctx: xDroneParser.ForContext):
        # TODO
        return self.visitChildren(ctx)

    def visitRepeat(self, ctx: xDroneParser.RepeatContext) -> List[NestedCommands]:
        expr, commands = self.visit(ctx.expr()), self.visit(ctx.commands())
        if expr.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr, expr.type))
        times = expr.value
        return commands * times

    ######## ident ########

    def visitIdent(self, ctx: xDroneParser.IdentContext) -> Identifier:
        ident = ctx.IDENT().getText()
        if ident in self.symbol_table:
            return Identifier(str(ident), self.symbol_table.get_expression(ident))
        return Identifier(str(ident), None)

    ######## list_elem ########

    def visitListElem(self, ctx: xDroneParser.ListElemContext) -> ListElem:
        expr1, expr2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if not isinstance(expr1.type, ListType):
            raise CompileError("Expression {} should have type list, but is {}".format(expr1, expr1.type))
        if expr2.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr2, expr2.type))
        if expr2.value >= len(expr1.value) or expr2.value < 0:
            raise CompileError("List {} has length {}, but has been assessed with out-of-range index {}"
                               .format(expr1.ident, len(expr1.value), expr2.value))
        return ListElem(expr1.ident, expr1, expr2.value)

    ######## vector_elem ########

    def visitVectorX(self, ctx: xDroneParser.VectorXContext) -> VectorElem:
        expr = self.visit(ctx.expr())
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 0)

    def visitVectorY(self, ctx: xDroneParser.VectorYContext) -> VectorElem:
        expr = self.visit(ctx.expr())
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 1)

    def visitVectorZ(self, ctx: xDroneParser.VectorZContext) -> VectorElem:
        expr = self.visit(ctx.expr())
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 2)

    ######## functions ########

    # Visit a parse tree produced by xDroneParser#call.
    def visitCall(self, ctx: xDroneParser.CallContext):
        # TODO
        return self.visitChildren(ctx)

    # Visit a parse tree produced by xDroneParser#argList.
    def visitArgList(self, ctx: xDroneParser.ArgListContext):
        # TODO
        return self.visitChildren(ctx)

    # Visit a parse tree produced by xDroneParser#function.
    def visitFunction(self, ctx: xDroneParser.FunctionContext):
        # TODO
        return self.visitChildren(ctx)

    # Visit a parse tree produced by xDroneParser#procedure.
    def visitProcedure(self, ctx: xDroneParser.ProcedureContext):
        # TODO
        return self.visitChildren(ctx)

    # Visit a parse tree produced by xDroneParser#paramList.
    def visitParamList(self, ctx: xDroneParser.ParamListContext):
        # TODO
        return self.visitChildren(ctx)

    # Visit a parse tree produced by xDroneParser#funcCommand.
    def visitFuncCommand(self, ctx: xDroneParser.FuncCommandContext):
        # TODO
        return self.visitChildren(ctx)

    # Visit a parse tree produced by xDroneParser#funcReturn.
    def visitFuncReturn(self, ctx: xDroneParser.FuncReturnContext):
        # TODO
        return self.visitChildren(ctx)

    ######## type ########

    def visitIntType(self, ctx: xDroneParser.IntTypeContext) -> Type:
        return Type.int()

    def visitDecimalType(self, ctx: xDroneParser.DecimalTypeContext) -> Type:
        return Type.decimal()

    def visitStringType(self, ctx: xDroneParser.StringTypeContext) -> Type:
        return Type.string()

    def visitBooleanType(self, ctx: xDroneParser.BooleanTypeContext) -> Type:
        return Type.boolean()

    def visitVectorType(self, ctx: xDroneParser.VectorTypeContext) -> Type:
        return Type.vector()

    def visitListType(self, ctx: xDroneParser.ListTypeContext) -> Type:
        elem_type = self.visit(ctx.type_())
        return Type.list_of(elem_type)

    ######## expr ########

    def visitIntExpr(self, ctx: xDroneParser.IntExprContext) -> Expression:
        signed_int = ctx.SIGNED_INT().getText()
        return Expression(Type.int(), int(signed_int))

    def visitDecimalExpr(self, ctx: xDroneParser.DecimalExprContext) -> Expression:
        signed_float = ctx.SIGNED_FLOAT().getText()
        return Expression(Type.decimal(), float(signed_float))

    def visitStringExpr(self, ctx: xDroneParser.StringExprContext) -> Expression:
        escaped_string = ctx.ESCAPED_STRING().getText()
        quotation_removed = str(escaped_string)[1:-1]
        return Expression(Type.string(), quotation_removed)

    def visitTrueExpr(self, ctx: xDroneParser.TrueExprContext) -> Expression:
        return Expression(Type.boolean(), True)

    def visitFalseExpr(self, ctx: xDroneParser.FalseExprContext) -> Expression:
        return Expression(Type.boolean(), False)

    def visitIdentExpr(self, ctx: xDroneParser.IdentExprContext) -> Expression:
        identifier = self.visit(ctx.ident())
        if identifier.ident not in self.symbol_table:
            # identifier.expression is None iff child.ident not in self.symbol_table
            raise CompileError("Identifier {} has not been declared".format(identifier.ident))
        return identifier.to_expression()

    def visitListElemExpr(self, ctx: xDroneParser.ListElemExprContext) -> Expression:
        expr1, expr2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if not isinstance(expr1.type, ListType):
            raise CompileError("Expression {} should have type list, but is {}".format(expr1, expr1.type))
        if expr2.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr2, expr2.type))
        if expr2.value >= len(expr1.value) or expr2.value < 0:
            raise CompileError("List {} has length {}, but has been assessed with out-of-range index {}"
                               .format(expr1.ident, len(expr1.value), expr2.value))
        return ListElem(expr1.ident, expr1, expr2.value).to_expression()

    def visitVectorXExpr(self, ctx: xDroneParser.VectorXExprContext) -> Expression:
        expr = self.visit(ctx.expr())
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 0).to_expression()

    def visitVectorYExpr(self, ctx: xDroneParser.VectorYExprContext) -> Expression:
        expr = self.visit(ctx.expr())
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 1).to_expression()

    def visitVectorZExpr(self, ctx: xDroneParser.VectorZExprContext) -> Expression:
        expr = self.visit(ctx.expr())
        if expr.type != Type.vector():
            raise CompileError("Expression {} should have type vector, but is {}".format(expr, expr.type))
        return VectorElem(expr.ident, expr, 2).to_expression()

    def visitList(self, ctx: xDroneParser.ListContext) -> Expression:
        exprs = [self.visit(expr) for expr in ctx.expr()]
        if len(exprs) == 0:
            return Expression(Type.empty_list(), [])
        if not all(e.type == exprs[0].type for e in exprs):
            raise CompileError("Elements in list {} should have the same type".format([str(e) for e in exprs]))
        return Expression(Type.list_of(exprs[0].type), [e.value for e in exprs])

    def visitVector(self, ctx: xDroneParser.VectorContext) -> Expression:
        expr1, expr2, expr3 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.expr(2))
        for expr in [expr1, expr2, expr3]:
            if expr.type != Type.decimal():
                raise CompileError("Expression {} should have type decimal, but is {}".format(expr, expr.type))
        return Expression(Type.vector(), [expr1.value, expr2.value, expr3.value])

    def visitFunctionCall(self, ctx: xDroneParser.FunctionCallContext) -> Expression:
        # TODO
        return self.visitChildren(ctx)

    def visitSize(self, ctx: xDroneParser.SizeContext) -> Expression:
        expr = self.visit(ctx.expr())
        if not isinstance(expr.type, ListType):
            raise CompileError("Expression {} should have type list, but is {}".format(expr, expr.type))
        return Expression(Type.int(), len(expr.value))

    def visitParentheses(self, ctx: xDroneParser.ParenthesesContext) -> Expression:
        expr = self.visit(ctx.expr())
        return expr

    def visitNegate(self, ctx: xDroneParser.NegateContext) -> Expression:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        return Expression(expr.type, -expr.value)

    def visitNot(self, ctx: xDroneParser.NotContext) -> Expression:
        expr = self.visit(ctx.expr())
        if expr.type != Type.boolean():
            raise CompileError("Expression {} should have type boolean, but is {}".format(expr, expr.type))
        return Expression(Type.boolean(), not expr.value)

    def _get_result_type(self, type1: Type, type2: Type):
        assert type1 == Type.int() or type1 == Type.decimal()
        assert type2 == Type.int() or type2 == Type.decimal()
        if type1 == Type.decimal() or type2 == Type.decimal():
            return Type.decimal(), float
        return Type.int(), int

    def visitMultiDivide(self, ctx: xDroneParser.MultiDivideContext) -> Expression:
        expr1, expr2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if expr1.type != Type.int() and expr1.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr1, expr1.type))
        if expr2.type != Type.int() and expr2.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr2, expr2.type))
        result_type, func = self._get_result_type(expr1.type, expr2.type)

        if ctx.MULTI():
            result_value = func(expr1.value * expr2.value)
        else:  # DIV
            if expr2.value == 0:
                raise CompileError("Division by zero")
            result_value = func(expr1.value / expr2.value)
        return Expression(result_type, result_value)

    def visitPlusMinus(self, ctx: xDroneParser.PlusMinusContext) -> Expression:
        expr1, expr2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if expr1.type != Type.int() and expr1.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr1, expr1.type))
        if expr2.type != Type.int() and expr2.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr2, expr2.type))
        result_type, func = self._get_result_type(expr1.type, expr2.type)
        if ctx.PLUS():
            result_value = func(expr1.value + expr2.value)
        else:  # MINUS
            result_value = func(expr1.value - expr2.value)
        return Expression(result_type, result_value)

    def visitConcat(self, ctx: xDroneParser.ConcatContext) -> Expression:
        expr1, expr2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if expr1.type != Type.string():
            raise CompileError("Expression {} should have type string, but is {}".format(expr1, expr1.type))
        if expr2.type != Type.string():
            raise CompileError("Expression {} should have type string, but is {}".format(expr2, expr2.type))
        return Expression(Type.string(), expr1.value + expr2.value)

    def visitCompare(self, ctx: xDroneParser.CompareContext) -> Expression:
        expr1, expr2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if expr1.type != Type.int() and expr1.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr1, expr1.type))
        if expr2.type != Type.int() and expr2.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr2, expr2.type))
        if ctx.GREATER():
            result_value = expr1.value > expr2.value
        elif ctx.GREATER_EQ():
            result_value = expr1.value >= expr2.value
        elif ctx.LESS():
            result_value = expr1.value < expr2.value
        else:  # LESS_EQ
            result_value = expr1.value <= expr2.value
        return Expression(Type.boolean(), result_value)

    def visitEquality(self, ctx: xDroneParser.EqualityContext) -> Expression:
        expr1, expr2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if expr1.type != expr2.type:
            raise CompileError("Expressions {} and {} should have the same type".format(expr1, expr2))
        if ctx.EQ():
            result_value = expr1.value == expr2.value
        else:  # NOT_EQ
            result_value = expr1.value != expr2.value
        return Expression(Type.boolean(), result_value)

    def visitAnd(self, ctx: xDroneParser.AndContext) -> Expression:
        expr1, expr2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if expr1.type != Type.boolean():
            raise CompileError("Expression {} should have type boolean, but is {}".format(expr1, expr1.type))
        if expr2.type != Type.boolean():
            raise CompileError("Expression {} should have type boolean, but is {}".format(expr2, expr2.type))
        return Expression(Type.boolean(), expr1.value and expr2.value)

    def visitOr(self, ctx: xDroneParser.OrContext) -> Expression:
        expr1, expr2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if expr1.type != Type.boolean():
            raise CompileError("Expression {} should have type boolean, but is {}".format(expr1, expr1.type))
        if expr2.type != Type.boolean():
            raise CompileError("Expression {} should have type boolean, but is {}".format(expr2, expr2.type))
        return Expression(Type.boolean(), expr1.value or expr2.value)
