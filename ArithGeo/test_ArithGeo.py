'''
Unittests for ArithGeo.py
November 2020 Jakub Kazimierski
'''

import unittest
import ArithGeo

class test_ArithGeo(unittest.TestCase):
    '''
    class contains unittests for
    ArithGeo.py
    '''

    #region Unittests
    def test_AithmeticOutput(self):
        '''
        check if for arithmetic seq
        output is "Arithmetic"
        '''
        output = ArithGeo.ArithGeo([1,2,3,4])
        self.assertEqual(output, "Arithmetic")

    def test_GeometricOutput(self):
        '''
        check if output for geometric seq
        is "Geometric"
        '''
        output = ArithGeo.ArithGeo([1,2,4,8])
        self.assertEqual(output, "Geometric")

    def test_NegativeAithmeticOutput(self):
        '''
        check if for negative arithmetic seq
        output is "Arithmetic"
        '''
        output = ArithGeo.ArithGeo([-1,-2,-3,-4])
        self.assertEqual(output, "Arithmetic")

    def test_NegativeGeometricOutput(self):
        '''
        check if for negative num in geometric seq
        output is "Geometric"
        '''
        output = ArithGeo.ArithGeo([-1,2,-4,8])
        self.assertEqual(output, "Geometric")

    def test_WrongInputSequence(self):
        '''
        check if for wrong input seq
        output is -1
        '''
        output = ArithGeo.ArithGeo([-1,-1,0,0])
        self.assertEqual(output, -1)

    #endregion
if __name__ == "__main__":
    '''
    main method of unittest class
    '''
    unittest.main()