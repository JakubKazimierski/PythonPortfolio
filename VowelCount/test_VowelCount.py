'''
Unitests for VowelCount.py from codersbyte
October 2020 Jakub Kazimierski
'''

import unittest
import VowelCount

class test_VowelCount(unittest.TestCase):
    '''
    class with unittests for VowelCount
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        check if output is as expected
        '''
        output = VowelCount.VowelCount("Abcde")
        self.assertEqual(output, 2)

    def test_UpperAndLowerCaseVowels(self):
        '''
        check if uppercase vowels
        are counted
        '''
        output = VowelCount.VowelCount("AabcdeEf")
        self.assertEqual(output, 4)

    def test_VowelsAndSpaces(self):
        '''
        check if spaces affect proper input
        '''
        output = VowelCount.VowelCount("A a bcd e e f")
        self.assertEqual(output, 4)

    def test_VowelsAndPunctuationSigns(self):
        '''
        check if nonalphabetical signs affect input
        '''
        output = VowelCount.VowelCount("A/a\"bcd>e e f")
        self.assertEqual(output, 4)

    def test_WrongInput(self):
        '''
        check if output is '-1' for wrong input
        '''
        output = VowelCount.VowelCount(1233)
        self.assertEqual(output, -1)

    #endregion
    
if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()        