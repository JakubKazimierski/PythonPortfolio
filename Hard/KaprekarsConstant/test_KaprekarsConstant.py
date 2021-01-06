'''
Unittests for KaprekarsConstant.py
January 2021 Jakub Kazimierski
'''

import unittest
import KaprekarsConstant

class test_KaprekarsConstant(unittest.TestCase):    
    '''
    Class with unittests for KaprekarsConstant.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = KaprekarsConstant.KaprekarsConstant(2111)
        self.assertEqual(output, 5)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()