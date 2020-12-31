'''
Unittests for TreeConstructorTwo.py
December 2020 Jakub Kazimierski
'''

import unittest
import TreeConstructorTwo

class test_TreeConstructorTwo(unittest.TestCase):    
    '''
    Class with unittests for TreeConstructorTwo.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = TreeConstructorTwo.TreeConstructorTwo(["(1,2)", "(2,3)", "(3,1)", "(5,4)"])
        self.assertEqual(output, "false")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()