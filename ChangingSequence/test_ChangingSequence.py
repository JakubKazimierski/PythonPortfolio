'''
Unittests for ChangingSequence.py
November 2020 Jakub Kazimierski
'''

import unittest
import ChangingSequence


class test_ChangingSequence(unittest.TestCase):
    '''
    Class contains unittests for ChangingSequence.py
    '''

    #region Unittests

    def test_ExpectedOutputSequenceStopDecreasing(self):
        '''
        check if returned number
        is index where sequence stops decreasing
        '''
        output = ChangingSequence.ChangingSequence([5, 4, 3, 2, 10, 11])
        self.assertEqual(output, 3)
    
    
    def test_ExpectedOutputSequenceStopIncreasing(self):
        '''
        check if returned number
        is index where sequence stops increasing
        '''
        output = ChangingSequence.ChangingSequence([2, 10, 11, 5, 4, 3])
        self.assertEqual(output, 2)

    def test_OneSequenceIsIncreasing(self):
        '''
        check if for one sequence
        output is -1
        '''
        output = ChangingSequence.ChangingSequence([-4, -2, 9, 10])
        self.assertEqual(output, -1)
    
    def test_OneSequenceIsDecreasing(self):
        '''
        check if for one sequence
        output is -1
        '''
        output = ChangingSequence.ChangingSequence([10, 9, -2, -4])
        self.assertEqual(output, -1)

    def test_InputIsEmpty(self):
        '''
        check if assertion in function
        catches empty input
        '''
        output = ChangingSequence.ChangingSequence([])
        self.assertEqual(output, "Input is empty")

    def test_InputHasWrongType(self):
        '''
        check if assertion in function
        catches wrong type in input
        '''
        output = ChangingSequence.ChangingSequence([10,9,"8"])
        self.assertEqual(output, "Wrong Input Type")

    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()