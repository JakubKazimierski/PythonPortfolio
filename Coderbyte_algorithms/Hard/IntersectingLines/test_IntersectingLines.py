'''
Unittests for IntersectingLines.py
January 2021 Jakub Kazimierski
'''

import unittest
import IntersectingLines

class test_IntersectingLines(unittest.TestCase):    
    '''
    Class with unittests for IntersectingLines.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val =  ["(3,0)","(1,4)","(0,-3)","(2,3)"]
        output = IntersectingLines.IntersectingLines(input_val)
        self.assertEqual(output, "(9/5,12/5)")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()