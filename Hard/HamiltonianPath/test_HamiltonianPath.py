'''
Unittests for HamiltonianPath.py
January 2021 Jakub Kazimierski
'''

import unittest
import HamiltonianPath

class test_HamiltonianPath(unittest.TestCase):    
    '''
    Class with unittests for HamiltonianPath.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val =  ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C,A,D,B)"]
        output = HamiltonianPath.HamiltonianPath(input_val)
        self.assertEqual(output, "yes")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()