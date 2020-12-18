'''
Unittests for ThreeFiveMultiples.py
December 2020 Jakub Kazimierski
'''

import unittest
import ThreeFiveMultiples

class test_ThreeFiveMultiples(unittest.TestCase):    
    '''
    Class with unittests for ThreeFiveMultiples.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ThreeFiveMultiples.ThreeFiveMultiples(16)
        self.assertEqual(output, 60)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()