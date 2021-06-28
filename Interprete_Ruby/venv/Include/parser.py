import ply.yacc as yacc
from lexer import tokens

def p_instruction(p):
    """instruction : imprint
                    | expression
                    | sentence"""

def p_imprint(p):
    """imprint : PRINT expression
                | PUTS expression"""

def p_expression(p):
    """expression : expression ADD term
                    | expression SUBSTRACT term
                    | term"""
def p_term(p):
    """term : term MULTIPLY factor
            | term DIVIDE factor
            | factor"""

def p_sentence_while(p):
    """sentence : WHILE comparison DO instruction END
                | WHILE comparison OR comparison DO instruction END
                | WHILE comparison AND comparison DO instruction END"""

def p_sentence_for(p):
    'sentence : FOR ID IN RANGE instruction END'

def p_sentence_if(p):
    """sentence : IF comparison instruction END
                | IF comparison OR comparison instruction END
                | IF comparison AND comparison instruction END
                | IF comparison instruction ELSE instruction END
                | IF comparison instruction ELSIF instruction ELSE instruction END"""

def p_comparison(p):
    """comparison : factor EQUALS factor
                    | factor DIFFERENT factor
                    | factor LESS factor
                    | factor GREATER factor"""

def p_factor(p):
    """factor : INTEGER
                | FLOAT
                | STRING
                | ID
                | GLOBALID
                | INSTANCEID"""

#Aquí debería ir comparison


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
        s = input('parser > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)