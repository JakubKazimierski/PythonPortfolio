'''
Unittests for Valid_IP_Addresses.py
February 2021 Jakub Kazimierski
'''

import unittest
from Valid_IP_Addresses import validIPAddresses

class test_Valid_IP_Addresses(unittest.TestCase):    
    '''
    Class with unittests for Valid_IP_Addresses.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input = "1921680"
        self.output = [
                        "1.9.216.80",
                        "1.92.16.80",  
                        "1.92.168.0",
                        "19.2.16.80",
                        "19.2.168.0",
                        "19.21.6.80",
                        "19.21.68.0",
                        "19.216.8.0",
                        "192.1.6.80",
                        "192.1.68.0",
                        "192.16.8.0",

                    ]

        return self.input, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_str, output_arr  = self.setUp()
        output = validIPAddresses(input_str)
        self.assertEqual(output, output_arr)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()