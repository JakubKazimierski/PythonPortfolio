'''
Unittests for FarthestNode.py
January 2021 Jakub Kazimierski
'''

import unittest
import FarthestNode

class test_FarthestNode(unittest.TestCase):    
    '''
    Class with unittests for FarthestNode.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = FarthestNode.FarthestNode(["b-a","a-c","c-d","e-d","e-f","f-g","g-h","i-h","i-j"])
        self.assertEqual(output, 4)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()