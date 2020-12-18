'''
Unittests for CoinDeterminer.py
December 2020 Jakub Kazimierski
'''

import unittest
import CoinDeterminer

class test_CoinDeterminer(unittest.TestCase):    
    '''
    Class with unittests for CoinDeterminer.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = CoinDeterminer.CoinDeterminer(25)
        self.assertEqual(output, 3)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()