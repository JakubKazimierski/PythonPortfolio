'''
Unittests for BubbleSort.py
November 2020 Jakub Kazimierski
'''

import unittest
import BubbleSort

class test_BubbleSort(unittest.TestCase):
    '''
    Class contains unittests for Bubblesort.py
    '''

    def test_TestOutputArray(self):
        '''
        Checks if array is sorted.
        '''
        output = BubbleSort.BubbleSort([3,4,2,5,1])
        self.assertEqual(output, [1,2,3,4,5])

    def test_TestSortedArray(self):
        '''
        Checks if array is already sorted.
        '''
        output = BubbleSort.BubbleSort([1,2,3,4,5])
        self.assertEqual(output, "Array is already sorted")

    def test_CorrectInput(self):
        '''
        Checks if input is correct.
        '''
        output = BubbleSort.BubbleSort(123)
        self.assertEqual(output, -1)


if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()