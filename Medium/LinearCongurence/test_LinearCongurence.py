'''
Unittests for LinearCongurence.py
December 2020 Jakub Kazimierski
'''

import unittest
import LinearCongurence

class test_LinearCongurence(unittest.TestCase):    
    '''
    Class with unittests for LinearCongurence.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LinearCongurence.LinearCongruence("32x = 8 (mod 4)")
        self.assertEqual(output, 4)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()