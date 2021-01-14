'''
Unitests for VowelCount.py
October 2020 Jakub Kazimierski
'''

import unittest
import VowelCount

class test_VowelCount(unittest.TestCase):
    '''
    Class contains unittests for VowelCount.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = VowelCount.VowelCount("Abcde")
        self.assertEqual(output, 2)

    def test_UpperAndLowerCaseVowels(self):
        '''
        Checks if uppercase vowels are counted.
        '''
        output = VowelCount.VowelCount("AabcdeEf")
        self.assertEqual(output, 4)

    def test_VowelsAndSpaces(self):
        '''
        Checks if spaces affect proper input.
        '''
        output = VowelCount.VowelCount("A a bcd e e f")
        self.assertEqual(output, 4)

    def test_VowelsAndPunctuationSigns(self):
        '''
        Checks if nonalphabetical sign affects input.
        '''
        output = VowelCount.VowelCount("A/a\"bcd>e e f")
        self.assertEqual(output, 4)

    def test_WrongInput(self):
        '''
        Checks if output is equal '-1' for wrong input.
        '''
        output = VowelCount.VowelCount(1233)
        self.assertEqual(output, -1)

    #endregion
    
if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()        