import ply.lex as lex
from verificator import verificator

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
    'def': 'DEF',
    'new': 'NEW',
    'Queue': 'QUEUE',
    'to_i': 'TOI',
    'to_s': 'TOS',
    'to_f': 'TOF'
}

#David: Se definio diccionario de metodos de la estructura de control
array_methods = {
    'length': 'LENGTH',
    'push': 'PUSH',
    'insert': 'INSERT',
    'pop': 'POP',
    'first': 'FIRST'
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
    pass

def t_BLOCKCOMMENT(t):
    r'=begin(.|\n)*=end'
    pass

#Definición y conteo del número de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#Reconocimiento de tabulación
t_ignore = ' \t'

#Manuel: Reconocimiento de error
def find_warning(input, token):
    start_line = input.rfind("\n",0,token.lexpos) + 1
    return (token.lexpos - start_line) + 1

#Reconocimiento de errores
def t_error(t):
    line = find_warning(verificator.code, t)
    verificator.data_lex_error = f"El carácter {t.value[0]} es inválido. Se encuentra en la línea {t.lineno}"
    verificator.lex_error+=1
    print(f"El carácter {t.value[0]} es inválido. Se encuentra en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def build_lexer():
    verificator.lex = lex.lex()

def lex_analyzer(data):
    verificator()
    build_lexer()
    verificator.code = data
    lexer = verificator.lex
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
    return verificator.data_lex_error
