'''
Unittests for ArrayMinJumps.py
December 2020 Jakub Kazimierski
'''

import unittest
import ArrayMinJumps

class test_ArrayMinJumps(unittest.TestCase):    
    '''
    Class with unittests for ArrayMinJumps.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = [1, 5, 4, 6, 9, 3, 0, 0, 1, 3]
        output = ArrayMinJumps.ArrayMinJumps(input_val)
        self.assertEqual(output, 3)

    def test_NotPossible(self):
        '''
        Checks if returned output is equal -1 if it is not
        possible to reach end of array.
        '''
        input_val = [1, 0, 1]
        output = ArrayMinJumps.ArrayMinJumps(input_val)
        self.assertEqual(output, -1)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()