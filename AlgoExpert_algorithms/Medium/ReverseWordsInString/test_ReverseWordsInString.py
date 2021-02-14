'''
Unittests for ReverseWordsInString.py
February 2021 Jakub Kazimierski
'''

import unittest
from ReverseWordsInString import reverseWordsInString

class test_ReverseWordsInString(unittest.TestCase):    
    '''
    Class with unittests for ReverseWordsInString.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input = "AlgoExpert is the best!"
        self.output = "best! the is AlgoExpert"

        return self.input, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_str, output_arr  = self.setUp()
        output = reverseWordsInString(input_str)
        self.assertEqual(output, output_arr)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()