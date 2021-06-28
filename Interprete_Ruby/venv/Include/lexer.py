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
    'true': 'TRUE',
    'false': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'break': 'BREAK',
    'nil': 'NIL',
    'in': 'IN',
    'do':'DO',
    'then': 'THEN',
    'class': 'CLASS',
    'alias': 'ALIAS',
    'begin':'BEGIN',
    'end': 'END',
    'def': 'DEF'
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
    "'": 'SQUOTE',
    '+': 'ADD',
    '-': 'SUBSTRACT',
    '*': 'MULTIPLY',
    '/': 'DIVIDE',
    '(': 'LPAREN',
    ')': 'RPAREN',
    '[': 'LBRACKET',
    ']': 'RBRACKET',
    '%': 'MODULUS'
}

#Manuel: Se definió nuevos tokens
tokens = (
    'INTEGER',
    'ID',
    'FLOAT',
    'GLOBALVARIABLE',
    'INSTANCEVARIABLE',
    'ADD',
    'SUBTRACT',
    'MULTIPLY',
    'DIVIDE',
    'MODULUS',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'DIFFERENT',
    'LESS',
    'GREATER',
    'COMMA',
    'APOST',
    'DQUOTE',
    'ASSIGMENT',
    'EQUALS',
    'COMMENT',
    'BLOCKCOMMENT'
) + tuple(reserved.values())

# Manuel: Se definió nuevas expresiones regulares para tokens simples
t_ADD = r'\+'
t_SUBTRACT = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULUS = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DIFFERENT = r'\!\='
t_LESS = r'<'
t_GREATER = r'>'
t_COMMA = r','
t_APOST = r"\'"
t_DQUOTE = r'\"'
t_ASSIGMENT = r'='
t_EQUALS = r'=='

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FLOAT(t):
    r'(\d+\.\d*)|(\d*\.\d+)'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Manuel: Se definió nuevas expresiones regulares para tokens complejos
def t_GLOBALVARIABLE(t):
    r'\$[a-zA-Z_]\w*'
    return t

def t_INSTANCEVARIABLE(t):
    r'\@[a-zA-Z_]\w*'
    return t

def t_COMMENT(t):
    r'\#.*'
    return t

def t_BLOCKCOMMENT(t):
    r'=begin(.|\n)*=end'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

lexer = lex.lex()
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)

print("Succesfull")