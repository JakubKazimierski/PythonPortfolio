'''
Unittests for GroupTotals.py
December 2020 Jakub Kazimierski
'''

import unittest
import GroupTotals

class test_GroupTotals(unittest.TestCase):    
    '''
    Class with unittests for GroupTotals.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = GroupTotals.GroupTotals(["B:-1", "A:1", "B:3", "A:5"] )
        self.assertEqual(output, "A:6,B:2")

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()