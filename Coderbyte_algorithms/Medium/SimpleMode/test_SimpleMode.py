'''
Unittetst from SimpleMode.py
December 2020 Jakub Kazimierski
'''

import unittest
import SimpleMode

class test_SimpleMode(unittest.TestCase):    
    '''
    Class with unittests for SimpleMode.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SimpleMode.SimpleMode([5, 10, 10, 6, 5])
        self.assertEqual(output, 5)

    def test_NoMode(self):
        '''
        Checks if returned output is equal -1 if array has no mode.
        '''
        output = SimpleMode.SimpleMode([5, 10, 6])
        self.assertEqual(output, -1)


    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()