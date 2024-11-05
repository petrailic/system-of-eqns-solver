# Complete solver

from yacc import *
import augmentor
import gauss

def solve_system_of_eq(s: str):
    '''
    Parses and solves systems of equations with one solution, raises error if system has multiple or no solutions
    :param s: string representation of system of equations (each equation is on a new line)
    :return: dictionary of variables and their value
    '''
    # parse string
    parsed = parser.parse(s)

    # make augmented matrix
    matrix, var = augmentor.augment(parsed)

    # solve augmented matrix with gaussian elimination
    sol = gauss.solve_matrix(matrix, var)

    return sol