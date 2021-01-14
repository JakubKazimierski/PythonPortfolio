'''
Unittests for LineOrdering.py
January 2021 Jakub Kazimierski
'''

import unittest
import LineOrdering

class test_LineOrdering(unittest.TestCase):    
    '''
    Class with unittests for LineOrdering.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LineOrdering.LineOrdering(["J>B","B<S","D>J"])
        self.assertEqual(output, 3)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()