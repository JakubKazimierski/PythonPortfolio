'''
Unittests for EvenPairs.py
December 2020 Jakub Kazimierski
'''

import unittest
import EvenPairs

class test_EvenPairs(unittest.TestCase):    
    '''
    Class with unittests for EvenPairs.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = "7r5gg812" 
        output = EvenPairs.EvenPairs(input_val)
        self.assertEqual(output, "true")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()