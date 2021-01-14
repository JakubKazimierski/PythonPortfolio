'''
Unittestst for SeatingStudents.py
December 2020 Jakub Kazimierski
'''

import unittest
import SeatingStudents

class test_SeatingStudents(unittest.TestCase):    
    '''
    Class with unittests for SeatingStudents.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SeatingStudents.SeatingStudents([12, 2, 6, 7, 11])
        self.assertEqual(output, 6)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()