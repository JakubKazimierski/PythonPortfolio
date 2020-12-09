'''
Unittests for GCF.py
December 2020 Jakub Kazimierski
'''


import unittest
import GCF

class test_GCF(unittest.TestCase):    
    '''
    Class with unittests for GCF.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = GCF.GCF([45, 12])
        self.assertEqual(output, 3)

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = GCF.GCF(12)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()