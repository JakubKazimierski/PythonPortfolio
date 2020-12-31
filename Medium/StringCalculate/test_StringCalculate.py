'''
Unittests for StringCalculate.py
December 2020 Jakub Kazimierski
'''

import unittest
import StringCalculate

class test_StringCalculate(unittest.TestCase):    
    '''
    Class with unittests for StringCalculate.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StringCalculate.StringCalculate("((5-2*0-9*0)*0)+5**6")
        self.assertEqual(output, 15625)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()