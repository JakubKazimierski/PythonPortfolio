'''
Unittests for CommandLine.py
December 2020 Jakub Kazimierski
'''

import unittest
import CommandLine

class test_CommandLine(unittest.TestCase):
    '''
    Class contains unittests for CommandLine.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is as expected.
        '''
        input_str = "SampleNumber=3234 provider=Dr. M. Welby patient=John Smith priority=High" 
        output = CommandLine.CommandLine(input_str)
        self.assertEqual(output, "12=4 8=12 7=10 8=4")
    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = CommandLine.CommandLine(12)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittests.
    '''
    unittest.main()
