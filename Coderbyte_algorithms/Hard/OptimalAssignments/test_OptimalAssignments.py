'''
Unittests for OptimalAssignments.py
December 2020 Jakub Kazimierski
'''

import unittest
import OptimalAssignments

class test_OptimalAssignments(unittest.TestCase):    
    '''
    Class with unittests for OptimalAssignments.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''   
        output = OptimalAssignments.OptimalAssignments(["(5,4,2)","(12,4,3)","(3,4,13)"])
        self.assertEqual(output, "(1-3)(2-2)(3-1)")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()