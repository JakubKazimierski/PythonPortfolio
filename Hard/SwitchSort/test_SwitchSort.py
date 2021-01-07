'''
Unittests for SwitchSort.py
January 2021 Jakub Kazimierski
'''

import unittest
import SwitchSort

class test_SwitchSort(unittest.TestCase):    
    '''
    Class with unittests for SwitchSort.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SwitchSort.SwitchSort([3,4,2,1])
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()