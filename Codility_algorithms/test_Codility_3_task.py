'''
Unittests for Codility_3_task.py
February 2021 Jakub Kazimierski
'''

import unittest
from Codility_3_task import solution

class test_Codility_3_task(unittest.TestCase):    
    '''
    Class with unittests for Codility_3_task.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.arrayOne = [100, 63, 1, 6, 2, 13]
        self.X = 63
        self.Y = 63
        self.output = 5

        return self.arrayOne, self.X, self.Y, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        arrayOne, X, Y, output = self.setUp()
        output_method = solution(X, Y, arrayOne)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()