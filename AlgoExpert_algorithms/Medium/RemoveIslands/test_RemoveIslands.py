'''
Unittests for RemoveIslands.py
February 2021 Jakub Kazimierski
'''

import unittest
import RemoveIslands

class test_RemoveIslands(unittest.TestCase):    
    '''
    Class with unittests for RemoveIslands.py
    '''

    def setUp(self):
        '''
        SetUp matrix for tests.
        '''
        self.matrix = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]

        self.out_matrix = [
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]


        return self.matrix, self.out_matrix

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        input_matrix, output_matrix = self.setUp()
        output = RemoveIslands.removeIslands(input_matrix)
        self.assertEqual(output, output_matrix)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()