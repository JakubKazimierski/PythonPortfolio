'''
Unittests for ArrayRotation.py
January 2021 Jakub Kazimierski
'''

import unittest
import ArrayRotation

class test_ArrayRotation(unittest.TestCase):    
    '''
    Class with unittests for ArrayRotation.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = [2, 3, 4, 1, 6, 10]
        output = ArrayRotation.ArrayRotation(input_val)
        self.assertEqual(output, "4161023")
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()