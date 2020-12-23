'''
Unittests for WordSplit.py
December 2020 Jakub Kazimierski
'''

import unittest
import WordSplit

class test_WordSplit(unittest.TestCase):    
    '''
    Class with unittests for WordSplit.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]
        output = WordSplit.WordSplit(input_val)
        self.assertEqual(output, "hello,cat")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()