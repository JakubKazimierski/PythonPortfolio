'''
Unittests for H_Distance.py
December 2020 Jakub Kazimierski
'''

import unittest
import H_Distance

class test_H_Distance(unittest.TestCase):    
    '''
    Class with unittests for H_Distance.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = H_Distance.HDistance(["house", "hours"])
        self.assertEqual(output, 2)

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = H_Distance.HDistance(12)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()