'''
Unittests for ArrayCouples.py
January 2021 Jakub Kazimierski
'''

import unittest
import ArrayCouples

class test_ArrayCouples(unittest.TestCase):    
    '''
    Class with unittests for ArrayCouples.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = [2,1,1,2,3,3]
        output = ArrayCouples.ArrayCouples(input_val)
        self.assertEqual(output, "3,3")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()