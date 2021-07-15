import ply.yacc as yacc
from lexer import tokens

#Manuel: Parte Matemática
def p_math_operations(p):
    '''math_operations : math_operation
                    | math_operation math_operator math_operations'''
#Manuel: regla semántica para operaciones matematicas
def p_math_operation_complex(p):
    'math_operation : math_value math_operator math_value'
def p_math_operation_simple(p):
    'math_operation : math_value'
def p_math_operation_complex_paren(p):
    'math_operation : LPAREN math_value math_operator math_value RPAREN'
def p_math_value(p):
    '''math_value : real
                    | ID
                    | casting'''
def p_math_operator(p):
    '''math_operator : ADD
                    | SUBSTRACT
                    | MULTIPLY
                    | DIVIDE
                    | MODULUS'''
def p_real_integer(p):
    '''real : INTEGER
            | SUBSTRACT INTEGER'''
def p_real_float(p):
    '''real : FLOAT
            | SUBSTRACT FLOAT'''
def p_casting_integer(p):
    'casting : ID DOT TOI'
def p_casting_float(p):
    'casting : ID DOT TOF'

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)