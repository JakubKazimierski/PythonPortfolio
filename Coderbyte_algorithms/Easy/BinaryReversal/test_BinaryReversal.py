'''
Unittests for BinaryReversal.py
November 2020 Jakub Kazimierski
'''

import unittest
import BinaryReversal

class test_BinaryReversal(unittest.TestCase):
    '''
    Class contains unittests for BinaryReversal.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = BinaryReversal.BinaryReversal("47")
        self.assertEquals(output, 244)
                

    def test_WrongInput(self):
        '''
        Checks if for wrong input output is equal -1.
        '''
        output = BinaryReversal.BinaryReversal(5)
        self.assertEquals(output, -1)
        

    # endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()