'''
Unittests for Superincreasing.py
November 2020 Jakub Kazimierski
'''

import unittest
import Superincreasing

class test_Superincreasing(unittest.TestCase):
    '''
    Class contains unittests for Superincreasing.py
    '''

    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = Superincreasing.Superincreasing([1, 3, 6, 13, 54])
        self.assertEquals(output, "true")
        

    def test_FalseOutput(self):
        '''
        Cheks if output is equal "false" for not superincreasing sequence.
        '''
        output = Superincreasing.Superincreasing([1, 3, 6, 9, 54])
        self.assertEquals(output, "false")
        
    def test_WrongInput(self):
        '''
        Cheks if output is equal -1 for wrong type of input.
        '''
        output = Superincreasing.Superincreasing([1, "3", 6, 9, 54])
        self.assertEquals(output, -1)


if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()