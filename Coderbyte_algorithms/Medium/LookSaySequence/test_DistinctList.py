'''
Unittests for DistinctList.py
December 2020 Jakub Kazimierski
'''

import unittest
import DistinctList

class test_DistinctList(unittest.TestCase):    
    '''
    Class with unittests for DistinctList.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = DistinctList.DistinctList([1, 2, 2, 2, 3])
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()