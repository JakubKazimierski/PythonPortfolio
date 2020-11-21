'''
Unittests for AdditivePersistence.py
November 2020 Jakub Kazimierski
'''
import unittest
import AdditivePersistenceRecursion

class test_AdditivePersistence(unittest.TestCase):
    '''
    Class contains unittests for AdditivePersistence.
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned amount of steps
        is equal to real (e.g. for input 2718 output should be equall 2)
        '''
        output = AdditivePersistenceRecursion.AdditivePersistence(2718)
        self.assertEqual(output, 2)

    def test_SingleDigitInput(self):
        '''
        Checks if output is equal 0
        for single digit input.
        '''
        output = AdditivePersistenceRecursion.AdditivePersistence(1)
        self.assertEqual(output, 0)

    def test_InputType(self):
        '''
        Check if output is equal to -1
        for wrong input type.
        '''
        output = AdditivePersistenceRecursion.AdditivePersistence(1.0)
        self.assertEqual(output, -1)    

    def test_InputSign(self):
        '''
        Check if output is equal to -1
        for negative integer at input.
        '''
        output = AdditivePersistenceRecursion.AdditivePersistence(-1)
        self.assertEqual(output, -1)    

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()