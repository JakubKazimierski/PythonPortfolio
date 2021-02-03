'''
Unittests for CycleInGraph.py
February 2021 Jakub Kazimierski
'''

import unittest
import CycleInGraph

class test_CycleInGraph(unittest.TestCase):    
    '''
    Class with unittests for CycleInGraph.py
    '''

    def setUp(self):
        '''
        SetUp matrix for tests.
        '''
        self.input = [
            [1, 3],
            [2, 3, 4],
            [0],
            [],
            [2, 5],
            [],
        ]


        return self.input

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_graph = self.setUp()
        output = CycleInGraph.cycleInGraph(input_graph)
        self.assertEqual(output, True)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()