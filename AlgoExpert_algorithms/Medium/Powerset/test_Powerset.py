'''
Unittests for Powerset.py
February 2021 Jakub Kazimierski
'''

import unittest
from Powerset import powerset, powerset_recurency

class test_Powerset(unittest.TestCase):    
    '''
    Class with unittests for Powerset.py
    '''

    def SetUp(self):
        '''
        Set Up input list.
        '''
        
        self.input = [1, 2, 3]
        # due to list in list is not hashable type, use tuple for permutation 
        self.output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

        return self.input, self.output

    # region Unittests
    def test_Iterative_method(self):   
        '''
        Checks if output is correct.
        '''
        input_list, correct_output = self.SetUp()
        
        
        output = powerset(input_list)
        self.assertEqual(output, correct_output)

    def test_Recurency_method(self):   
        '''
        Checks if output is correct.
        '''
        input_list, correct_output = self.SetUp()
        
        
        output = powerset_recurency(input_list)
        self.assertEqual(output, correct_output)


    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()