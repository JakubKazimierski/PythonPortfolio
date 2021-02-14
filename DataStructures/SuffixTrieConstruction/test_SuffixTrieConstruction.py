'''
Unittests for SuffixTrieConstruction.py
February 2021 Jakub Kazimierski
'''

import unittest
from SuffixTrieConstruction import SuffixTrie

class test_ReverseWordsInString(unittest.TestCase):    
    '''
    Class with unittests for ReverseWordsInString.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input = "babc"
        self.populated = {
                        'c' : {'*' : True},
                        'b' : {
                                'c' : {'*' : True},
                                'a' : { 'b' : {'c' : {'*' : True}}},
                        },
                        'a' : { 'b' : {'c' : {'*' : True}}},
                    }   

        self.tree = SuffixTrie(self.input)
        
        return self.tree.contains("abc")

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output_true  = self.setUp()
        self.assertEqual(True, output_true)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()