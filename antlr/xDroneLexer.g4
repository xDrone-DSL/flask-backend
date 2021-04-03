lexer grammar xDroneLexer;

MAIN: 'main' ;

TAKEOFF: 'takeoff' ;
LAND: 'land' ;
UP: 'up' ;
DOWN: 'down' ;
LEFT: 'left' ;
RIGHT: 'right' ;
FORWARD: 'forward' ;
BACKWARD: 'backward' ;
ROTATE_LEFT: 'rotate_left' ;
ROTATE_RIGHT: 'rotate_right' ;
WAIT: 'wait' ;

AT: 'at' ;
INSERT: 'insert' ;
REMOVE: 'remove' ;
SIZE: 'size' ;

IF: 'if' ;
ELSE: 'else' ;
WHILE: 'while' ;
FOR: 'for' ;
FROM: 'from' ;
TO: 'to' ;
REPEAT: 'repeat' ;
TIMES: 'times' ;

FUNCTION: 'function' ;
RETURN: 'return' ;

TYPE_INT: 'int' ;
TYPE_DECIMAL: 'decimal' ;
TYPE_STRING: 'string' ;
TYPE_BOOLEAN: 'boolean' ;
TYPE_VECTOR: 'vector' ;
TYPE_LIST: 'list' ;

TRUE: 'true' ;
FALSE: 'false' ;

VEC_X: 'x' ;
VEC_Y: 'y' ;
VEC_Z: 'z' ;

MULTI: '*' ;
DIV: '/' ;
PLUS: '+' ;
MINUS: '-' ;
CONCAT: '&' ;
GREATER: '>' ;
GREATER_EQ: '>=' ;
LESS: '<' ;
LESS_EQ: '<=' ;
EQ: '==' ;
NOT_EQ: '=/=' ;
NOT: 'not' ;
AND: 'and' ;
OR: 'or' ;

L_PAR: '(' ;
R_PAR: ')' ;
L_BRACKET: '[' ;
R_BRACKET: ']' ;
L_BRACE: '{' ;
R_BRACE: '}' ;

DOT: '.' ;
COMMA: ',' ;
SEMICOLON: ';' ;
ARROW: '<-' ;



fragment DIGIT : [0-9] ;
fragment LOWERCASE : [a-z] ;
fragment UPPERCASE : [A-Z] ;
fragment UNDERSCORE : '_' ;

COMMENT: '#' ~[\r\n]* [\r\n] -> skip ;
WS: [ \n\r\t]+ -> skip ;

IDENT :
  (UNDERSCORE
  | LOWERCASE
  | UPPERCASE)
  (UNDERSCORE
  | LOWERCASE
  | UPPERCASE
  | DIGIT)*
  ;

fragment INT : DIGIT+ ;
SIGNED_INT : ('+'|'-')? INT ;
fragment DECIMAL : INT '.' INT? | '.' INT ;

fragment EXP: ('e'|'E') SIGNED_INT ;
fragment FLOAT: INT EXP | DECIMAL EXP? ;
SIGNED_FLOAT: ('+'|'-')? FLOAT ;

fragment DOUBLE_QUOTE : '"' ;
fragment ESCAPED_CHAR
  :
  ('\\0'
  | '\\' 'b'
  | '\\' 'n'
  | '\\' 'f'
  | '\\' 'r'
  | '\\' DOUBLE_QUOTE
  | '\\' '\''
  | '\\' '\\')
  ;

fragment CHARACTER
  :
  ~('\''
  | '"'
  | '\\')
  | ESCAPED_CHAR
  ;
ESCAPED_STRING : DOUBLE_QUOTE CHARACTER* DOUBLE_QUOTE ;
