'''
Unittests for HTMLelements.py
December 2020 Jakub Kazimierski
'''

import unittest
import HTMLelements

class test_HTMLelements(unittest.TestCase):    
    '''
    Class with unittests for HTMLelements.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = HTMLelements.HTMLelements("<div><i>hello</i>world</b>")
        self.assertEqual(output, "div")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()