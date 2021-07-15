import ply.yacc as yacc
from lexer import tokens, find_warning, build_lexer, lex_analyzer
from verificator import verificator
from mathOperations import *
from logicOperations import *
#Manuel: Definición de reglas para sentencias generales
def p_sentences(p):
    '''sentences : sentence
                | sentence sentences
                | empty'''
#Manuel: Definición de la regla de vacío
def p_empty(p):
    'empty : '
#Manuel: Definción de regla para sentencia simple
def p_sentence(p):
    '''sentence : assignment_var
                | operations
                | imprint
                | structs_control
                | termination'''
#Manuel: Regla para Asignación para variables, globales e instancia
def p_assignation_var(p):
    '''assignation_var : ID ASSIGN value
                    | special_var ASSIGN value'''
#Manuel: Regla para operaciones matemáticas que provienen de mathOperations.py
def p_operations(p):
    '''operations : math_operations
                | log_operations
                | inc_dec_operations'''
#Manuel: Regla para las estructuras de control a implementar
def p_structs_control(p):
    '''structs_control : struct_while
                        | struct_if'''
#Manuel: Regla que contiene terminaciones comunes para las estructuras de control
def p_termination(p):
    '''termination : return
                    | continue
                    | break'''
#Manuel: Regla neta para variables especiales global, instance
def p_special_var(p):
    '''special_var : GLOBAL
                    | INSTANCE'''
#Manuel: Regla de tipos especificos de datos
def p_type(p):
    '''type : real
            | STRING
            | boolean
            | NIL'''
#Manuel: Regla que contiene datos para operaciones mateematicas. Se definio regla semantica en mathOperations
def p_real(p):
    '''real : INTEGER
            | FLOAT'''
#Manuel: Regla que contiene datos booleanos
def p_boolean(p):
    '''boolean : TRUE
                | FALSE'''
#Manuel: Regla que contiene todos los datos a utilizar
def p_value(p):
    '''value : type
            | operations
            | ID
            | structs_data
            | slicing
            | methods_struct
            | call_function
            | negative
            | casting'''
#Manuel: Se definió nuevas reglas de Casting
def p_casting_integer(p):
    'casting : ID DOT TOI'
def p_casting_float(p):
    'casting : ID DOT TOF'
def p_casting_string(p):
    'casting : ID DOT TOS'
#Manuel: Se definió regla de números negativos
def p_negative(p):
    '''negative : SUBSTRACT real
                | SUBSTRACT ID
                | SUBSTRACT slicing
                | SUBSTRACT call_function'''
def p_slicing(p):
    'index : ID LBRACKET value DCORCH'
def p_assignation_array(p):
    '''assignation_array : ID LBRACKET INTEGER RBRACKET ASSIGN value'''
def p_assignation_inc_dec(p):
    '''assignation_inc_dec : ID operator ASSIGN operation_mat'''
def p_imprint(p):
    '''imprint : PRINT value
                | PUTS value'''
#Manuel: Se definió diferentes formatos de la estructura de control WHILE en Ruby
def p_while(p):
    '''while : WHILE comparison DO operations END
            | WHILE comparison OR comparison DO operations END
            | WHILE comparison AND comparison DO operations END'''

#Manuel: Se definió diferentes formatos de la estructura de control IF en Ruby
def p_if(p):
    """if : IF comparison operations END
            | IF comparison OR comparison operations END
            | IF comparison AND comparison operations END
            | IF comparison instruction ELSE operations END
            | IF comparison instruction ELSIF operations ELSE operations END"""
#Manuel: Se definió un conjunto de comparaciones que pueden realizarse. Regla Semántica
def p_comparisons(p):
    '''comparisons: comparison
                    | comparison log_operator comparisons'''
def p_comparison(p):
    '''comparison : type EQUALS type
                    | type DIFFERENT type
                    | type LESS type
                    | type GREATER type
                    | type GREATEREQUAL type
                    | type LESSEQUAL type
                    | boolean'''
def p_structs_control(p):
    '''structs_control : while
                        | if'''
def p_arg_function(p):
    '''arg_function : ID
                    | assignation_var'''
def p_args_function(p):
    '''args_function : arg_function COMMA args_function
                    | arg_function
                    | empty'''
def p_function(p):
    'function : DEF ID LPAREN args_function RPAREN sentences END'

# David: Se definió los tipo array de asignaciones mas comunes
def p_assignment(p):
    """assignment : ID ASSIGN sentence
                    | GLOBALID ASSIGN sentence
                    | INSTANCEID ASSIGN sentence"""

#David: Se separa la declaracion de un array para asignarle sus funciones
def p_array(p):
   """array : arrays ASSIGN LBRACKET value COMMA value COMMA value COMMA value RBRACKET
            | arrays ASSIGN LBRACKET RBRACKET
            | arrays ASSIGN QUEUE DOT NEW"""

def p_arrays(p):
    """arrays : STRING
              | ID"""

# David: Se definió el formato de la declaracion de una funcion
def p_funcion(p):
    "assignment : DEF ID sentence END"

def p_funcion_length(p):
    "assignment : array DOT LENGTH"

#David: funcion first
def p_funcion_first(p):
    "assignment : array DOT FIRST"

# David: Se definió el metodo insert de array
def p_funcion_insert(p):
    """assignment : array DOT INSERT LPAREN sentence COMMA sentence RPAREN
                    | array DOT INSERT LPAREN sentence COMMA sentence COMMA sentence COMMA sentence RPAREN"""


# David: Se definió el metodo push de array (trabaja como cola)
def p_funcion_push(p):
    "assignment : array DOT PUSH LPAREN sentence RPAREN"

#David: funcion pop para pilas
def p_funcion_pop(p):
    "assignment : array DOT POP "

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
