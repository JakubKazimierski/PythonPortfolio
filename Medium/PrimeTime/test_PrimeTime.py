'''
Unittests for PrimeTime.py
December 2020 Jakub Kazimierski
'''

import unittest
import PrimeTime

class test_PrimeTime(unittest.TestCase):    
    '''
    Class with unittests for PrimeTime.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PrimeTime.PrimeTime(19)
        self.assertEqual(output, "true")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = PrimeTime.PrimeTime("11")
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()