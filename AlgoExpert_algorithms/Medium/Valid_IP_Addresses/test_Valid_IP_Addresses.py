'''
Unittests for Valid_IP_Addresses.py
February 2021 Jakub Kazimierski
'''

import unittest
import Valid_IP_Addresses

class test_Valid_IP_Addresses(unittest.TestCase):    
    '''
    Class with unittests for Valid_IP_Addresses.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        # input_arr  = [12, 3, 1, 2, -6, 5, -8, 6]
        # target = 0
        # output = Valid_IP_Addresses.valid_IP_Addresses(input_arr, target)
        # self.assertEqual(output, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()