'''
Unittests for ConvexHullPoints.py
January 2021 Jakub Kazimierski
'''

import unittest
import ConvexHullPoints

class test_ConvexHullPoints(unittest.TestCase):    
    '''
    Class with unittests for ConvexHullPoints.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["(0,1)", "(3,6)", "(2,2)", "(0,7)"] 
        output = ConvexHullPoints.ConvexHullPoints(input_val)
        self.assertEqual(output, 3)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()