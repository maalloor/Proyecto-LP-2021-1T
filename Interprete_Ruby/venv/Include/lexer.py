import ply.lex as lex
reglas = []
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

#David: Se definio diccionario de metodos de la estructura de control
array_methods = {
    'length': 'LENGTH',
    'push': 'PUSH',
    'insert': 'INSERT'
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
    'LESSEQUAL',
) + tuple(reserved.values()) + tuple(array_methods.values())

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
    print("No se ha reconocido '%s'" % t.value[0])
    if t is not None:
        reglas.append("Error, no se pudo encontrar el token '%s'" % t.value[0])
    else:
        print("Error de sintáxis")
        reglas.append("Syntax Error")  # añade el error a el arreglo
    t.lexer.skip(1)

lexer = lex.lex()

def analizarLexico(data):
    reglas.clear()  # limpio los errores
    lexer.input(data)
    resultados = ""
    while True:
        tok = lexer.token()
        if not tok:
            break
        resultado = str(tok) + "\n"
        resultados = resultados + resultado
    return resultados, reglas
