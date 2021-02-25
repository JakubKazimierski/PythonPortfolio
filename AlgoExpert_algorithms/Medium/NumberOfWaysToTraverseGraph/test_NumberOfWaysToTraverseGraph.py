'''
Unittests for NumberOfWaysToTraverseGraph.py
February 2021 Jakub Kazimierski
'''

import unittest
from NumberOfWaysToTraverseGraph import numberOfWaysToTraverseGraph

class test_NumberOfWaysToTraverseGraph(unittest.TestCase):    
    '''
    Class with unittests for NumberOfWaysToTraverseGraph.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.width = 4
        self.height = 3
        self.output = 10

        return self.width, self.height, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        Input cannot be empty string.
        '''
        width, height, output = self.setUp()
        output_method = numberOfWaysToTraverseGraph(width, height)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()