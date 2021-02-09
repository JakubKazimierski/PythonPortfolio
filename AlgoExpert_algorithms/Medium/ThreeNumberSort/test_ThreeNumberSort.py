'''
Unittests for ThreeNumberSort.py
February 2021 Jakub Kazimierski
'''

import unittest
from ThreeNumberSort import threeNumberSort

class test_ThreeNumberSort(unittest.TestCase):    
    '''
    Class with unittests for ThreeNumberSort.py
    '''

    def SetUp(self):
        '''
        Set Up input matrix.
        '''
        
        self.array = [1, 0, 0, -1, -1, 0, 1, 1]
        self.order = [0, 1, -1]
        self.output = [0, 0, 0, 1, 1, 1, -1, -1]

        return self.array, self.order, self.output

    # region Unittests
    def test_Iterative_method(self):   
        '''
        Checks if output is correct.
        '''
        
        array, order, proper_out = self.SetUp()
        
        output = threeNumberSort(array, order)
        self.assertEqual(output, proper_out)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()