# Displaying matrices nicely

def show_matrix(m):
    '''
    Nicely prints matrix
    :param m: augmented matrix
    :return: prints matrix in readable form
    '''
    s = ''
    for r in m:
        s += '\n['

        for c in r[:-1]:
            s += f'{c:9.3f} '
        s += f'| {r[-1]:.3f}'

        s += ']'

    print(s)