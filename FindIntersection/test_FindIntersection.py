'''
Unittests for find intersection method
October 2020 Jakub Kazimierski
'''

import unittest
import FindIntersection

class test_FindIntersection(unittest.TestCase):
    '''
    class with unittests for find intersection method
    '''

    #region Unittests
    def test_SimpleIntersection(self):
        '''
        test if output is exxpected list of numbers from both strings
        '''
        output = FindIntersection.FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"])
        self.assertEqual(output, "1,4,13")

    def test_NoIntersection(self):
        '''
        check if output is false when no intersection is found
        '''
        output = FindIntersection.FindIntersection(["2, 3, 4","5, 6, 7"])
        self.assertEqual(output, False)

    def test_RepeatedValues(self):
        '''
        check if output is correct when values repeat few times in oth array
        (output should be one number from both arrays if both contain it, no matter how many times 
        it appears in both arrays)
        '''

        output = FindIntersection.FindIntersection(["2, 3, 3","3, 3, 4, 4"])
        self.assertEqual(output, "3")

    def test_UnsortedArrays(self):
        '''
        check if output is correct when arrays are not sorted
        '''
        output = FindIntersection.FindIntersection(["4, 3, 2, 5","5, 6, 4"])
        self.assertEqual(output, "4,5")
    
    def test_UnsortedOutput(self):
        '''
        check if output is sorted ascending
        '''
        output = FindIntersection.FindIntersection(["2, 3, 4","5, 6, 7"])
        self.assertFalse(output, "5,4")
    #endregion
    
if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()