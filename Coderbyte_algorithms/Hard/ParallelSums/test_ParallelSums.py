'''
Unittests for ParallelSums.py
January 2021 Jakub Kazimierski
'''

import unittest
import ParallelSums

class test_ParallelSums(unittest.TestCase):    
    '''
    Class with unittests for ParallelSums.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ParallelSums.ParallelSums([16, 22, 35, 8, 20, 1, 21, 11])
        self.assertEqual(output, "1,11,20,35,8,16,21,22")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()