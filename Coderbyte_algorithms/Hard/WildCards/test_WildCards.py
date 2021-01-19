'''
Unittests for WildCards.py
January 2021 Jakub Kazimierski
'''

import unittest
import WildCards

class test_WildCards(unittest.TestCase):    
    '''
    Class with unittests for WildCards.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = "$****{4}+++$ 8fffbbbeeerrrrmkou"
        output = WildCards.WildCards(input_val)
        self.assertEqual(output, "false")
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()