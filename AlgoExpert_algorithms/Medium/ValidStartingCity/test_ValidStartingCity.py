'''
Unitttests for ValidStartingCity.py
February 2021 Jakub Kazimierski
'''

import unittest
import ValidStartingCity

class test_ValidStartingCity(unittest.TestCase):    
    '''
    Class with unittests for ValidStartingCity.py
    '''

    def setUp(self):
        '''
        SetUp values for tests.
        '''

        self.input_dist = [5, 25, 15, 10, 15]
        self.input_fuel = [1, 2, 1, 0, 3]
        self.mpg = 10
        self.output = 4

        return self.input_dist, self.input_fuel, self.mpg ,self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        input_dist, input_fuel, mpg ,proper_output = self.setUp()
        output = ValidStartingCity.validStartingCity(input_dist, input_fuel, mpg)
        self.assertEqual(output, proper_output)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()