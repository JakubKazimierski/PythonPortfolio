'''
Unittests for ArrayJumping.py
January 2021 Jakub Kazimierski
'''

import unittest
import ArrayJumping

class test_ArrayJumping(unittest.TestCase):    
    '''
    Class with unittests for ArrayJumping.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ArrayJumping.ArrayJumping([2, 3, 5, 6, 1])
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()