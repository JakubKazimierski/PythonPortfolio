'''
Unittests for KnapsackProblem.py
March 2021 Jakub Kazimierski
'''

import unittest
from KnapsackProblem import knapsackProblem

class test_KnapsackProblem(unittest.TestCase):    
    '''
    Class with unittests for KnapsackProblem.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_items = [[1, 2], [4, 3], [5, 6], [6, 7]]
        self.capacity = 10
        self.output = [10, [1, 3]]

        return self.input_items, self.capacity, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        items, capacity, output = self.setUp()
        output_method = knapsackProblem(items, capacity)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()