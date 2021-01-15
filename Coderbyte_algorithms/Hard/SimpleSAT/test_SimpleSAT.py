'''
Unittests for SimpleSAT.py
January 2021 Jakub Kazimierski
'''

import unittest
import SimpleSAT

class test_SimpleSAT(unittest.TestCase):    
    '''
    Class with unittests for SimpleSAT.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SimpleSAT.SimpleSAT("((a&c)&~a)")
        self.assertEqual(output, "no")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()