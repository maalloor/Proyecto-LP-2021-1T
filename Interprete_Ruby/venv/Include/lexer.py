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

#Manuel: Se definió nuevos tokens
tokens = (
    'INTEGER',
    'ID',
    'STRING',
    'FLOAT',
    'GLOBALID',
    'INSTANCEID',
    'ADD',
    'SUBSTRACT',
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
    'ASSIGN',
    'EQUALS',
    'COMMENT',
    'BLOCKCOMMENT',
    'DOT',
    'GREATEREQUAL',
    'LESSEQUAL'
) + tuple(reserved.values())

# Manuel: Se definió nuevas expresiones regulares para tokens simples
t_ADD = r'\+'
t_SUBSTRACT = r'-'
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
t_ASSIGN = r'='
t_EQUALS = r'=='
t_DOT = r'\.'
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_STRING(t):
    r'(\'.*\'|\".*\")'
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
def t_GLOBALID(t):
    r'\$[a-zA-Z_]\w*'
    return t

def t_INSTANCEID(t):
    r'\@[a-zA-Z_]\w*'
    return t

def t_COMMENT(t):
    r'\#.*'
    return t

def t_BLOCKCOMMENT(t):
    r'=begin(.|\n)*=end'
    return t

#Definición y conteo del número de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#Reconocimiento de tabulación
t_ignore = ' \t'

#Reconocimiento de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Obtener los tokens del Lexer
def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

lexer = lex.lex()

"""
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)

print("Succesfull")

"""