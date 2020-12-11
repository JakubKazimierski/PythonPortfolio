'''
Unittests for StarRating.py
December 2020 Jakub Kazimierski
'''

import unittest
import StarRating

class test_StarRating(unittest.TestCase):    
    '''
    Class with unittests for StarRating.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StarRating.StarRating("4.5")
        self.assertEqual(output, "full full full full half")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = StarRating.StarRating("a")
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()