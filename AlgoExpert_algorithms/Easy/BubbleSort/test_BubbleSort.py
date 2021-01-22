'''
Unittests for BubbleSort.py
January 2021 Jakub Kazimierski
'''

import unittest
import BubbleSort

class test_BubbleSort(unittest.TestCase):    
    '''
    Class with unittests for BubbleSort.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        pass
        input_arr  = [8, 5, 2, 9, 5, 6, 3]
        output = BubbleSort.bubbleSort(input_arr)
        self.assertEqual(output, [2, 3, 5, 5, 6, 8, 9])
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()