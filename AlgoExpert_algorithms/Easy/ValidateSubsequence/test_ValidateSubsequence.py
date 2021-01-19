'''
Unittests for ValidateSubsequence.py
January 2021 Jakub Kazimierski
'''

import unittest
import ValidateSubsequence

class test_ValidateSubsequence(unittest.TestCase):    
    '''
    Class with unittests for ValidateSubsequence.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        pass
        input_arr = [5, 1, 22, 25, 6, -1, 8, 10]
        input_sequence  = [1, 6, -1, 10]        
        output = ValidateSubsequence.validateSubsequence(input_arr, input_sequence)
        self.assertEqual(output, True)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()