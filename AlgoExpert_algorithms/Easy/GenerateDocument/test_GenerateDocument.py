'''
Unittests for GenerateDocument.py
March 2021 Jakub Kazimierski
'''

import unittest
from GenerateDocument import generateDocument

class test_GenerateDocument(unittest.TestCase):    
    '''
    Class with unittests for GenerateDocument.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_characters = "Bste!hetsi ogEAxpelrt x "
        self.input_document = "AlgoExpert is the Best!"
        self.output = True

        return self.input_characters, self.input_document, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        characters, document, output = self.setUp()
        output_method = generateDocument(characters, document)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()