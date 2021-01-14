'''
Unittests for BinaryConverter.py
December 2020 Jakub Kazimierski
'''

import unittest
import BinaryConverter

class test_BinaryConverter(unittest.TestCase):    
    '''
    Class with unittests for BinaryConverter.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = BinaryConverter.BinaryConverter("1000")
        self.assertEqual(output, 8)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()