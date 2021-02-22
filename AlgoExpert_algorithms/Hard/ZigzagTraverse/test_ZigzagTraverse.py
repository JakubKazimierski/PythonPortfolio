'''
Unittests for ZigzagTraverse.py
February 2021 Jakub Kazimierski
'''

import unittest
from ZigzagTraverse import zigzagTraverse

class test_ZigzagTraverse(unittest.TestCase):    
    '''
    Class with unittests for ZigzagTraverse.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input_arr = [
                            [1, 3, 4, 10],
                            [2, 5, 9, 11],
                            [6, 8, 12, 15],    
                            [7, 13, 14, 16],
                        ]

        self.output = [1, 2, 3 ,4 ,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        return self.input_arr, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr, output_arr  = self.setUp()
        output = zigzagTraverse(input_arr)
        self.assertEqual(output, output_arr)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()