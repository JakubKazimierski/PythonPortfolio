'''
Unittests for StockPicker.py
December 2020 Jakub Kazimierski
'''

import unittest
import StockPicker

class test_StockPicker(unittest.TestCase):    
    '''
    Class with unittests for StockPicker.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StockPicker.StockPicker([44, 30, 24, 32, 35, 30, 40, 38, 15])
        self.assertEqual(output, 16)

    def test_NoGain(self):
        '''
        Checks if returned output is equal -1 if there is no profit.
        '''
        output = StockPicker.StockPicker([10, 9, 8, 2])
        self.assertEqual(output, -1)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()