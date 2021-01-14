'''
Unittests for ShortestPath.py
January 2021 Jakub Kazimierski
'''

import unittest
import ShortestPath

class test_ShortestPath(unittest.TestCase):    
    '''
    Class with unittests for ShortestPath.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''   
        input_val = ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]
        output = ShortestPath.ShortestPath(input_val)
        self.assertEqual(output, "A-E-D-F-G")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()