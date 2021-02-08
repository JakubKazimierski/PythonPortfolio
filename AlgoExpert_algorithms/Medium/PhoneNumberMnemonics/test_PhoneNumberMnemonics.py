'''
Unittests for PhoneNumberMnemonics.py
February 2021 Jakub Kazimierski
'''

import unittest
from PhoneNumberMnemonics import phoneNumberMnemonics

class test_PhoneNumberMnemonics(unittest.TestCase):    
    '''
    Class with unittests for PhoneNumberMnemonics.py
    '''

    def SetUp(self):
        '''
        Set Up input and output lists.
        '''
        
        self.input = "1905"

        self.output = [
                        "1w0j",
                        "1w0k",
                        "1w0l",
                        "1x0j",
                        "1x0k",
                        "1x0l",
                        "1y0j",
                        "1y0k",
                        "1y0l",
                        "1z0j",
                        "1z0k",
                        "1z0l",
                        ]


        return self.input, self.output

    # region Unittests

    def test_Iterative_method(self):   
        '''
        Checks if output is correct.
        '''
        input_number, correct_output = self.SetUp()
        
        output = phoneNumberMnemonics(input_number)
        self.assertEqual(output, correct_output)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()