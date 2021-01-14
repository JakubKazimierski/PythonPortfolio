'''
Unittests for MaxSubarray.py
December 2020 Jakub Kazimierski
'''

import unittest
import MaxSubarray

class test_MaxSubarray(unittest.TestCase):    
    '''
    Class with unittests for MaxSubarray.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MaxSubarray.MaxSubarray([-2, 5, -1, 7, -3])
        self.assertEqual(output, 11)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()