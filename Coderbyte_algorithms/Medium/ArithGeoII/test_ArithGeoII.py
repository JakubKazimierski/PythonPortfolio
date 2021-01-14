'''
Unittests for ArithGeoII.py
December 2020 Jakub Kazimierski
'''

import unittest
import ArithGeoII

class test_ArithGeoII(unittest.TestCase):    
    '''
    Class with unittests for ArithGeoII.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ArithGeoII.ArithGeoII([2, 4, 6, 8])
        self.assertEqual(output, "Arithmetic")

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()