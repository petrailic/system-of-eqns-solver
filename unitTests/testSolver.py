import unittest
from solver import solve_system_of_eq
from exceptions import MultipleSolException, NoSolException, InputSyntaxErrorException

class TestingSolveSystemOfEq(unittest.TestCase):
    def test_solver_1_eq(self):
        self.assertEqual(solve_system_of_eq('2x = 5'),
                         {'x': 5/2})

    def test_solver_2_eq(self):
        self.assertEqual(solve_system_of_eq('''x = 5
                                                z = 6'''),
                         {'x': 5, 'z':6})

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

    def test_solver_10_eq(self):
        a = '''2a + 3b -c + 4d -e + 2f -g +5h +2i +j =15
               4a -2b + c -d + 3e +f -2g + 4h -3i + 2j = 8
               a + 4b -3c + 2d + 5e -f + g -h + 3i +j = 12
               3a -1b + 4c -d + 2e + f -3g +h -i + 2j = 9
               -a +2b + 3c -d + 4e +f + g -2h +4i +j =10
               2a -b + c + 3d -e + 4f -g + h -2i + 3j = 5
               a - b + 2c + d + 3e - f + 4g - h + 2i -j = 7
               -3a +b + c - d + 2e + 3f -g + 4h -i + 2j = 6
               a + 3b -c + 2d + 4e -f + 2g -3h +i +5j = 14
               4a -b +c +2d - 3e + f -g + 3h + 2i + j = 11'''
        b = {'a': 0.11215, 'b': -0.34002, 'c': 0.93034, 'd': 1.66183, 'e': 1.17305,
             'f': -1.14487, 'g': -0.47326, 'h': 1.46008, 'i': 1.87058, 'j': 2.02674}
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

    def test_incorrect_eq_structure(self):
        a = '''3 + 2x = 1
               x + y = 4'''
        self.assertRaises(InputSyntaxErrorException, solve_system_of_eq, a)

    def test_empty(self):
        self.assertRaises(InputSyntaxErrorException, solve_system_of_eq, '')