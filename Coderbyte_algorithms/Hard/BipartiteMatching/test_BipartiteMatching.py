'''
Unittests for BipartiteMatching.py
January 2021 Jakub Kazimierski
'''

import unittest
import BipartiteMatching

class test_BipartiteMatching(unittest.TestCase):    
    '''
    Class with unittests for BipartiteMatching.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["a->d", "a->e", "b->f", "c->e"]
        output = BipartiteMatching.BipartiteMatching(input_val)
        self.assertEqual(output, 3)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()