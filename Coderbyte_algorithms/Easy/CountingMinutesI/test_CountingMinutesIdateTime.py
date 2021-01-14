'''
Unittests for CountingMinutesIdateTime.py
November 2020 Jakub Kazimierski
'''

import unittest
import CountingMinutesIdateTime

class test_CountingMinutesIbetter(unittest.TestCase):
    '''
    Class contains unittests for
    CountingMinutesIbetter.py
    '''

    #region Unittests
    def test_StartHourIsLessThanEndHour(self):
        '''
        Checks if difference is correct when start hour
        is less than end hour.
        '''
        output = CountingMinutesIdateTime.CountingMinutesI("10:00am-1:00pm")
        self.assertEqual(output, 180)
    
    def test_StartHourIsGreater(self):
        '''
        Checks if difference is correct
        if start hour is greater than endHour
        and formats of hours are different pm-am.
        '''
        output = CountingMinutesIdateTime.CountingMinutesI("10:00pm-1:00am")
        self.assertEqual(output, 180)
    
    def test_StartHourIsGreaterSameFormat(self):
        '''
        Checks if difference is correct
        if first hour is grater than end hour
        and both are same format e.g pm-pm.
        '''
        output = CountingMinutesIdateTime.CountingMinutesI("10:00pm-9:00pm")
        self.assertEqual(output, 1380)

    def test_Midnight(self):
        '''
        Checks if for midnight hour
        start hour is later than end hour
        so output is whole day without one minute.
        '''
        output = CountingMinutesIdateTime.CountingMinutesI("12:01pm-12:00pm")
        self.assertEqual(output, 1439)    
    
    def test_TooLongInput(self):
        '''
        Checks if assertion catch wrong input.
        '''
        output = CountingMinutesIdateTime.CountingMinutesI("10:00pm---9:00pm")
        self.assertEqual(output, "Wrong Input")

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()