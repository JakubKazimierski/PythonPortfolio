'''
Unittests for NoughtsDeterminer.py
January 2021 Jakub Kazimierski
'''

import unittest
import NoughtsDeterminer

class test_NoughtsDeterminer(unittest.TestCase):    
    '''
    Class with unittests for NoughtsDeterminer.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val =  ["X","O","-","<>","-","O","-","<>","O","X","-"]
        output = NoughtsDeterminer.NoughtsDeterminer(input_val)
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()