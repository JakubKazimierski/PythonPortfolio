'''
Unittests for CountingMinutesI.py
November 2020 Jakub Kazimierski
'''

import unittest
import CountingMinutesI

class test_CountingMinutesI(unittest.TestCase):
    '''
    class contains unittests for CountingMinutesI.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        check if simple input gives expected output
        '''
        output = CountingMinutesI.CountingMinutesI("10:00am-1:00pm")
        self.assertEqual(output, 180)
    
    def test_FirstRangeIsLaterDiffrentFormats(self):
        '''
        check if algorithm is correct
        if start hour is greater than endHour
        and formats of hours are different e.g pm-am
        '''
        output = CountingMinutesI.CountingMinutesI("10:00pm-1:00am")
        self.assertEqual(output, 180)
    
    def test_FirstRangeIsLaterSecondIsSameFormat(self):
        '''
        change if alghoritm works properly
        if first hour is grater than end hour
        and both are same format e.g pm
        '''
        output = CountingMinutesI.CountingMinutesI("10:00pm-9:00pm")
        self.assertEqual(output, 1380)

    def test_Midnight(self):
        '''
        test output for midnight hour
        start hour is later than end hour
        so output is whole day without oe minute
        '''
    
        output = CountingMinutesI.CountingMinutesI("12:01pm-12:00pm")
        self.assertEqual(output, 1439)    
    
    def test_TooLongInput(self):
        '''
        check if assertion catch too long input
        '''
        output = CountingMinutesI.CountingMinutesI("10:00pm---9:00pm")
        self.assertEqual(output, "Wrong Input")
    
    def test_InputWithoutSign(self):
        '''
        check if assertion catch input without '-' sign
        '''
        output = CountingMinutesI.CountingMinutesI("10:00pm9:00pm")
        self.assertEqual(output, "Wrong Input")

    def test_TooShortInput(self):
        '''
        check if assertion catch too short input
        '''
        output = CountingMinutesI.CountingMinutesI("10pm-9:00pm")
        self.assertEqual(output, "Wrong Input")



    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()