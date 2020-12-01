'''
Unittests for NonrepeatingCharacter.py
December 2020 Jakub Kazimierski
'''

import unittest
import NonrepeatingCharacter

class test_NonrepeatingCharacter(unittest.TestCase):
    '''
    Class contains unittests for NonrepeatingCharacter.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = NonrepeatingCharacter.NonrepeatingCharacter("agettkgaeee")
        self.assertEqual(output, "k")

    def test_WrongInput(self):
        '''
        Checks if output is as expected.
        '''
        output = NonrepeatingCharacter.NonrepeatingCharacter(123)
        self.assertEqual(output, -1)

    #endregion


if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()