import unittest
import gauss
from exceptions import MultipleSolException, NoSolException


class TestingRowOps(unittest.TestCase):
    def test_row_scale(self):
        m = [[1, 2, 3], [4, 5, 6]]
        gauss.row_scale(m, 0, 2)
        self.assertEqual(m,[[2, 4, 6], [4, 5, 6]])

    def test_row_swap(self):
        m = [[1, 2, 3], [4, 5, 6]]
        gauss.row_swap(m, 0, 1)
        self.assertEqual(m,[[4, 5, 6], [1, 2, 3]])

    def test_row_swap_inplace(self):
        m = [[1, 2, 3], [4, 5, 6]]
        gauss.row_swap(m, 0, 0)
        self.assertEqual(m,[[1, 2, 3], [4, 5, 6]])

    def test_row_sum(self):
        m = [[1, 2, 3], [4, 5, 6]]
        gauss.row_sum(m, 0, 1, 2)
        self.assertEqual(m,[[1, 2, 3], [6, 9, 12]])

    def test_row_sum_neg(self):
        m = [[1, 2, 3], [4, 5, 6]]
        gauss.row_sum(m, 0, 1, -2)
        self.assertEqual(m,[[1, 2, 3], [2, 1, 0]])


class TestingRowReduce(unittest.TestCase):

    def test_row_reduce_2x3(self):
        self.assertEqual(gauss.row_reduce([[1,2,3],[4,5,6]]),
                         [[1,0,-1],[0,1,2]])

    def test_row_reduce_3x4(self):
        self.assertEqual(gauss.row_reduce([[1,2,3,12],
                                          [4,5,6,9],
                                          [7,8,10,6]]),
                         [[1,0,0,-14],
                                  [0,1,0,13],
                                  [0,0,1,0]])

    def test_row_reduce_3x4_swaps(self):
        self.assertEqual(gauss.row_reduce([[0,2,3,5],
                                          [4,5,6,10],
                                          [7,8,10,15]]),
                         [[1,0,0,-1],
                                  [0,1,0,4],
                                  [0,0,1,-1]])

    def test_row_reduce_row_of_0s(self):
        self.assertEqual(gauss.row_reduce([[1,1,1],[1,1,1]]),
                         [[1,1,1],[0,0,0]])

class TestingHasZeroCol(unittest.TestCase):

    def test_zero_col_false(self):
        self.assertEqual(gauss.has_zero_col([[1,2,3],[4,5,6]]), False)

    def test_zero_col_true(self):
        self.assertEqual(gauss.has_zero_col([[1,0,3],[4,0,6]]), True)

    def test_zero_col_last_col(self):
        self.assertEqual(gauss.has_zero_col([[1,2,0],[4,5,0]]), False)

class TestingSolveOneSol(unittest.TestCase):

    def test_solve_1x2(self):
        self.assertEqual(gauss.solve_matrix([[1, 2]], ['x']), {'x': 2})

    def test_solve_2x3(self):
        self.assertEqual(gauss.solve_matrix([[1, 2, 3], [4, 5, 6]], ['x', 'y']), {'x': -1, 'y': 2})

    def test_solve_3x4(self):
        self.assertEqual(gauss.solve_matrix([[1, 2, 3, 12],
                                            [4,5,6,9],
                                            [7,8,10,6]], ['x', 'y', 'z']), {'x': -14, 'y': 13, 'z': 0})

    def test_solve_3x4_swaps(self):
        self.assertEqual(gauss.solve_matrix([[0, 2, 3, 5],
                                            [4,5,6,10],
                                            [7,8,10,15]], ['x', 'y', 'z']), {'x': -1, 'y': 4, 'z': -1})

    def test_solve_3x4_zero(self):
        self.assertEqual(gauss.solve_matrix([[0, 2, 3, 0],
                                            [4,5,6,0],
                                            [7,8,10,0]], ['x', 'y', 'z']), {'x': 0, 'y': 0, 'z': 0})


class TestingSolveNoOrMultSol(unittest.TestCase):

    def test_solve_inf_sol(self):
        self.assertRaises(MultipleSolException, gauss.solve_matrix, [[1, 1, 1], [1, 1, 1]], ['x', 'y', 'z'])

    def test_solve_no_sol(self):
        self.assertRaises(MultipleSolException, gauss.solve_matrix, [[1, 1, 1], [2, 2, 2]], ['x', 'y', 'z'])

    def test_solve_zero_eq_nonzero(self):
        self.assertRaises(NoSolException, gauss.solve_matrix, [[1, 1, 1], [1, 1, 2]], ['x', 'y', 'z'])

    def test_solve_zero_col(self):
        self.assertRaises(NoSolException, gauss.solve_matrix, [[1, 0, 1], [2, 0, 1]], ['x', 'y', 'z'])


if __name__ == '__main__':
    unittest.main()
