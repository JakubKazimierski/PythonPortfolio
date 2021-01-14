'''
Unittests for BlackjackHighest.py
January 2021 Jakub Kazimierski
'''

import unittest
import BlackjackHighest

class test_BlackjackHighest(unittest.TestCase):    
    '''
    Class with unittests for BlackjackHighest.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["four","ace","ten"]
        output = BlackjackHighest.BlackjackHighest(input_val)
        self.assertEqual(output, "below ten")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()