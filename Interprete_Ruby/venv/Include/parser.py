import ply.yacc as yacc
from lexer import tokens

#Manuel: Se definió los tipos de instrucciones que contendrá el cuerpo del código
def p_instruction(p):
    """instruction : imprint
                    | expression
                    | sentence
                    | assignment"""
#Manuel: Se definió los tipos de impresión a utilizar en Ruby
def p_imprint(p):
    """imprint : PRINT expression
                | PUTS expression"""
#Manuel: Se definió las operaciones básicas en Ruby
def p_expression(p):
    """expression : expression ADD term
                    | expression SUBSTRACT term
                    | term"""
def p_term(p):
    """term : term MULTIPLY factor
            | term DIVIDE factor
            | factor"""
#Manuel: Se definió diferentes formatos de la estructura de control WHILE en Ruby
def p_sentence_while(p):
    """sentence : WHILE comparison DO instruction END
                | WHILE comparison OR comparison DO instruction END
                | WHILE comparison AND comparison DO instruction END"""
#Manuel: Se definió diferentes formatos de la estructura de control FOR en Ruby
def p_sentence_for(p):
    """sentence : FOR ID IN factor DOT DOT factor instruction END
                | FOR ID IN ID instruction END"""
#Manuel: Se definió diferentes formatos de la estructura de control IF en Ruby
def p_sentence_if(p):
    """sentence : IF comparison instruction END
                | IF comparison OR comparison instruction END
                | IF comparison AND comparison instruction END
                | IF comparison instruction ELSE instruction END
                | IF comparison instruction ELSIF instruction ELSE instruction END"""
#Manuel: Se definió un conjunto de comparaciones que pueden realizarse
def p_comparison(p):
    """comparison : factor EQUALS factor
                    | factor DIFFERENT factor
                    | factor LESS factor
                    | factor GREATER factor
                    | factor GREATEREQUAL factor
                    | factor LESSEQUAL factor"""
#Manuel: Se definió los tipo de asignaciones mas comunes
def p_assignment(p):
    """assignment : ID ASSIGN expression
                    | GLOBALID ASSIGN expression
                    | INSTANCEID ASSIGN expression"""
#Manuel: Se definió un tipo de assignacion exclusivo para la estructura de datos array
def p_assignment_array(p):
    'assignment : ID ASSIGN LBRACKET factor COMMA factor COMMA factor COMMA factor RBRACKET'
#Manuel: Se definió factor que incluye todos los tipos de datos
def p_factor(p):
    """factor : INTEGER
                | FLOAT
                | STRING
                | ID
                | GLOBALID
                | INSTANCEID
                | FALSE
                | TRUE"""

# Regla de error para errores de sintaxis
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")

# Contrucción del parser
parser = yacc.yacc()

while True:
    try:
        s = input('parser > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)