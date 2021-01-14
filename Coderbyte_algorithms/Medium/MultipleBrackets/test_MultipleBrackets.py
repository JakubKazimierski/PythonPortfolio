'''
Unittests for MultipleBrackets.py
December 2020 Jakub Kazimierski
'''

import unittest
import MultipleBrackets

class test_MultipleBrackets(unittest.TestCase):    
    '''
    Class with unittests for MultipleBrackets.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MultipleBrackets.MultipleBrackets("(hello [world])(!)")
        self.assertEqual(output, "1 3")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()