from typing import List, Optional

from antlr.xDroneParser import xDroneParser
from antlr.xDroneParserVisitor import xDroneParserVisitor
from xdrone.visitors.compiler_utils.command import Command
from xdrone.visitors.compiler_utils.compile_error import CompileError
from xdrone.visitors.compiler_utils.expressions import Identifier, ListElem, VectorElem, Expression
from xdrone.visitors.compiler_utils.functions import FunctionTable, Function, Parameter, FunctionIdentifier
from xdrone.visitors.compiler_utils.symbol_table import SymbolTable
from xdrone.visitors.compiler_utils.type import Type, ListType, EmptyList


class Interpreter(xDroneParserVisitor):

    def __init__(self, symbol_table, function_table):
        super().__init__()
        self.symbol_table = [SymbolTable() if symbol_table is None else symbol_table]
        self.function_table = FunctionTable() if function_table is None else function_table
        self.returned = [False]
        self.returned_value = []
        self.commands = []

    def _get_latest_symbol_table(self):
        return self.symbol_table[-1]

    ######## prog ########

    def visitProg(self, ctx: xDroneParser.ProgContext) -> List[Command]:
        for func in ctx.func():
            self.visit(func)
        self.visit(ctx.commands())
        commands = self.commands
        self.commands = []
        return commands

    ######## commands ########

    def visitCommands(self, ctx: xDroneParser.CommandsContext) -> None:
        for command in ctx.command():
            if self.returned[-1]:
                break
            self.visit(command)

    ######## command ########

    def visitTakeoff(self, ctx: xDroneParser.TakeoffContext) -> None:
        self.commands.append(Command.takeoff())

    def visitLand(self, ctx: xDroneParser.LandContext) -> None:
        self.commands.append(Command.land())

    def visitUp(self, ctx: xDroneParser.UpContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        self.commands.append(Command.up(expr.value))

    def visitDown(self, ctx: xDroneParser.DownContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        self.commands.append(Command.down(expr.value))

    def visitLeft(self, ctx: xDroneParser.LeftContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        self.commands.append(Command.left(expr.value))

    def visitRight(self, ctx: xDroneParser.RightContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        self.commands.append(Command.right(expr.value))

    def visitForward(self, ctx: xDroneParser.ForwardContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        self.commands.append(Command.forward(expr.value))

    def visitBackward(self, ctx: xDroneParser.BackwardContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        self.commands.append(Command.backward(expr.value))

    def visitRotateLeft(self, ctx: xDroneParser.RotateLeftContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        self.commands.append(Command.rotate_left(expr.value))

    def visitRotateRight(self, ctx: xDroneParser.RotateRightContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        self.commands.append(Command.rotate_right(expr.value))

    def visitWait(self, ctx: xDroneParser.WaitContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        self.commands.append(Command.wait(expr.value))

    def visitDeclare(self, ctx: xDroneParser.DeclareContext) -> None:
        type, identifier = self.visit(ctx.type_()), self.visit(ctx.ident())
        ident = identifier.ident
        if ident in self._get_latest_symbol_table():
            raise CompileError("Identifier {} already declared".format(ident))
        self._get_latest_symbol_table().store(ident, Expression(type, type.default_value, ident=ident))

    def visitDeclareAssign(self, ctx: xDroneParser.DeclareAssignContext) -> None:
        type, identifier, expr = self.visit(ctx.type_()), self.visit(ctx.ident()), self.visit(ctx.expr())
        ident = identifier.ident
        if ident in self._get_latest_symbol_table():
            raise CompileError("Identifier {} already declared".format(ident))
        if expr.type != type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}"
                               .format(ident, type, expr.type))
        expr_with_ident = Expression(type, expr.value, ident)
        self._get_latest_symbol_table().store(ident, expr_with_ident)

    def _unfold_nested_list(self, ident: str) -> (str, list, list):
        if "[" in ident:
            tokens = ident.split("[")
            ident = tokens[0]
            indices = [int(token.replace("]", "")) for token in tokens[1:]]
        else:
            indices = []
        assert ident in self._get_latest_symbol_table()
        new_list = self._get_latest_symbol_table().get_expression(ident).value
        inner = new_list
        for i in indices:
            inner = inner[i]
        return ident, new_list, inner

    def _insert_nested_ident(self, ident: Optional[str], expr: Expression, index: int) -> None:
        if ident is not None:
            new_ident, new_list, inner = self._unfold_nested_list(ident)
            inner.insert(index, expr.value)
            self._get_latest_symbol_table().update(new_ident, new_list)

    def _remove_nested_ident(self, ident: Optional[str], index: int) -> None:
        if ident is not None:
            new_ident, new_list, inner = self._unfold_nested_list(ident)
            inner.pop(index)
            self._get_latest_symbol_table().update(new_ident, new_list)

    def _update_nested_ident(self, ident: Optional[str], expr: Expression, index: int) -> None:
        if ident is not None:
            new_ident, new_list, inner = self._unfold_nested_list(ident)
            inner[index] = expr.value
            self._get_latest_symbol_table().update(new_ident, new_list)

    def visitAssignVectorElem(self, ctx: xDroneParser.AssignVectorElemContext) -> None:
        vector_elem, expr = self.visit(ctx.vectorElem()), self.visit(ctx.expr())
        ident = vector_elem.ident
        vector = vector_elem.container
        index = vector_elem.index
        if expr.type != Type.decimal():
            raise CompileError("Assigned value {} should have type decimal, but is {}".format(expr, expr.type))
        self._update_nested_ident(ident, expr, index)

    def visitAssignListElem(self, ctx: xDroneParser.AssignListElemContext) -> None:
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

    def visitAssignIdent(self, ctx: xDroneParser.AssignIdentContext) -> None:
        identifier, expr = self.visit(ctx.ident()), self.visit(ctx.expr())
        ident = identifier.ident
        if ident not in self._get_latest_symbol_table():
            raise CompileError("Identifier {} has not been declared".format(ident))
        assigned_type = expr.type
        declared_type = self._get_latest_symbol_table().get_expression(ident).type
        if assigned_type != declared_type:
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}"
                               .format(ident, declared_type, assigned_type))
        self._get_latest_symbol_table().update(ident, expr.value)

    def visitDel(self, ctx: xDroneParser.DelContext) -> None:
        identifier = self.visit(ctx.ident())
        ident = identifier.ident
        if ident not in self._get_latest_symbol_table():
            raise CompileError("Identifier {} has not been declared".format(ident))
        self._get_latest_symbol_table().delete(ident)

    def visitInsert(self, ctx: xDroneParser.InsertContext) -> None:
        list = self.visit(ctx.expr(0))
        if not isinstance(list.type, ListType):
            raise CompileError("Expression {} should have type list, but is {}".format(list, list.type))
        if ctx.AT():
            index = self.visit(ctx.expr(1))
            value = self.visit(ctx.expr(2))
        else:
            index = Expression(Type.int(), len(list.value))
            value = self.visit(ctx.expr(1))
        if index.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(index, index.type))
        if index.value > len(list.value) or index.value < 0:
            raise CompileError("List {} has length {}, but has been inserted at out-of-range index {}"
                               .format(list, len(list.value), index.value))
        if not isinstance(list.type, EmptyList) and value.type != list.type.elem_type:
            raise CompileError("List {} has been declared as {}, but inserted with element type {}"
                               .format(list, list.type, value.type))
        self._insert_nested_ident(list.ident, value, index.value)

    def visitRemove(self, ctx: xDroneParser.RemoveContext) -> None:
        list = self.visit(ctx.expr(0))
        if not isinstance(list.type, ListType):
            raise CompileError("Expression {} should have type list, but is {}".format(list, list.type))
        if ctx.AT():
            index = self.visit(ctx.expr(1))
        else:
            index = Expression(Type.int(), len(list.value) - 1)
        if index.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(index, index.type))
        if index.value >= len(list.value) or index.value < 0:
            raise CompileError("List {} has length {}, but has been removed at out-of-range index {}"
                               .format(list, len(list.value), index.value))
        self._remove_nested_ident(list.ident, index.value)

    def visitProcedureCall(self, ctx: xDroneParser.ProcedureCallContext) -> None:
        call = self.visit(ctx.call())
        if call is not None:
            raise CompileError("Procedure call should not return any expression, but {} is returned".format(call))
        return call

    def visitIf(self, ctx: xDroneParser.IfContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.boolean():
            raise CompileError("Expression {} should have type boolean, but is {}".format(expr, expr.type))
        if expr.value:
            self.visit(ctx.commands(0))
        else:
            if ctx.ELSE():
                self.visit(ctx.commands(1))

    def visitWhile(self, ctx: xDroneParser.WhileContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.boolean():
            raise CompileError("Expression {} should have type boolean, but is {}".format(expr, expr.type))
        while expr.value:
            self.visit(ctx.commands())
            expr = self.visit(ctx.expr())

    def visitFor(self, ctx: xDroneParser.ForContext) -> None:
        identifier, expr1, expr2 = self.visit(ctx.ident()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        ident = identifier.ident
        if ident not in self._get_latest_symbol_table():
            raise CompileError("Identifier {} has not been declared".format(ident))
        declared_type = self._get_latest_symbol_table().get_expression(ident).type
        if declared_type != Type.int():
            raise CompileError("Identifier {} has been declared as {}, but assigned as {}"
                               .format(ident, declared_type, Type.int()))
        if expr1.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr1, expr1.type))
        if expr2.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr2, expr2.type))

        if ctx.STEP():
            expr3 = self.visit(ctx.expr(2))
            if expr3.type != Type.int():
                raise CompileError("Expression {} should have type int, but is {}".format(expr3, expr3.type))
            step = expr3.value
        else:
            step = 1

        for i in range(expr1.value, expr2.value + 1, step):
            self._get_latest_symbol_table().update(ident, i)
            self.visit(ctx.commands())

    def visitRepeat(self, ctx: xDroneParser.RepeatContext) -> None:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int():
            raise CompileError("Expression {} should have type int, but is {}".format(expr, expr.type))
        times = expr.value

        for _ in range(times):
            self.visit(ctx.commands())

    def visitReturn(self, ctx: xDroneParser.ReturnContext) -> None:
        if len(self.returned) == 1:
            raise CompileError("Cannot return in the Main function")
        self.returned[-1] = True  # order important
        if ctx.expr():
            expr = self.visit(ctx.expr())
            self.returned_value[-1] = Expression(expr.type, expr.value, ident=None)

    ######## ident ########

    def visitIdent(self, ctx: xDroneParser.IdentContext) -> Identifier:
        ident = ctx.IDENT().getText()
        if ident in self._get_latest_symbol_table():
            return Identifier(str(ident), self._get_latest_symbol_table().get_expression(ident))
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
                               .format(expr1, len(expr1.value), expr2.value))
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

    def visitFuncIdent(self, ctx: xDroneParser.FuncIdentContext):
        ident = ctx.IDENT().getText()
        return FunctionIdentifier(str(ident))

    def visitCall(self, ctx: xDroneParser.CallContext) -> Optional[Expression]:
        func_identifier = self.visit(ctx.funcIdent())
        ident = func_identifier.ident
        arg_list = self.visit(ctx.argList()) if ctx.argList() else []
        if ident not in self.function_table:
            raise CompileError("Function or procedure {} has not been defined".format(ident))
        function = self.function_table.get_function(ident)
        arg_types = [arg.type for arg in arg_list]
        param_types = [param.type for param in function.param_list]
        if arg_types != param_types:
            raise CompileError("Arguments when calling function or procedure {} should have types {}, but is {}"
                               .format(ident, [str(type) for type in param_types], [str(type) for type in arg_types]))
        new_symbol_table = SymbolTable()
        param_idents = [param.ident for param in function.param_list]
        for param_ident, expr in zip(param_idents, arg_list):
            new_symbol_table.store(param_ident, expr)

        self.symbol_table.append(new_symbol_table)
        self.returned.append(False)
        self.returned_value.append(None)
        self.visit(function.get_commands())
        returned_value = self.returned_value.pop(-1)
        self.returned.pop(-1)
        self.symbol_table.pop(-1)
        if function.return_type is None:
            if returned_value is not None:
                raise CompileError("Procedure {} should not return anything, but {} is returned"
                                   .format(ident, returned_value))
            return None
        else:
            if returned_value is None:
                raise CompileError("Function {} has returned type {}, but nothing is returned"
                                   .format(ident, function.return_type))
            if returned_value.type != function.return_type:
                raise CompileError("Function {} has returned type {}, but {} is returned"
                                   .format(ident, function.return_type, returned_value.type))
            return returned_value

    def visitArgList(self, ctx: xDroneParser.ArgListContext) -> List[Expression]:
        exprs = [self.visit(expr) for expr in ctx.expr()]
        return exprs

    def visitFunction(self, ctx: xDroneParser.FunctionContext) -> None:
        func_identifier, return_type = self.visit(ctx.funcIdent()), self.visit(ctx.type_())
        ident = func_identifier.ident
        if ident in self.function_table:
            raise CompileError("Function or procedure {} already defined".format(ident))
        param_list = self.visit(ctx.paramList()) if ctx.paramList() else []
        self.function_table.store(ident, Function(ident, param_list, return_type, ctx.commands()))

    def visitProcedure(self, ctx: xDroneParser.ProcedureContext) -> None:
        func_identifier = self.visit(ctx.funcIdent())
        ident = func_identifier.ident
        if ident in self.function_table:
            raise CompileError("Function or procedure {} already defined".format(ident))
        param_list = self.visit(ctx.paramList()) if ctx.paramList() else []
        self.function_table.store(ident, Function(ident, param_list, None, ctx.commands()))

    def visitParamList(self, ctx: xDroneParser.ParamListContext) -> List[Parameter]:
        types = [self.visit(type) for type in ctx.type_()]
        idents = [self.visit(ident).ident for ident in ctx.ident()]
        if len(idents) != len(set(idents)):
            raise CompileError("Parameter names are duplicated in {}".format(idents))
        parameters = []
        for type, ident in zip(types, idents):
            parameters.append(Parameter(ident, type))
        return parameters

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
        signed_int = ctx.INT().getText()
        return Expression(Type.int(), int(signed_int))

    def visitDecimalExpr(self, ctx: xDroneParser.DecimalExprContext) -> Expression:
        signed_float = ctx.FLOAT().getText()
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
        if identifier.ident not in self._get_latest_symbol_table():
            # identifier.expression is None iff child.ident not in latest symbol table
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
                               .format(expr1, len(expr1.value), expr2.value))
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
        call = self.visit(ctx.call())
        if call is None:
            raise CompileError("Function call should return an expression, but nothing is returned")
        return call

    def visitSize(self, ctx: xDroneParser.SizeContext) -> Expression:
        expr = self.visit(ctx.expr())
        if not isinstance(expr.type, ListType):
            raise CompileError("Expression {} should have type list, but is {}".format(expr, expr.type))
        return Expression(Type.int(), len(expr.value))

    def visitParentheses(self, ctx: xDroneParser.ParenthesesContext) -> Expression:
        expr = self.visit(ctx.expr())
        return expr

    def visitPositNegate(self, ctx: xDroneParser.PositNegateContext) -> Expression:
        expr = self.visit(ctx.expr())
        if expr.type != Type.int() and expr.type != Type.decimal():
            raise CompileError("Expression {} should have type int or decimal, but is {}".format(expr, expr.type))
        if ctx.PLUS():
            result_value = +expr.value
        else:  # MINUS
            result_value = -expr.value
        return Expression(expr.type, result_value)

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
