'''
Unittests for GasStation.py
January 2021 Jakub Kazimierski
'''

import unittest
import GasStation

class test_GasStation(unittest.TestCase):    
    '''
    Class with unittests for GasStation.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = GasStation.GasStation(["4","0:1","2:2","1:2","3:1"])
        self.assertEqual(output, 4)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()