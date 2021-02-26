'''
Unittests for Codility_1_task.py
February 2021 Jakub Kazimierski
'''

import unittest
from Codility_1_task import solution

class test_Codility_1_task(unittest.TestCase):    
    '''
    Class with unittests for Codility_1_task.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.TimeOne = "15:15:00"
        self.TimeTwo = "15:15:12"
        self.output = 1

        return self.TimeOne, self.TimeTwo, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        TimeOne, TimeTwo, output = self.setUp()
        output_method = solution(TimeOne, TimeTwo)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()