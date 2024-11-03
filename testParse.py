import unittest
from yacc import *
from augmentor import *

class TestingYaccOneEq(unittest.TestCase):
    def test_yacc_1_var(self):
        self.assertEqual(parser.parse('2x = 5'),
                         [{'x': 2, 'result': 5}])
    def test_yacc_2_var(self):
        self.assertEqual(parser.parse('2*x - 3y = 5'),
                             [{'x': 2, 'y': -3, 'result': 5}])
    def test_yacc_4_var(self):
        self.assertEqual(parser.parse('-2x - 3y + 4z - 6a = 5'),
                         [{'x': -2, 'y': -3, 'z': 4, 'a': -6, 'result': 5}])
    def test_yacc_1_coeff(self):
        self.assertEqual(parser.parse('x + 2y = 5'),
                         [{'x': 1, 'y': 2, 'result': 5}])
    def test_yacc_neg_1_coeff(self):
        self.assertEqual(parser.parse('2x - y = 5'),
                         [{'x': 2, 'y': -1, 'result': 5}])

class TestingYaccManyEq(unittest.TestCase):
    def test_yacc_2_eq(self):
        self.assertEqual(parser.parse('''2x = 5
                                        3x = 4'''),
                         [{'x': 2, 'result': 5}, {'x': 3, 'result': 4}])
    def test_yacc_3_eq(self):
        self.assertEqual(parser.parse('''2x = 5 
                                        3y = 4 
                                        2x - 3y = 5'''),
                         [{'x': 2, 'result': 5}, {'y': 3, 'result': 4}, {'x': 2, 'y': -3, 'result': 5}])

class TestingAugmentor(unittest.TestCase):
    def test_aug_1_eq(self):
        self.assertEqual(augment([{'x': 2, 'result': 5}]), ([[2., 5.]], ['x', 'result']))
    def test_aug_2_eq(self):
        self.assertEqual(augment([{'x': -1, 'y': 3, 'result': 4}, {'x': 2, 'y': -4, 'result': 5}]),
                         ([[-1, 3, 4],[2, -4, 5]], ['x', 'y', 'result']))
    def test_aug_4_eq(self):
        a = augment([{'w': 3, 'result': 10},
                     {'x': 13, 'y': -24, 'z': 5, 'w': 7, 'result': 35},
                     {'w': -12, 'x': 16, 'y': 32, 'z': 10, 'result': 60},
                     {'y':4, 'z': 9, 'result': -12}])
        b = ([[3, 0., 0., 0., 10],
              [7, 13, -24, 5, 35],
              [-12, 16, 32, 10, 60],
              [0., 0., 4, 9, -12]], ['w', 'x', 'y', 'z', 'result'])
        self.assertEqual(a,b)