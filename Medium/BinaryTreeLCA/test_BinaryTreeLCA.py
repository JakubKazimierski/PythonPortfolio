'''
Unittests for BinaryTreeLCA.py
December 2020 Jakub Kazimierski
'''

import unittest
import BinaryTreeLCA

class test_BinaryTreeLCA(unittest.TestCase):    
    '''
    Class with unittests for BinaryTreeLCA.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["[12, 5, 9, 6, 2, 0, 8, #, #, 7, 4, #, #, #, #]", "6", "4"]
        output = BinaryTreeLCA.BinaryTreeLCA(input_val)
        self.assertEqual(output, '5')

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()