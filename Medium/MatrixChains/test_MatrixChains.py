'''
Unittests for MatrixChains.py
December 2020 Jakub Kazimierski
'''

import unittest
import MatrixChains

class test_MatrixChains(unittest.TestCase):    
    '''
    Class with unittests for MatrixChains.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MatrixChains.MatrixChains([1, 2, 3, 4])
        self.assertEqual(output, 18)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()