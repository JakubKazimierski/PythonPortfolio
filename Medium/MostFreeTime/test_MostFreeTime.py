'''
Unittests for MostFreeTime.py
December 2020 Jakub Kazimierski
'''

import unittest
import MostFreeTime

class test_MostFreeTime(unittest.TestCase):    
    '''
    Class with unittests for MostFreeTime.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MostFreeTime.MostFreeTime(["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"])
        self.assertEqual(output, "01:30")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()