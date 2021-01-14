'''
Unittests for K_Unique_Characters.py
December 2020 Jakub Kazimierski
'''

import unittest
import K_Unique_Characters

class test_K_Unique_Characters(unittest.TestCase):    
    '''
    Class with unittests for K_Unique_Characters.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = K_Unique_Characters.K_Unique_Characters("3aabacbebebe")
        self.assertEqual(output, "cbebebe")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()