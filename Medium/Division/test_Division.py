'''
Unittests for Division.py
December 2020 Jakub Kazimierski
'''

import unittest
import Division

class test_Division(unittest.TestCase):    
    '''
    Class with unittests for Division.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = Division.Division(12, 16 )
        self.assertEqual(output, 4)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()