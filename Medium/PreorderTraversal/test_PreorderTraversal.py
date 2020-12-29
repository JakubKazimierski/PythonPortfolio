'''
Unittests for PreorderTraversal.py
December 2020 Jakub Kazimierski
'''

import unittest
import PreorderTraversal

class test_PreorderTraversal(unittest.TestCase):    
    '''
    Class with unittests for PreorderTraversal.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["5", "2", "6", "1", "9", "#", "8", "#", "#", "#", "#", "4", "#"] 
        output = PreorderTraversal.PreorderTraversal(input_val)
        self.assertEqual(output, "5 2 1 9 6 8 4")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()