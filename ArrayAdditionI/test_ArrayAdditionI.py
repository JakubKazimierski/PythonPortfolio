'''
Unittests for ArrayAdditionI.py
November 2020 Jakub Kazimierski
'''

import unittest
import ArrayAdditionI

class test_ArrayAdditionI(unittest.TestCase):
    '''
    Class contains unittests for ArrayAdditionI.py
    '''

    #region Unittests
    def test_TrueOutput(self):
        '''
        Checks if it is possible to get sum which is equal to max element,
        and this sum is created from one of combinations of elements, 
        in array without max element,
        output will be true.
        '''
        output = ArrayAdditionI.ArrayAdditionI([1,2,3,4])
        self.assertEqual(output, "true")
    
    def test_FalseOutput(self):
        '''
        Checks if it is imposiible to get sum which is equal to max element,
        and this sum is created from one of combinations of elements, 
        in array without max element,
        output will be false.
        '''
        output = ArrayAdditionI.ArrayAdditionI([1,2,4])
        self.assertEqual(output, "false")

    def test_TrueOutputWithNegatives(self):
        '''
        Checks if it is possible to get sum which is equal to max element,
        and this sum is created from one of combinations of elements
        which containing negative numbers, 
        in array without max element,
        output will be true.
        '''
        output = ArrayAdditionI.ArrayAdditionI([2,-1,7,6])
        self.assertEqual(output, "true")

    def test_ExceptionType(self):
        '''
        Checka if for wrong type input, output is -1.
        '''
        output = ArrayAdditionI.ArrayAdditionI([2,"1",7,6])
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()