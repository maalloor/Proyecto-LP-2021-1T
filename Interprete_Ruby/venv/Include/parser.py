import ply.yacc as yacc
from lexer import tokens, lexer

def p_cuerpo(p):
    """cuerpo : expression
             | impresion
             | sentencia """
def p_impresion(p):
    '''impresion : PRINT LPAREN expression RPAREN
                    | PRINT LPAREN RPAREN'''
def p_expression_plus(p):
    'expression : expression MAS term'
def p_expression_minus(p):
    'expression : expression MINUS term'

def p_expression_term(p):
    'expression : term'
def p_term_times(p):
    'term : term TIMES factor'
def p_term_div(p):
    'term : term DIVIDE factor'
def p_term_mod(p):
    'term : term MOD factor'
def p_term_factor(p):
    'term : factor'
def p_sentencia_if(p):
    'sentencia : IF factor comparacion factor LKEY cuerpo RKEY'
def p_comparacion(p):
    '''comparacion : MAYOR
                    | MAYORIGUAL'''
def p_factor_num(p):
    'factor : NUMBER'
def p_factor_id(p):
    'factor : ID'
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
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