'''
Unittests for TimeDifference.py
December 2020 Jakub Kazimierski
'''

import unittest
import TimeDifference

class test_TimeDifference(unittest.TestCase):
    '''
    Class contains unittests for
    TimeDifference.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = TimeDifference.TimeDifference(["2:10pm", "1:30pm", "10:30am", "4:42pm"] )
        self.assertEqual(output, 40)

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = TimeDifference.TimeDifference(12)
        self.assertEqual(output, -1)


    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()