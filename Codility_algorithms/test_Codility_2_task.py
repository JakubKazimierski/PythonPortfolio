'''
Unittests for Codility_2_task.py
February 2021 Jakub Kazimierski
'''

import unittest
from Codility_2_task import solution

class test_Codility_2_task(unittest.TestCase):    
    '''
    Class with unittests for Codility_2_task.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.arrayOne = [1, 3, 4, 2, 2, 2, 1, 1, 2]
        
        self.output = True

        return self.arrayOne, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        arrayOne, output = self.setUp()
        output_method = solution(arrayOne)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()