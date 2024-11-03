import unittest
from solver import solve_system_of_eq
from exceptions import MultipleSolException, NoSolException

class TestingSolveSystemOfEq(unittest.TestCase):
    def test_solver_1_eq(self):
        self.assertEqual(solve_system_of_eq('2x = 5'),
                         {'x': 5/2})

    def test_solver_3_eq(self):
        a = '''x +3y +2z = 4
              5x + 8y + 6z = 7
              4x + 3z -2y = 6'''
        b = {'x': round(-65/21, 5), 'y': round(-25/21, 5), 'z': round(16/3, 5)}
        self.assertEqual(solve_system_of_eq(a), b)

    def test_solver_5_eq(self):
        a = '''2*v + w + x + y + z =4
                v + w + y + 2x + z = 6
                v + 2w + 1x + y +z = 5
                v + w + x + 2y + z = 7
                v + 2z + x + y + w = 8'''
        b = {'v': -1, 'w': 0, 'x': 1, 'y': 2, 'z': 3}
        self.assertEqual(solve_system_of_eq(a), b)

class TestSolveSystemOfEqExceptions(unittest.TestCase):
    def test_solver_mult_sol(self):
        a = '''x + y = 1
               2x + 2y = 2'''
        self.assertRaises(MultipleSolException, solve_system_of_eq, a)

    def test_solver_more_var_than_eq(self):
        a = '''x +3y +2z = 4
              4x + 3z -2y = 6'''
        self.assertRaises(MultipleSolException, solve_system_of_eq, a)

    def test_solver_no_sol(self):
        a = '''x + y + z = 1
               x + y + z = 2
               x + y + z = 3'''
        self.assertRaises(NoSolException, solve_system_of_eq, a)