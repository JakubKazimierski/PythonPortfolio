'''
Unittests for PermutationStep.py
December 2020 Jakub Kazimierski
'''

import unittest
import PermutationStep

class test_PermutationStep(unittest.TestCase):    
    '''
    Class with unittests for PermutationStep.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PermutationStep.PermutationStep(123)
        self.assertEqual(output, 132)

    def test_NoGreaterPermutation(self):
        '''
        Checks if returned output is equal -1 if there is no greater permutation.
        '''
        output = PermutationStep.PermutationStep(222)
        self.assertEqual(output, -1)
    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()