# Generated from xDroneParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .xDroneParser import xDroneParser
else:
    from xDroneParser import xDroneParser

# This class defines a complete generic visitor for a parse tree produced by xDroneParser.

class xDroneParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by xDroneParser#prog.
    def visitProg(self, ctx:xDroneParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#commands.
    def visitCommands(self, ctx:xDroneParser.CommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#takeoff.
    def visitTakeoff(self, ctx:xDroneParser.TakeoffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#land.
    def visitLand(self, ctx:xDroneParser.LandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#up.
    def visitUp(self, ctx:xDroneParser.UpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#down.
    def visitDown(self, ctx:xDroneParser.DownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#left.
    def visitLeft(self, ctx:xDroneParser.LeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#right.
    def visitRight(self, ctx:xDroneParser.RightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#forward.
    def visitForward(self, ctx:xDroneParser.ForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#backward.
    def visitBackward(self, ctx:xDroneParser.BackwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#rotateLeft.
    def visitRotateLeft(self, ctx:xDroneParser.RotateLeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#rotateRight.
    def visitRotateRight(self, ctx:xDroneParser.RotateRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#wait.
    def visitWait(self, ctx:xDroneParser.WaitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#declare.
    def visitDeclare(self, ctx:xDroneParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#declareAssign.
    def visitDeclareAssign(self, ctx:xDroneParser.DeclareAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#assignVectorElem.
    def visitAssignVectorElem(self, ctx:xDroneParser.AssignVectorElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#assignListElem.
    def visitAssignListElem(self, ctx:xDroneParser.AssignListElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#assignIdent.
    def visitAssignIdent(self, ctx:xDroneParser.AssignIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#del.
    def visitDel(self, ctx:xDroneParser.DelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#insert.
    def visitInsert(self, ctx:xDroneParser.InsertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#remove.
    def visitRemove(self, ctx:xDroneParser.RemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#procedureCall.
    def visitProcedureCall(self, ctx:xDroneParser.ProcedureCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#if.
    def visitIf(self, ctx:xDroneParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#while.
    def visitWhile(self, ctx:xDroneParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#for.
    def visitFor(self, ctx:xDroneParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#repeat.
    def visitRepeat(self, ctx:xDroneParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#ident.
    def visitIdent(self, ctx:xDroneParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#listElem.
    def visitListElem(self, ctx:xDroneParser.ListElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#vectorX.
    def visitVectorX(self, ctx:xDroneParser.VectorXContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#vectorY.
    def visitVectorY(self, ctx:xDroneParser.VectorYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#vectorZ.
    def visitVectorZ(self, ctx:xDroneParser.VectorZContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#call.
    def visitCall(self, ctx:xDroneParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#argList.
    def visitArgList(self, ctx:xDroneParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#function.
    def visitFunction(self, ctx:xDroneParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#procedure.
    def visitProcedure(self, ctx:xDroneParser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#paramList.
    def visitParamList(self, ctx:xDroneParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#funcCommand.
    def visitFuncCommand(self, ctx:xDroneParser.FuncCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#funcReturn.
    def visitFuncReturn(self, ctx:xDroneParser.FuncReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#intType.
    def visitIntType(self, ctx:xDroneParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#decimalType.
    def visitDecimalType(self, ctx:xDroneParser.DecimalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#stringType.
    def visitStringType(self, ctx:xDroneParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#booleanType.
    def visitBooleanType(self, ctx:xDroneParser.BooleanTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#vectorType.
    def visitVectorType(self, ctx:xDroneParser.VectorTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#listType.
    def visitListType(self, ctx:xDroneParser.ListTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#parentheses.
    def visitParentheses(self, ctx:xDroneParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#plusMinus.
    def visitPlusMinus(self, ctx:xDroneParser.PlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#compare.
    def visitCompare(self, ctx:xDroneParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#intExpr.
    def visitIntExpr(self, ctx:xDroneParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#or.
    def visitOr(self, ctx:xDroneParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#decimalExpr.
    def visitDecimalExpr(self, ctx:xDroneParser.DecimalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#trueExpr.
    def visitTrueExpr(self, ctx:xDroneParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#listElemExpr.
    def visitListElemExpr(self, ctx:xDroneParser.ListElemExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#concat.
    def visitConcat(self, ctx:xDroneParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#list.
    def visitList(self, ctx:xDroneParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#vectorYExpr.
    def visitVectorYExpr(self, ctx:xDroneParser.VectorYExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#stringExpr.
    def visitStringExpr(self, ctx:xDroneParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#identExpr.
    def visitIdentExpr(self, ctx:xDroneParser.IdentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#not.
    def visitNot(self, ctx:xDroneParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#vectorXExpr.
    def visitVectorXExpr(self, ctx:xDroneParser.VectorXExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#size.
    def visitSize(self, ctx:xDroneParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#negate.
    def visitNegate(self, ctx:xDroneParser.NegateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#and.
    def visitAnd(self, ctx:xDroneParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#functionCall.
    def visitFunctionCall(self, ctx:xDroneParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#vectorZExpr.
    def visitVectorZExpr(self, ctx:xDroneParser.VectorZExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#vector.
    def visitVector(self, ctx:xDroneParser.VectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#falseExpr.
    def visitFalseExpr(self, ctx:xDroneParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#multiDivide.
    def visitMultiDivide(self, ctx:xDroneParser.MultiDivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xDroneParser#equality.
    def visitEquality(self, ctx:xDroneParser.EqualityContext):
        return self.visitChildren(ctx)



del xDroneParser