'''
Unittests for ChangingSequenceBetter.py
November 2020 Jakub Kazimierski
'''

import unittest
import ChangingSequenceBetter


class test_ChangingSequence(unittest.TestCase):
    '''
    Class contains unittests for ChangingSequenceBetter.py
    '''

    #region Unittests

    def test_ExpectedOutputSequenceStopDecreasing(self):
        '''
        Checks if number in output
        is index where sequence stops decreasing.
        '''
        output = ChangingSequenceBetter.ChangingSequence([5, 4, 3, 2, 10, 11])
        self.assertEqual(output, 3)
    
    
    def test_ExpectedOutputSequenceStopIncreasing(self):
        '''
        Checks if number in output
        is index where sequence stops increasing.
        '''
        output = ChangingSequenceBetter.ChangingSequence([2, 10, 11, 5, 4, 3])
        self.assertEqual(output, 2)

    def test_OneSequenceIsIncreasing(self):
        '''
        Checks if for one sequence increasing
        output is -1.
        '''
        output = ChangingSequenceBetter.ChangingSequence([-4, -2, 9, 10])
        self.assertEqual(output, -1)
    
    def test_OneSequenceIsDecreasing(self):
        '''
        Checks if for one sequence decreasing
        output is -1.
        '''
        output = ChangingSequenceBetter.ChangingSequence([10, 9, -2, -4])
        self.assertEqual(output, -1)

    def test_InputIsEmpty(self):
        '''
        Checks if assertion loop in function
        catches empty input.
        '''
        output = ChangingSequenceBetter.ChangingSequence([])
        self.assertEqual(output, "Input is empty")

    def test_InputHasWrongType(self):
        '''
        Checks if assertion in function
        catches wrong type in input.
        '''
        output = ChangingSequenceBetter.ChangingSequence([10,9,"8"])
        self.assertEqual(output, "Wrong Input Type")

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()