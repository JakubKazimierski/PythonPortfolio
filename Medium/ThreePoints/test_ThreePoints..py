'''
Unittestst for ThreePoints.py
December 2020 Jakub Kazimierski
'''

import unittest
import ThreePoints

class test_ThreePoints(unittest.TestCase):    
    '''
    Class with unittests for ThreePoints.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ThreePoints.ThreePoints(["(1,1)", "(3,3)", "(2,0)"])
        self.assertEqual(output, "right")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()