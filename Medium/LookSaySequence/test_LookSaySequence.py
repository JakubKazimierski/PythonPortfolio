'''
Unittests for LookSaySequence.py
December 2020 Jakub Kazimierski
'''

import unittest
import LookSaySequence

class test_LookSaySequence(unittest.TestCase):    
    '''
    Class with unittests for LookSaySequence.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LookSaySequence.LookSaySequence(1211)
        self.assertEqual(output, 111221)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()