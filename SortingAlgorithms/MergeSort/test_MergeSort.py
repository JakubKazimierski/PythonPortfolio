'''
Unittests for MergeSort.py
November 2020 Jakub Kazimierski
'''

import unittest
import MergeSort

class test_MergeSort(unittest.TestCase):
    '''
    Class contains unittests for MergeSort.py
    '''
 
    def test_TestOutputArray(self):
        '''
        Checks if array is sorted.
        '''
        output = MergeSort.MergeSort([1,4,2,3])
        self.assertEqual(output, [1,2,3,4])

    def test_CorrectInput(self):
        '''
        Checks if input is correct.
        '''
        output = MergeSort.MergeSort(123)
        self.assertEqual(output, -1)


if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()