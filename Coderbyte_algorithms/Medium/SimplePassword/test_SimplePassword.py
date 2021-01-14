'''
Unittests for SimplePassword.py
December 2020 Jakub Kazimierski
'''

import unittest
import SimplePassword

class test_SimplePassword(unittest.TestCase):    
    '''
    Class with unittests for SimplePassword.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SimplePassword.SimplePassword("apple!M7")
        self.assertEqual(output, "true")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()