'''
Unittests for OverlappingRanges.py
November 2020 Jakub Kazimiersi
'''

import unittest
import OverlappingRanges


class test_OverlappingRanges(unittest.TestCase):
    '''
    Class contains unittests for OverlappingRanges.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = OverlappingRanges.OverlappingRanges([5,11,1,5,1])
        self.assertEqual(output, "true")

    def test_FalseOutput(self):
        '''
        Cheks if output is as false if intersection fo sets is lower than defined one.
        '''
        output = OverlappingRanges.OverlappingRanges([5,11,1,5,2])
        self.assertEqual(output, "false")

    def test_WrongInput(self):
        '''
        Cheks if output is equal -1 if input array is not proper.
        '''
        output = OverlappingRanges.OverlappingRanges([5,11,1,5])
        self.assertEqual(output, -1)

    # endregion


if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()