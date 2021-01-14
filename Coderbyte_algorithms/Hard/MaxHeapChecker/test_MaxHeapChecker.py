'''
Unittests for MaxHeapChecker.py
January 2021 Jakub Kazimierski
'''

import unittest
import MaxHeapChecker

class test_MaxHeapChecker(unittest.TestCase):    
    '''
    Class with unittests for MaxHeapChecker.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = [10,19,52,13,16]
        output = MaxHeapChecker.MaxHeapChecker(input_val)
        self.assertEqual(output, "19,52")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()