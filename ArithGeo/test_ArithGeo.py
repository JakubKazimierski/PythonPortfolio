'''
Unittests for ArithGeo.py
November 2020 Jakub Kazimierski
'''

import unittest
import ArithGeo

class test_ArithGeo(unittest.TestCase):
    '''
    Class contains unittests for
    ArithGeo.py
    '''

    #region Unittests
    def test_ArithmeticOutput(self):
        '''
        Checks if for arithmetic sequence
        output is "Arithmetic".
        '''
        output = ArithGeo.ArithGeo([1,2,3,4])
        self.assertEqual(output, "Arithmetic")

    def test_GeometricOutput(self):
        '''
        Checks if output for geometric sequence
        is "Geometric".
        '''
        output = ArithGeo.ArithGeo([1,2,4,8])
        self.assertEqual(output, "Geometric")

    def test_NegativeArithmeticOutput(self):
        '''
        Checks if for negative arithmetic seq
        output is "Arithmetic".
        '''
        output = ArithGeo.ArithGeo([-1,-2,-3,-4])
        self.assertEqual(output, "Arithmetic")

    def test_NegativeGeometricOutput(self):
        '''
        Checks if for negative numbers in geometric sequence
        output is "Geometric".
        '''
        output = ArithGeo.ArithGeo([-1,2,-4,8])
        self.assertEqual(output, "Geometric")

    def test_WrongInputSequence(self):
        '''
        Checks if for 0 in input 
        output is -1.
        '''
        output = ArithGeo.ArithGeo([0,1,2,3])
        self.assertEqual(output, -1)

    def test_InputContainsSameElements(self):
        '''
        Checks if for same elements in input 
        output is "Input array contains same elements".
        '''
        output = ArithGeo.ArithGeo([1,1,1,1])
        self.assertEqual(output, "Input array contains same elements")

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()