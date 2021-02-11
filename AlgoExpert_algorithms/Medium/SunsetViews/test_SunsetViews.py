'''
Unittests for SunsetViews.py
February 2021 Jakub Kazimierski
'''

import unittest
from SunsetViews import sunsetViews

class test_SunsetViews(unittest.TestCase):    
    '''
    Class with unittests for SunsetViews.py
    '''

    def setUp(self):
        '''
        SetUp array for tests.
        '''

        self.buildings = [3, 5, 4, 4, 3, 1 ,3, 2]
        self.direction = 'EAST'
        self.output = [1, 3, 6, 7]

        return self.buildings, self.direction, self.output 

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        buildings, direction, proper_out = self.setUp()

        output = sunsetViews(buildings, direction)

        self.assertEqual(output, proper_out)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()