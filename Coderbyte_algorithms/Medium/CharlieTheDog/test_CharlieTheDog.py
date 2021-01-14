'''
Unittests for CharlieTheDog.py
December 2020 Jakub Kazimierski
'''

import unittest
import CharlieTheDog

class test_CharlieTheDog(unittest.TestCase):    
    '''
    Class with unittests for CharlieTheDog.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = CharlieTheDog.CharlieTheDog(["FOOF", "OCOO", "OOOH", "FOOO"])
        self.assertEqual(output, 11)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()