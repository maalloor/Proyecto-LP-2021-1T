import ply.lex as lex

reserved = {
    'puts': 'PUTS',
    'print': 'PRINT',
    'gets': 'GETS',
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'while': 'WHILE',
    'for': 'FOR',
    'end': 'END',
    'true': 'TRUE',
    'false': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'break': 'BREAK',
    'nil': 'NIL'
}
symbols = {
    '@': 'AT',
    '#': 'HASH',
    '=': 'EQUAL',
    '$': 'DOLLAR',
    '>': 'GREATER',
    '<': 'LESS',
    '!': 'EXCLAMATION',
    '"': 'DQUOTE',
    "'": 'SQUOTE'
}
tokens = (
    'INTEGER',
    'STRING',
    'FLOAT',
    'ADD',
    'SUBTRACT',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'MODULUS',
) + tuple(reserved.values()) + tuple(symbols.values())
# Regular expression rules for simple tokens
t_ADD = r'\+'
t_SUBTRACT = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_MODULUS = r'%'

def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'STRING')
    return t

def t_FLOAT(t):
    r'(\d+\.\d*)|(\d*\.\d+)'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SYMBOL(t):
    r'\W'
    t.type = symbols.get(t.value, 'STRING')
    if t.type in symbols.values():
        return t
    else:
        t_error(t)

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

# Build the lexer
lexer = lex.lex()
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")