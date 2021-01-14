'''
Unittests for ElementMerger.py
December 2020 Jakub Kazimierski
'''

import unittest
import ElementMerger

class test_ElementMerger(unittest.TestCase):    
    '''
    Class with unittests for ElementMerger.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ElementMerger.ElementMerger([4, 5, 1, 2, 7])
        self.assertEqual(output, 1)

    def test_OneElement(self):
        '''
        Checks if returned output is as expected for one digit in input arr.
        '''
        output = ElementMerger.ElementMerger([1])
        self.assertEqual(output, 1)


    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = ElementMerger.ElementMerger(12)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()