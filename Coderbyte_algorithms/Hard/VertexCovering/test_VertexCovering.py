'''
Unittests for VertexCovering.py
January 2021 Jakub Kazimierski
'''

import unittest
import VertexCovering

class test_VertexCovering(unittest.TestCase):    
    '''
    Class with unittests for VertexCovering.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C,B)"]
        output = VertexCovering.VertexCovering(input_val)
        self.assertEqual(output, "yes")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()