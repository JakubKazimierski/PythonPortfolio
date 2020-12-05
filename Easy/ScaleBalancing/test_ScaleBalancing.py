'''
Unittests for ScaleBalancing.py
December 2020 Jakub Kazimierski
'''
import unittest
import ScaleBalancing

class test_ScaleBalancing(unittest.TestCase):
    '''
    Class contains unittests for
    ScaleBalancing.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = ScaleBalancing.ScaleBalancing(["[5, 9]", "[1, 2, 6, 7]"])
        self.assertEqual(output, "2,6")

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()