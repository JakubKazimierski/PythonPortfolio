'''
Unittests for NumberStream.py
December 2020 Jakub Kazimierski
'''


import unittest
import NumberStream

class test_NumberStream(unittest.TestCase):    
    '''
    Class with unittests for NumberStream.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = NumberStream.NumberStream("6539923335")
        self.assertEqual(output, "true")

    
    def test_ShortInput(self):
        '''
        Checks if returned output is false for one digit in given input.
        '''
        output = NumberStream.NumberStream("6")
        self.assertEqual(output, "false")

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()