# Functions pertaining to Gaussian Elimination

import exceptions
from exceptions import MultipleSolException, NoSolException

# Elementary Row Operations

def row_scale(m, r, s):
    """
    Multiplying matrix row by a constant s

    :param m: matrix
    :param r: (int) row index value
    :param s: (float) scalar value
    """
    m[r] = [x * s for x in m[r]]

def row_swap(m, row_a, row_b):
    """
    Exchanging two rows of a matrix

    :param m: matrix
    :param row_a: (int) row index value
    :param row_b: (int) row index value
    """
    m[row_a], m[row_b] = m[row_b], m[row_a]


def row_sum(m, row_a, row_b, s=1):
    """
    Adding a multiple of row_a to row_b

    :param m: matrix
    :param row_a: (int) row index value
    :param row_b: (int) row index value
    :param s: (float) scalar value for row_a, default value of 1
    """
    for i in range(len(m[row_a])):
       m[row_b][i] += m[row_a][i] * s


# Gaussian Elimination
def row_reduce(m):
    '''
    Converts matrix into reduced row echelon from (RREF)

    :param m: matrix
    :return: mutated matrix m in RREF
    '''

    lead1pos = 0
    row_pos = 0
    while row_pos < len(m) and lead1pos < len(m):

        # find non-zero leading value and move it to the "top"
        if m[row_pos][lead1pos] != 0:
            row_swap(m, row_pos, lead1pos)

            # scale row with non-zero leading value to have pivotal 1
            scaler = 1 / m[lead1pos][lead1pos]
            row_scale(m, lead1pos, scaler)

            # clear out non-zero values above and below the pivotal 1
            for i in range(0, len(m)):
                if i != lead1pos and m[i][lead1pos] != 0:
                    s = m[i][lead1pos]
                    row_sum(m, lead1pos, i, -1 * s)

            # move on to next leading one position
            lead1pos += 1
            row_pos = lead1pos

        else:
            row_pos+=1

    return m

def has_zero_col(m):
    '''
    :param m: matrix
    :return: (boolean) True if matrix m has zero column in any but last column,
                returns False otherwise
    '''
    for c in range(len(m[0])-1):
        for r in range(len(m)):
            if m[r][c] != 0:
                break
            elif r == len(m)-1:
                return True
    return False

def has_zero_equals_nonzero(m):
    for r in m:
        if r[:-1] == [0] * (len(m[0]) -1) and r[-1] != 0:
            return True
    return False

def solve_matrix(m, var):
    '''
    Solves a matrix
    :param m: augmented matrix
    :param var: array of variables in the order they are represented in the matrix
    :return: dictionary of form variable : solution rounded to 5 decimal places
    '''
    # check matrix dimensions and variables
    if len(m) != len(m[0])-1:
        raise MultipleSolException
    if len(var) != len(m[0]):
        print('Variables array is inconsistent with matrix')

    # get to RREF
    row_reduce(m)

    # consider multiple or no solutions via exceptions
    if [0]*len(m[0]) in m:               # row of zeros
        raise MultipleSolException

    if has_zero_col(m):
        raise NoSolException

    if has_zero_equals_nonzero(m):
        raise NoSolException

    # extract solution
    sol = {}
    for i in range(len(var)):
        if var[i] != 'result':
            v = var[i]
            n = round(m[i][-1], 5)
            sol[v] = n
    return sol

