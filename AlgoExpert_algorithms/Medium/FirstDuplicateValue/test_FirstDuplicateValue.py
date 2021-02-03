'''
Unittests for FirstDuplicateValue.py
February 2021 Jakub Kazimierski
'''

import unittest
import FirstDuplicateValue

class test_FirstDuplicateValue(unittest.TestCase):    
    '''
    Class with unittests for FirstDuplicateValue.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr  = [2, 1, 5, 2, 3, 3, 4]
        output = FirstDuplicateValue.firstDuplicateValue(input_arr)
        self.assertEqual(output, 2)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()