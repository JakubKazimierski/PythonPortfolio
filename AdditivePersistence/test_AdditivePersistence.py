'''
Unittests for AdditivePersistence.py
November 2020 Jakub Kazimierski
'''
import unittest
import AdditivePersistence

class test_AdditivePersistence(unittest.TestCase):
    '''
    class contains unittests for AdditivePersistence
    '''

    #region Unittests

    def test_ExpectedOutput(self):
        '''
        check if returned amount of steps
        is as it should be
        '''
        output = AdditivePersistence.AdditivePersistence(2718)
        self.assertEqual(output, 2)

    def test_SingleDigitInput(self):
        '''
        check id output is correct
        for single digit input
        '''
        output = AdditivePersistence.AdditivePersistence(1)
        self.assertEqual(output, 0)


    def test_InputType(self):
        '''
        check if assertion for input
        type works properly
        '''
        output = AdditivePersistence.AdditivePersistence(-1.0)
        self.assertEqual(output, -1)    

    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()