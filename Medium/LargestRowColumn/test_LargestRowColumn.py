'''
Unittests for LargestRowColumn.py
December 2020 Jakub Kazimierski
'''

import unittest
import LargestRowColumn

class test_LargestRowColumn(unittest.TestCase):    
    '''
    Class with unittests for LargestRowColumn.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LargestRowColumn.LargestRowColumn(["345", "326", "221"])
        self.assertEqual(output, 12)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()