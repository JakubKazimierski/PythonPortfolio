'''
Unittests for NumberSearch.py
December 2020 Jakub Kazimierski
'''

import unittest
import NumberSearch

class test_NumberSearch(unittest.TestCase):    
    '''
    Class with unittests for NumberSearch.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = NumberSearch.NumberSearch("Hello6 9World 2, Nic8e D7ay!")
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()