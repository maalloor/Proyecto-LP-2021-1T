import ply.yacc as yacc
from lexer import tokens, find_warning, build_lexer, lex_analyzer
from verificator import verificator
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


# David: Se definió los tipo array de asignaciones mas comunes
# David: Se definió los tipo array de asignaciones mas comunes
def p_assigment(p):
    """assignment : ID ASSIGN expression
                    | GLOBALID ASSIGN expression
                    | INSTANCEID ASSIGN expression"""

#David: Se separa la declaracion de un array para asignarle sus funciones
def p_array(p):
   """array : arrays ASSIGN LBRACKET factor COMMA factor COMMA factor COMMA factor RBRACKET
            | arrays ASSIGN LBRACKET RBRACKET
            | arrays ASSIGN QUEUE DOT NEW"""


def p_arrays(p):
    """arrays : STRING
              | ID"""

# David: Se definió el formato de la declaracion de una funcion
def p_funcion(p):
    "assignment : DEF ID instruction END"

def p_funcion_length(p):
    "assignment : array DOT LENGTH"

#David: funcion first
def p_funcion_first(p):
    "assignment : array DOT FIRST"

# David: Se definió el metodo insert de array
def p_funcion_insert(p):
    """assignment : array DOT INSERT LPAREN factor COMMA factor RPAREN
                    | array DOT INSERT LPAREN factor COMMA factor COMMA factor COMMA factor RPAREN"""


# David: Se definió el metodo push de array (trabaja como cola)
def p_funcion_push(p):
    "assignment : array DOT PUSH LPAREN factor RPAREN"

#David: funcion pop para pilas
def p_funcion_pop(p):
    "assignment : array DOT POP "

# David: Se definió el metodo length de array

def p_factor(p):
    """factor : INTEGER
                | FLOAT
                | STRING
                | ID
                | GLOBALID
                | INSTANCEID
                | FALSE
                | TRUE"""
# Manuel: Nueva regla, casos en que se ingresan sentencias vacías
def p_empty(p):
    "empty :"
    pass

# Manuel: Regla de sintáxis para errores del parser
def p_error(p):
    if p is not None:
        line = find_warning(verificator.code, p)
        verificator.yacc_error+=1
        verificator.data_yacc_error+=f"Se encontró un error de sintáxis en la línea {p.lineno}\n"
        print(f"Se encontró un error de sintáxis en la línea {p.lineno}\n")
    else:
        verificator.data_yacc_error = "Syntax error at EOF"
        print("Syntax error at EOF")

#Manuel: Construir el parser
def yacc_analyzer(data):
    verificator()
    build_lexer()
    parser = yacc.yacc(start="sentences")
    verificator.code = data
    parser.parse(data)
    return verificator
