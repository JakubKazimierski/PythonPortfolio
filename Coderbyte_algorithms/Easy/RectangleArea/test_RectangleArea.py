'''
Unittests for RectangleArea.py
November 2020 Jakub Kazimierski
'''

import unittest
import RectangleArea

class test_RectangleArea(unittest.TestCase):
    '''
    Class contains unittests for RectangleArea.py
    '''
    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = RectangleArea.RectangleArea(["(0 0)", "(3 0)", "(0 2)", "(3 2)"])
        self.assertEquals(output, 6)
        
    def test_ZeroOutput(self):
        '''
        Cheks if output is equal 0 if one of parameters is equal 0.
        '''
        output = RectangleArea.RectangleArea(["(0 0)", "(0 0)", "(0 2)", "(0 2)"])
        self.assertEquals(output, 0)    
    def test_WrongInput(self):
        '''
        Cheks if for wrong input, output equals -1.
        '''
        output = RectangleArea.RectangleArea([(0, 0), "(3 0)", "(0 2)", "(3 2)"])
        self.assertEquals(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()