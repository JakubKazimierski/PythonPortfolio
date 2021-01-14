'''
Unittests for WaveSorting.py
November 2020 Jakub Kazimierski
'''

import unittest
import WaveSorting

class test_WaveSorting(unittest.TestCase):
    '''
    Class contains unittests for WaveSorting.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = WaveSorting.WaveSorting([0, 4, 22, 4, 14, 4, 2])
        self.assertEqual(output, "true")

    def test_WrongInput(self):
        '''
        Cheks if output is equal -1 for worng input type.
        '''
        output = WaveSorting.WaveSorting([0, "4", 22, 4, 14, 4, 2])
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()
