'''
Unittests for ConnectFourWinner.py
January 2021 Jakub Kazimierski
'''

import unittest
import ConnectFourWinner

class test_ConnectFourWinner(unittest.TestCase):    
    '''
    Class with unittests for ConnectFourWinner.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["R","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,R,Y,x,Y)","(x,x,x,R,R,Y,R)","(x,x,x,Y,R,R,Y)"]
        output = ConnectFourWinner.ConnectFourWinner(input_val)
        self.assertEqual(output, "(3x3)")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()