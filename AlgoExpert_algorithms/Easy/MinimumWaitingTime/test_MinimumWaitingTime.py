'''
Unittests for MinimumWaitingTime.py
January 2021 Jakub Kazimierski
'''

import unittest
import MinimumWaitingTime

class test_MinimumWaitingTime(unittest.TestCase):    
    '''
    Class with unittests for MinimumWaitingTime.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        queries = [3, 2, 1, 2, 6]
        output = MinimumWaitingTime.minimumWaitingTime(queries)
        self.assertEqual(output, 17)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()