'''
Unittests for ArrayMatching.py
November 2020 Jakub Kazimierski
'''

import unittest
import ArrayMatching

class test_ArrayMatching(unittest.TestCase):
    '''
    Class contains unittests for ArrayMatching.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = ArrayMatching.ArrayMatching(["[1, 2, 5, 6]", "[5, 2, 8, 11]"])
        self.assertEquals(output, "6-4-13-17")
        

    def test_DifferentLenght(self):
        '''
        Cheks if output is as expected for different lenght of lists.
        '''
        output = ArrayMatching.ArrayMatching(["[1, 2, 5, 6]", "[5, 2, 8]"])
        self.assertEquals(output, "6-4-13-6")
        

    def test_WrongInput(self):
        '''
        Checks if for wrong input output is equal -1.
        '''
        output = ArrayMatching.ArrayMatching([[1, 2, 5, 6], "[5, 2, 8, 11]"])
        self.assertEquals(output, -1)
        

    # endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()