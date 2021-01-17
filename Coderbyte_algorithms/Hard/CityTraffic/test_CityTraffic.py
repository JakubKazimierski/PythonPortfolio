'''
Unittests for CityTraffic.py
January 2021 Jakub Kazimierski
'''

import unittest
import CityTraffic

class test_CityTraffic(unittest.TestCase):    
    '''
    Class with unittests for CityTraffic.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["1:[5]", "4:[5]", "3:[5]", "5:[1,4,3,2]", \
            "2:[5,15,7]", "7:[2,8]", "8:[7,38]", "15:[2]", "38:[8]"]
        output = CityTraffic.CityTraffic(input_val)
        self.assertEqual(output, "1:82,2:53,3:80,4:79,5:70,7:46,8:38,15:68,38:45")
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()