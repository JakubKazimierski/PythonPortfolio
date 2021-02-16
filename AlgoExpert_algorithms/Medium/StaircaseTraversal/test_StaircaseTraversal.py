'''
Unittests for StaircaseTraversal.py
February 2021 Jakub Kazimierski
'''

import unittest
from StaircaseTraversal import staircaseTraversal

class test_StaircaseTraversal(unittest.TestCase):    
    '''
    Class with unittests for StaircaseTraversal.py
    '''

    def setUp(self):
        self.height = 4
        self.maxSteps = 2
        self.output = 5

        return self.height, self.maxSteps, self.output
    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        height, maxSteps, output = self.setUp()
        method_output = staircaseTraversal(height, maxSteps)
        self.assertEqual(output, method_output)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()