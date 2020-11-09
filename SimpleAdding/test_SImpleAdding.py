'''
Unittests for SimpleAdding
October 2020 Jakub Kazimierski
'''

import unittest
import SImpleAdding

class test_SImpleAdding(unittest.TestCase):
    '''
    class with unittests
    for SimpleAdding
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        checks if output is as expected
        '''
        output = SImpleAdding.SimpleAdding(12)
        self.assertEqual(output, 78)

    def test_NotProperInput(self):
        '''
        checks if output is -1
        when input is wrong type
        '''
        output = SImpleAdding.SimpleAdding("12")
        self.assertEqual(output, -1)
    #endregion

if __name__ == "__main__":
    '''
    main method for unittests class
    '''
    unittest.main()