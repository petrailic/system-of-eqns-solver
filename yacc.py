# System of Equations Parser

from logging import Logger
import ply.yacc as yacc
from eqnlex import tokens

def p_system(p):
    '''system : equation
              | system NEWLINE equation '''

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_equation(p):
    'equation : expression EQUALS NUMBER'
    p[0] = p[1] | {'result': p[3]}

def p_expression(p):
    '''expression : term
                  | expression term'''
    if len(p) ==2:
        p[0] = p[1]
    else:
        p[0] = p[1] | p[2]

def p_term(p):
    '''term : VARIABLE
            | PLUS VARIABLE
            | MINUS VARIABLE
            | factor VARIABLE
            | factor MULTIPLY VARIABLE'''
    if p[0] == None:
        if len(p) == 4:
            p[0] = {p[3] : p[1]}
        elif len(p) == 2:
            p[0] = {p[1]: 1}
        elif p[1] == '+':
            p[0] = {p[2] : 1}
        elif p[1] == '-':
            p[0] = {p[2] : -1}
        else:
            p[0] = {p[2] : p[1]}
    else:
        if len(p) == 4:
            p[0][p[3]] = p[1]
        elif p[1] == '+':
            p[0][p[2]] = 1
        elif p[1] == '-':
            p[0][p[2]] = -1
        else:
            p[0][p[2]] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | PLUS NUMBER
              | MINUS NUMBER'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == '+':
        p[0] =  p[2]
    elif p[1] == '-':
        p[0] = -1 * p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

