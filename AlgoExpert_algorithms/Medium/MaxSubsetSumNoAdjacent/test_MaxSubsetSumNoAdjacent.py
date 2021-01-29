'''
Unittests for MaxSubsetSumNoAdjacent.py
January 2021 Jakub Kazimierski
'''


import unittest
from MaxSubsetSumNoAdjacent import maxSubsetSumNoAdjacent

class test_MaxSubsetSumNoAdjacent(unittest.TestCase):    
    '''
    Class with unittests for MaxSubsetSumNoAdjacent.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr = [75, 105, 120, 75, 90, 135]
        output = maxSubsetSumNoAdjacent(input_arr)
        self.assertEqual(output, 330)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()