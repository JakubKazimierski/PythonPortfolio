'''
Unittests for SameBSTs.py
February 2021 Jakub Kazimierski
'''


import unittest
from SameBSTs import sameBSTs

class test_SameBSTs(unittest.TestCase):    
    '''
    Class with unittests for SameBSTs.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        self.arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
        self.output = True

        return self.arrayOne, self.arrayTwo, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        Input cannot be empty string.
        '''
        arrayOne, arrayTwo, output = self.setUp()
        output_method = sameBSTs(arrayOne, arrayTwo)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()