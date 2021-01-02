'''
Unittests for TransitivityRelations.py
December 2020 Jakub Kazimierski
'''

import unittest
import TransitivityRelations

class test_TransitivityRelations(unittest.TestCase):    
    '''
    Class with unittests for TransitivityRelations.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''   
        output = TransitivityRelations.TransitivityRelations(["(0,1,0,0)","(0,0,1,0)","(0,0,1,1)","(0,0,0,1)"])
        self.assertEqual(output, "(0,2)-(0,3)-(1,3)")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()