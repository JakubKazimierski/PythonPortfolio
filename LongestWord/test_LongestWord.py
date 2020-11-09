'''
Unittests for LongestWord from codersbyte
October 2020 Jakub Kazimierski
'''

import unittest
import LongestWord

class test_LongestWord(unittest.TestCase):
    '''
    class with unittests for LongestWord method
    '''

    #region Unittests       
    def test_ProperOutput(self):
        '''
        check if output is as expected
        '''
        output  = LongestWord.LongestWord("Aaaaa bbbb ccc")
        self.assertEqual(output, "Aaaaa")

    def test_ProperOutput2(self):
        '''
        check if output is not equal
        to second longest word
        '''
        output  = LongestWord.LongestWord("Aaaaa bbbbb ccc")
        self.assertNotEqual(output, "bbbbb")

    def test_ProperOutput3(self):
        '''
        check if numbers are not count as word
        '''
        output  = LongestWord.LongestWord("bbbb ccc1234ddddd ")
        self.assertEqual(output, "ddddd")

    def test_NotValidInpit(self):
        '''
        check if output is empty
        for empty input
        '''
        output = LongestWord.LongestWord("")
        self.assertEqual(output, "")
    #endregion
            
if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()        