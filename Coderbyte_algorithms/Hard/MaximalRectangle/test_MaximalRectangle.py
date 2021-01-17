'''
Unittests for MaximalRectangle.py
January 2021 Jakub Kazimierski
'''

import unittest
import MaximalRectangle

class test_MaximalRectangle(unittest.TestCase):    
    '''
    Class with unittests for MaximalRectangle.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val =  ["10100", "10111", "11111", "10010"] 
        output = MaximalRectangle.MaximalRectangle(input_val)
        self.assertEqual(output, 6)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()