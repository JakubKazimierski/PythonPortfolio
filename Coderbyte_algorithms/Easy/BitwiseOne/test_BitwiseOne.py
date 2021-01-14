'''
Unittests for BitwiseOne.py
November 2020 Jakub Kazimierski
'''

import unittest
import BitwiseOne

class test_BitwiseOne(unittest.TestCase):
    '''
    Class contains unittests for BitwiseOne.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = BitwiseOne.BitwiseOne(["1001", "0100"])
        self.assertEquals(output, "1101")

    def test_WrongInput(self):
        '''
        Checks if for wrong input output is equal -1.
        '''
        output = BitwiseOne.BitwiseOne([1001, "0100"])
        self.assertEquals(output, -1)


    # endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()