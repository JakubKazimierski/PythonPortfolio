'''
Unittests for ArrayAdditionI.py
November 2020 Jakub Kazimierski
'''

import unittest
import ArrayAdditionI

class test_ArrayAdditionI(unittest.TestCase):
    '''
    class contains unittests for ArrayAdditionI.py
    '''

    #region Unittests
    def test_TrueOutput(self):
        '''
        check if for possible sum of elements to max elem
        which are less than max elem
        output will be true
        '''
        output = ArrayAdditionI.ArrayAdditionI([1,2,3,4])
        self.assertEqual(output, "true")
    
    def test_FalseOutput(self):
        '''
        check if it is not possible to sum to max elem elements
        which are less than max elem
        output will be false
        '''
        output = ArrayAdditionI.ArrayAdditionI([1,2,4])
        self.assertEqual(output, "false")

    def test_TrueOutputWithNegatives(self):
        '''
        check if for possible to sum to max elem elements
        which are less than max elem, and some of them are negatives
        output will be true
        '''
        output = ArrayAdditionI.ArrayAdditionI([2,-1,7,6])
        self.assertEqual(output, "true")

    def test_ExceptionType(self):
        '''
        check if for wrong type output is -1
        '''
        output = ArrayAdditionI.ArrayAdditionI([2,"1",7,6])
        self.assertEqual(output, -1)



    #endregion

if __name__ == "__main__":
    '''
    main method for uittests
    '''
    unittest.main()