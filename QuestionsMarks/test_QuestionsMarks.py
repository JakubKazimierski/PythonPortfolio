'''
TestsUnits fro QuestionsMarks.py from codersbyte
October/November 2020 Jakub Kazimierski
'''

import unittest
import QuestionsMarks


class test_QuestionsMarks(unittest.TestCase):
    '''
    class contains unittests for QuestionsMaks.py from codersbyte
    '''

    #region Unittests
    def test_trueOutput(self):
        '''
        check ifoutput is true as expected
        '''
        output = QuestionsMarks.QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?a??5")
        self.assertEqual(output, "true")

    def test_notEnoughQuestionsMarksOutput(self):
        '''
        check if output is false when there is not enough
        questions marks
        '''
        output = QuestionsMarks.QuestionsMarks("arrb6??4xxbl5??eee5")
        self.assertEqual(output, "false")


    def test_EnoughQuestionsMarksDigitsNotAddUpToTen(self):
        '''
        check if output is false 
        when numbers not add up to 10
        '''
        output = QuestionsMarks.QuestionsMarks("arrb6???xxbl5???eee4")
        self.assertEqual(output, "false")

    def test_NoDigits(self):
        '''
        check if output is false when there is no digits
        '''
        output = QuestionsMarks.QuestionsMarks("arrb???xxbl???eee")
        self.assertEqual(output, "false")

    def test_NotValidInput(self):
        '''
        check if output is -1 when
        input is empty
        '''
        output = QuestionsMarks.QuestionsMarks("")
        self.assertEqual(output, -1)

    #endregion
    
if __name__ == "__main__":
    '''
    main method for unittests class
    '''
    unittest.main()        
