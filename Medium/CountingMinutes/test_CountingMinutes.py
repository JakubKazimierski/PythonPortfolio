'''
Unittests for CountingMinutes.py
December 2020 Jakub Kazimierski
'''

import unittest
import CountingMinutes

class test_CountingMinutes(unittest.TestCase):    
    '''
    Class with unittests for CountingMinutes.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = CountingMinutes.CountingMinutes("1:00pm-11:00am")
        self.assertEqual(output, 1320)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()