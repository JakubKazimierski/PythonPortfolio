'''
Unittests for Dijkstra_sAlgorithm.py
March 2021 Jakub Kazimierski
'''

import unittest
from Dijkstra_sAlgorithm import dijkstra_sAlgorithm

class test_Dijkstra_sAlgorithm(unittest.TestCase):    
    '''
    Class with unittests for Dijkstra_sAlgorithm.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.start = 0
        self.input_edges = [
                [[1, 7]],
                [[2, 6], [3, 20], [4, 3]],
                [[3, 14]],
                [[4, 2]],
                [],
                [],
        ]

        self.output = [0, 7, 13, 27, 10, -1]

        return self.start, self.input_edges, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        start, edges, output = self.setUp()
        output_method = dijkstra_sAlgorithm(start, edges)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()