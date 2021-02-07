'''
Unittests for Permutations.py
February 2021 Jakub Kazimierski
'''

import unittest
from Permutations import getPermutations

class test_Permutations(unittest.TestCase):    
    '''
    Class with unittests for Permutations.py
    '''

    def SetUp(self):
        '''
        Set Up input list.
        '''
        
        self.input = [1, 2, 3]
        # due to list in list is not hashable type, use tuple for permutation 
        self.output = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

        return self.input, self.output

    # region Unittests
    def test_RemoveKthNodeFromEnd(self):   
        '''
        Checks if output is correct.
        '''
        input_list, correct_output = self.SetUp()
        
        
        output = getPermutations(input_list)
        self.assertEqual(set(output), set(correct_output))


    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()