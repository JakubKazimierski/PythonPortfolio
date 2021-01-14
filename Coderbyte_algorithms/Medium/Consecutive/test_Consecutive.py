'''
Unittests for Consecutive.py
December 2020 Jakub Kazimierski
'''

import unittest
import Consecutive

class test_Consecutive(unittest.TestCase):    
    '''
    Class with unittests for Consecutive.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = Consecutive.Consecutive([4, 8, 6])
        self.assertEqual(output, 2)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()