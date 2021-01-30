'''
Unittests for LavenshteinDistance.py
January 2021 Jakub Kazimierski
'''

import unittest
from LavenshteinDistance import lavenshteinDistance

class test_LavenshteinDistance(unittest.TestCase):    
    '''
    Class with unittests for LavenshteinDistance.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_str_I = "abc"
        input_str_II = "yabd"
        output = lavenshteinDistance(input_str_I, input_str_II)
        self.assertEqual(output, 2)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()