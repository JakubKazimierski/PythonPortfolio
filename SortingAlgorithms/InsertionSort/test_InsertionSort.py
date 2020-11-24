'''
Unittests for InsertionSort.py
November 2020 Jakub Kazimierski
'''

import unittest
import InsertionSort

class test_InsertionSort(unittest.TestCase):
    '''
    Class contains unittests for Insertionsort.py
    '''

    def test_TestOutputArray(self):
        '''
        Checks if array is sorted.
        '''
        output = InsertionSort.InsertionSort([3,4,2,5,1])
        self.assertEqual(output, [1,2,3,4,5])

    def test_CorrectInput(self):
        '''
        Checks if input is correct.
        '''
        output = InsertionSort.InsertionSort(123)
        self.assertEqual(output, -1)


if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()