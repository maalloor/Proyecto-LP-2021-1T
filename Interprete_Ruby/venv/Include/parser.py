import ply.yacc as yacc
from lexer import tokens, lexer
checked = True
parser_rules = []
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
def p_assigment(p):
    """assignment : ID ASSIGN expression
                    | GLOBALID ASSIGN expression
                    | INSTANCEID ASSIGN expression
                    | ID ASSIGN LBRACKET factor COMMA factor COMMA factor COMMA factor RBRACKET"""


# David: Se definió el formato de la declaracion de una funcion
def p_funcion(p):
    "assignment : DEF ID instruction END"


# David: Se definió el metodo length de array
def p_funcion_length(p):
    "assignment : ID DOT LENGTH"


# David: Se definió el metodo insert de array
def p_funcion_insert(p):
    "assignment : ID DOT INSERT LPAREN factor COMMA factor RPAREN"


# David: Se definió el metodo push de array (trabaja como cola)
def p_funcion_push(p):
    "assignment : ID DOT PUSH LPAREN factor RPAREN"

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

# Regla de error para errores de sintaxis
def p_error(p):
    if p is not None:
        parser_rules.append("Syntax Error")

    else:
        print("Syntax Error!!")
        parser_rules.append("Syntax Error")  # añade el error a el arreglo

# Manuel: Se procede a construir el parser
parser = yacc.yacc()

def p_empty(p):
    "empty :"
    pass


# Build the parser
parser = yacc.yacc()

#Manuel: Creación de código ejemplo para el parser.py
example_code = """
def main (a)
    saludo = 'Hola'
    if saludo == 'Hola'
        saludo = 'Hola Mundo!'
    end
end
"""

lexer.input(example_code)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
print("\n")

lexer.lineno = 0

#Manuel: Ejecución de ejemplo con el parse.py
parser.parse(example_code)

if checked:
    print("¡El código es válido!")
else:
    print("¡El código no es válido!")

# funcion del analizador

def analizarSintactico(s):
    parser_rules.clear()  # limpio los errores
    print(s)
    parser_result = str(parser.parse(s))
    print(parser_result)
    return parser_result, parser_rules
