'''
Unittests for BitmapHoles.py
December 2020 Jakub Kazimierski
'''

import unittest
import BitmapHoles

class test_BitmapHoles(unittest.TestCase):    
    '''
    Class with unittests for BitmapHoles.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = BitmapHoles.BitmapHoles( ["10111", "10101", "11101", "11111"])
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()