'''
Unittests for SimpleEvens.py
December 2020 Jakub Kazimierski
'''

import unittest
import SimpleEvens

class test_SimpleEvens(unittest.TestCase):    
    '''
    Class with unittests for SimpleEvens.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SimpleEvens.SimpleEvens(4602225 )
        self.assertEqual(output, "false")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''        
        output = SimpleEvens.SimpleEvens("a")
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()