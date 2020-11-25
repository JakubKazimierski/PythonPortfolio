'''
Unittests for SelectionSort.py
November 2020 Jakub Kazimierski
'''

import unittest
import SelectionSort

class test_SelectionSort(unittest.TestCase):
    '''
    Class contains unittests for QuickSort.py
    '''
 
    def test_TestOutputArray(self):
        '''
        Checks if array is sorted.
        '''
        output = SelectionSort.SelectionSort([3,4,2,5,1])
        self.assertEqual(output, [1,2,3,4,5])

    def test_TestOneDigitArray(self):
        '''
        Checks if function does not return error for one digit.
        '''
        output = SelectionSort.SelectionSort([3])
        self.assertEqual(output, [3])        

    def test_CorrectInput(self):
        '''
        Checks if input is correct.
        '''
        output = SelectionSort.SelectionSort(123)
        self.assertEqual(output, -1)

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()