'''
Unittests for CharacterRemoval.py
December 2020 Jakub Kazimierski
'''

import unittest
import CharacterRemoval

class test_CharacterRemoval(unittest.TestCase):    
    '''
    Class with unittests for CharacterRemoval.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["worlcde", "apple,bat,cat,goodbye,hello,yellow,why,world"]
        output = CharacterRemoval.CharacterRemoval(input_val)
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()