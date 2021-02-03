'''
Unittests for TaskAssignment.py
February 2021 Jakub Kazimierski
'''

import unittest
import TaskAssignment

class test_TaskAssignment(unittest.TestCase):    
    '''
    Class with unittests for TaskAssignment.py
    '''

    def setUp(self):
        '''
        SetUp matrix for tests.
        '''

        self.input_k = 3
        self.input_arr = [1, 3, 5, 3, 1, 4]
        self.output = [[0, 2], [4, 5], [1, 3]]

        return self.input_k, self.input_arr, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        input_k, input_arr, proper_output = self.setUp()
        output = TaskAssignment.taskAssignment(input_k, input_arr)
        self.assertEqual(output, proper_output)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()