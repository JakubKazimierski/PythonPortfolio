'''
Unittests for HammingDistance.py
November 2020 Jakub Kazimierski
'''

import unittest
import HammingDistance

class test_HammingDistance(unittest.TestCase):
    '''
    Class contains unittests for HammingDistance.py
    '''
    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = HammingDistance.HammingDistance(["coder", "codec"])
        self.assertEquals(output, 1)
    def test_ZeroOutput(self):
        '''
        Cheks if output is equal 0 if there is no difference in input strings.
        '''
        output = HammingDistance.HammingDistance(["coder", "coder"])
        self.assertEquals(output, 0)

    def test_WrongInput(self):
        '''
        Cheks if output is equal -1 if input is worng.
        '''
        output = HammingDistance.HammingDistance([1, "coder"])
        self.assertEquals(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()