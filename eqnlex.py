# System of Equations Tokenizer

import ply.lex as lex

tokens = ('PLUS', 'MINUS', 'NUMBER', 'MULTIPLY', 'VARIABLE', 'EQUALS', 'NEWLINE')

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_VARIABLE = '[a-zA-Z]'
t_EQUALS = r'='
t_NEWLINE = r'\n'

def t_NUMBER(t):
    #r'[\-+]?\d+'
    r'\d+'
    t.value = float(t.value)
    return t

t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()