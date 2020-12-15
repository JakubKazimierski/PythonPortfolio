'''
Unittests for ArrayAddition.py
December 2020 Jakub Kazimierski
'''

import unittest
import ArrayAddition

class test_ArrayAddition(unittest.TestCase):    
    '''
    Class with unittests for ArrayAddition.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ArrayAddition.ArrayAddition([4, 6, 23, 10, 1, 3])
        self.assertEqual(output, "true")

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()