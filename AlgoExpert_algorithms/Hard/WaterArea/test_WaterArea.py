'''
Unittests for WaterArea.py
March 2021 Jakub Kazimierski
'''


import unittest
from WaterArea import waterArea

class test_WaterArea(unittest.TestCase):    
    '''
    Class with unittests for WaterArea.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_arr = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
        self.output = 48

        return self.input_arr, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        heights, output = self.setUp()
        output_method = waterArea(heights)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()