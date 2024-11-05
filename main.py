from eqnlex import *
from yacc import *
from augmentor import*
from gauss import *
from solver import *

# examining tokens example
data = '''2*x + 6y = 4 
            2x - 3y = 5'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# trying out parser
result = parser.parse(data)
print(result)

# trying out complete solver
s = '''3x -4y +2z = 5
       2x + 7y -z = 6
       5x + z +10y = 14'''

print(solve_system_of_eq(s))
