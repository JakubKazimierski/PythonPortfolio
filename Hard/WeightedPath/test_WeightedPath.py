'''
Unittestst for WeightedPath.py
January 2021 Jakub Kazimierski
'''

import unittest
import WeightedPath

class test_WeightedPath(unittest.TestCase):    
    '''
    Class with unittests for WeightedPath.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["6","D","B","C","A","E","F","B|A|2","A|F|3","A|C|4","B|D|1","D|E|12","C|D|4","F|E|1"]
        output = WeightedPath.WeightedPath(input_val)
        self.assertEqual(output, "D-B-A-F")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()