'''
Unittests for StringMerge.py
December 2020 Jakub Kazimierski
'''

import unittest
import StringMerge

class test_StringMerge(unittest.TestCase):    
    '''
    Class with unittests for StringMerge.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StringMerge.StringMerge("abc1*kyoo")
        self.assertEqual(output, "akbyco1o")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = StringMerge.StringMerge(12)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()