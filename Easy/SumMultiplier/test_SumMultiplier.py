'''
Unittests for SumMultiplier.py
December 2020 Jakub Kazimierski
'''

import unittest
import SumMultiplier

class test_SumMultiplier(unittest.TestCase):    
    '''
    Class with unittests for SumMultiplier.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        pass
#        output = SumMultiplier.SumMultiplier("BOB loves-coding")
#        self.assertEqual(output, "bob_loves_coding")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        pass        
#        output = SumMultiplier.SumMultiplier(6)
#        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()