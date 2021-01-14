'''
Unittests for QuestionsMarks.py
October/November 2020 Jakub Kazimierski
'''

import unittest
import QuestionsMarks


class test_QuestionsMarks(unittest.TestCase):
    '''
    Class contains unittests for QuestionsMaks.py
    '''

    #region Unittests
    def test_trueOutput(self):
        '''
        Checks if output is true for proper input. 
        '''
        output = QuestionsMarks.QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?a??5")
        self.assertEqual(output, "true")

    def test_notEnoughQuestionsMarksOutput(self):
        '''
        Checks if output is false when there is not enough
        questions marks.
        '''
        output = QuestionsMarks.QuestionsMarks("arrb6??4xxbl5??eee5")
        self.assertEqual(output, "false")


    def test_DigitsNotAddUpToTen(self):
        '''
        Checks if output is false 
        when numbers not add up to 10.
        '''
        output = QuestionsMarks.QuestionsMarks("arrb6???xxbl5???eee4")
        self.assertEqual(output, "false")

    def test_NoDigits(self):
        '''
        Checks if output is false when there is no digits.
        '''
        output = QuestionsMarks.QuestionsMarks("arrb???xxbl???eee")
        self.assertEqual(output, "false")

    def test_EmptyInput(self):
        '''
        Checks if output is false when input is empty.
        '''
        output = QuestionsMarks.QuestionsMarks("")
        self.assertEqual(output, "false")

    def test_NotValidInput(self):
        '''
        Checks if output is -1 for wrong type input.
        '''
        output = QuestionsMarks.QuestionsMarks(123)
        self.assertEqual(output, -1)
    #endregion
    
if __name__ == "__main__":
    '''
    Main method for unittests class
    '''
    unittest.main()        
