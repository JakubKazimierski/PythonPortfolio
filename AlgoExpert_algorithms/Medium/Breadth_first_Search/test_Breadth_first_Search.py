'''
Unittests for Breadth_first_Search.py
January 2021 Jakub Kazimierski
'''

import unittest
from Breadth_first_Search import Node, setUp

class test_SingleCycleCheck(unittest.TestCase):    
    '''
    Class with unittests for SingleCycleCheck.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        graph = setUp()
        out_array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        output = graph.breadthFirstSearch([])
        self.assertEqual(output, out_array)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()