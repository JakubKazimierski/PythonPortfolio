'''
Unittests for EquivalentKeypresses.py
December 2020 Jakub Kazimierski
'''

import unittest
import EquivalentKeypresses

class test_EquivalentKeypresses(unittest.TestCase):    
    '''
    Class with unittests for EquivalentKeypresses.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = EquivalentKeypresses.EquivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,d"])
        self.assertEqual(output, "true")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = EquivalentKeypresses.EquivalentKeypresses(12)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()