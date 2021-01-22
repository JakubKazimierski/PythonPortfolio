'''
Unittests for SelectionSort.py
January 2021 Jakub Kazimierski
'''

import unittest
import SelectionSort

class test_SelectionSort(unittest.TestCase):    
    '''
    Class with unittests for SelectionSort.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr  = [8, 5, 2, 9, 5, 6, 3]
        output = SelectionSort.selectionSort(input_arr)
        self.assertEqual(output, [2, 3, 5, 5, 6, 8, 9])
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()