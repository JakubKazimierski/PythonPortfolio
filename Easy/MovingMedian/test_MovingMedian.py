'''
Unittests for MovingMedian.py
December 2020 Jakub Kazimierski
'''

import unittest
import MovingMedian

class test_MovingMedian(unittest.TestCase):    
    '''
    Class with unittests for MovingMedian.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MovingMedian.MovingMedian([3, 1, 3, 5, 10, 6, 4, 3, 1] )
        self.assertEqual(output, "1,2,3,5,6,6,4,3")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = MovingMedian.MovingMedian(["s", 1, 3, 5, 10, 6, 4, 3, 1])
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()