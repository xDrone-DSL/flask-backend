parser grammar xDroneParser;

options {
  tokenVocab=xDroneLexer;
}

prog : func* MAIN L_PAR R_PAR L_BRACE commands R_BRACE ;

commands : command* ;

command
  : TAKEOFF L_PAR R_PAR SEMICOLON                                           #takeoff
  | LAND L_PAR R_PAR SEMICOLON                                              #land
  | UP L_PAR expr R_PAR SEMICOLON                                           #up
  | DOWN L_PAR expr R_PAR SEMICOLON                                         #down
  | LEFT L_PAR expr R_PAR SEMICOLON                                         #left
  | RIGHT L_PAR expr R_PAR SEMICOLON                                        #right
  | FORWARD L_PAR expr R_PAR SEMICOLON                                      #forward
  | BACKWARD L_PAR expr R_PAR SEMICOLON                                     #backward
  | ROTATE_LEFT L_PAR expr R_PAR SEMICOLON                                  #rotateLeft
  | ROTATE_RIGHT L_PAR expr R_PAR SEMICOLON                                 #rotateRight
  | WAIT L_PAR expr R_PAR SEMICOLON                                         #wait
  | type_ ident SEMICOLON                                                   #declare
  | type_ ident ARROW expr SEMICOLON                                        #declareAssign
  | vectorElem ARROW expr SEMICOLON                                         #assignVectorElem
  | listElem ARROW expr SEMICOLON                                           #assignListElem
  | ident ARROW expr SEMICOLON                                              #assignIdent
  | expr (DOT AT L_PAR expr R_PAR)? DOT INSERT L_PAR expr R_PAR SEMICOLON   #insert
  | expr (DOT AT L_PAR expr R_PAR)? DOT REMOVE L_PAR R_PAR SEMICOLON        #remove
  | call                                                                    #precdureCall
  | IF expr L_BRACE commands R_BRACE (ELSE L_BRACE commands R_BRACE)?       #if
  | WHILE expr L_BRACE commands R_BRACE                                     #while
  | FOR ident FROM expr TO expr L_BRACE commands R_BRACE                    #for
  | REPEAT expr TIMES L_BRACE commands R_BRACE                              #repeat
  ;

ident : IDENT ;

listElem: expr L_BRACKET expr R_BRACKET ;

vectorElem
  : expr DOT VEC_X                                                          #vectorX
  | expr DOT VEC_Y                                                          #vectorY
  | expr DOT VEC_Z                                                          #vectorZ
  ;

call : ident L_PAR (argList)? R_PAR SEMICOLON ;

argList: expr (COMMA expr)* ;

func
  : FUNCTION ident L_PAR (paramList)? R_PAR RETURN type_ L_BRACE (funcCommand)* R_BRACE      #function
  | FUNCTION ident L_PAR (paramList)? R_PAR L_BRACE commands R_BRACE                         #procedure
  ;
paramList: type_ ident (COMMA type_ ident)* ;

funcCommand
  : command
  | funcReturn
  ;
funcReturn : RETURN expr SEMICOLON ;


type_
  : TYPE_INT                                   #intType
  | TYPE_DECIMAL                               #decimalType
  | TYPE_STRING                                #stringType
  | TYPE_BOOLEAN                               #booleanType
  | TYPE_VECTOR                                #vectorType
  | TYPE_LIST L_BRACKET type_ R_BRACKET        #listType
  ;

expr
  : SIGNED_INT                                              #intExpr
  | SIGNED_FLOAT                                            #decimalExpr
  | ESCAPED_STRING                                          #stringExpr
  | TRUE                                                    #trueExpr
  | FALSE                                                   #falseExpr
  | ident                                                   #identExpr
  | expr L_BRACKET expr R_BRACKET                           #listElemExpr
  | expr DOT VEC_X                                          #vectorXExpr
  | expr DOT VEC_Y                                          #vectorYExpr
  | expr DOT VEC_Z                                          #vectorZExpr
  | L_BRACKET (expr (COMMA expr)*)? R_BRACKET               #list
  | L_PAR expr COMMA expr COMMA expr R_PAR                  #vector
  | call                                                    #functionCall
  | expr DOT SIZE                                           #size
  | L_PAR expr R_PAR                                        #parentheses
  | MINUS expr                                              #negate
  | NOT expr                                                #not
  | expr (MULTI | DIV) expr                                 #multiDivide
  | expr (PLUS | MINUS) expr                                #plusMinus
  | expr CONCAT expr                                        #concat
  | expr (GREATER | GREATER_EQ | LESS | LESS_EQ) expr       #compare
  | expr (EQ | NOT_EQ) expr                                 #equality
  | expr AND expr                                           #and
  | expr OR expr                                            #or
  ;
