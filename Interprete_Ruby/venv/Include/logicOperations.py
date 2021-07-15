from mathOperations import *

def p_log_operations(p):
    '''log_operations : log_operation
                    | log_operation log_operator log_operations'''
def p_log_operator(p):
    '''log_operator : AND
                    | OR
                    | NOT'''
#manuel: Regla semantica para comparaciones
def p_log_operation_simple(p):
    'log_operation : comp_value comparator comp_value'
def p_log_operation_complex_paren(p):
    'log_operation : LPAREN comp_value comparator comp_value RPAREN'
def p_comparator(p):
    '''comparator : EQUALS
                    | DIFFERENT
                    | GREATER
                    | LESS
                    | GREATEREQUAL
                    | LESSEQUAL'''
def p_comp_value(p):
    '''comp_value : ID
                    | real
                    | STRING
                    | boolean
                    | slicing
                    | comp_negative
                    | method_struct
                    | call_function'''
def p_comp_negative(p):
    'comp_negative : NOT comp_value'


