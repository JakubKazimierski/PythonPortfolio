'''
Unittests for SearchInSortedMatrix.py
February 2021 Jakub Kazimierski
'''


import unittest
from SearchInSortedMatrix import searchInSortedMatrix

class test_SearchInSortedMatrix(unittest.TestCase):    
    '''
    Class with unittests for SearchInSortedMatrix.py
    '''

    def SetUp(self):
        '''
        Set Up input matrix.
        '''
        
        self.target = 44
        self.matrix = [
                        [1, 4, 7, 12, 15, 1000],
                        [2, 5, 19, 31, 32, 1001],
                        [3, 8, 24, 33, 35, 1002],
                        [40, 41, 42, 44, 45, 1003],
                        [99, 100, 103, 106, 128, 1004],
                       ]

        return self.target, self.matrix

    # region Unittests
    def test_Iterative_method(self):   
        '''
        Checks if output is correct.
        '''
        
        target, matrix = self.SetUp()
        
        output = searchInSortedMatrix(matrix, target)
        self.assertEqual(output, [3, 3])

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()