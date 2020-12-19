'''
Unittests for ChristmasTree.py
December 2020 Jakub Kazimierski
'''

import unittest
import ChristmasTree

class test_ChristmasTree(unittest.TestCase):    
    '''
    Class with unittests for ChristmasTree.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ChristmasTree.ChristmasTree(10)
        self.assertEqual(output, 0)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()