'''
Unittests for FindIntersection.py
October 2020 Jakub Kazimierski
'''

import unittest
import FindIntersection

class test_FindIntersection(unittest.TestCase):
    '''
    Class contains unittests for FindIntersection.py
    '''

    #region Unittests
    def test_SimpleIntersection(self):
        '''
        Tests if output has expected list of numbers from both strings.
        '''
        output = FindIntersection.FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"])
        self.assertEqual(output, "1,4,13")

    def test_NoIntersection(self):
        '''
        Checks if output is false if no intersection was found.
        '''
        output = FindIntersection.FindIntersection(["2, 3, 4","5, 6, 7"])
        self.assertEqual(output, False)

    def test_RepeatedValues(self):
        '''
        Checks if output is correct if values repeat in each array
        (output should have one number from both arrays if both contains this number, no matter how many times 
        it appears in both arrays).
        '''
        output = FindIntersection.FindIntersection(["2, 3, 3","3, 3, 4, 4"])
        self.assertEqual(output, "3")

    def test_UnsortedArrays(self):
        '''
        Checks if output is correct if arrays are not sorted.
        '''
        output = FindIntersection.FindIntersection(["4, 3, 2, 5","5, 6, 4"])
        self.assertEqual(output, "4,5")
    
    def test_UnsortedOutput(self):
        '''
        Checks if output is sorted ascending.
        '''
        output = FindIntersection.FindIntersection(["2, 3, 4","5, 6, 7"])
        self.assertFalse(output, "5,4")

    def test_AssertInput(self):
        '''
        Checks if output is -1 for wrong input.
        '''
        output = FindIntersection.FindIntersection(["2, 3, 4",5, 6, 7])
        self.assertTrue(output, -1)    
    #endregion
    
if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()