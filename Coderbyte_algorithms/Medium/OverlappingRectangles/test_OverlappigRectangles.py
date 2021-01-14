'''
Unittests for OverlappingRectangles.py
December 2020 Jakub Kazimierski
'''

import unittest
import OverlappingRectangles

class test_OverlappingRectangles(unittest.TestCase):    
    '''
    Class with unittests for OverlappingRectangles.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = OverlappingRectangles.OverlappingRectangles(["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"])
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()