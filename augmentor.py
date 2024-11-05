# Augmentor function for interpreting parser output

import numpy as np

def augment(lyst: list):
    '''
    Creates matrix representation of valid system of equations and descriptive variable array
    :param lyst: list of dictionaries where each dictionary represents a linear equation;
                the dictionaries are of the form {variable : coefficient} with one key named 'result' that
                holds the value of the right hand side of the equation
    :return: tuple of augmented matrix representing the system of equations and
            an array of variables in the order they are represented in the matrix (alphabetical)
    '''
    # make list of all variables
    variables = []
    for eq in lyst:
        variables += list(eq.keys())

    # get rid of repeated variables
    variables = set(variables)
    variables = list(variables)
    variables.sort()

    # move 'result' to end of variables list
    # this list is in the order that the variables are represented in the augmented matrix
    variables.remove('result')
    variables.append('result')

    # make appropriately sized zero matrix
    rows = len(lyst)
    cols = len(variables)
    m = (np.zeros((rows, cols))).tolist()
    #m = [[0.]*cols]*rows

    # fill the matrix
    for i in range(cols):
        var = variables[i]
        for eq in range(rows):
            if var in lyst[eq]:
                m[eq][i] = lyst[eq][var]


    return m, variables