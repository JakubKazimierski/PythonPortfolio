'''
Unittests for ClassPhotos.py
February 2021 Jakub Kazimierski
'''

import unittest
from ClassPhotos import classPhotos

class test_ClassPhotos(unittest.TestCase):    
    '''
    Class with unittests for ClassPhotos.py
    '''

    def setUp(self):
        '''
        Sets up input and output.
        '''
        self.redShirtHeights = [5, 8, 1, 3, 4]
        self.blueShirtHeights = [6, 9, 2, 4, 5]
        self.output = True

        return self.redShirtHeights, self.blueShirtHeights, self.output
    
    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        redShirts, blueShirts, output = self.setUp()
        method_output = classPhotos(redShirts, blueShirts)
        self.assertEqual(output, method_output)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()