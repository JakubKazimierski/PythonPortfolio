'''
Unittests for MinMaxStackConstruction.py
February 2021 Jakub Kazimierski
'''

import unittest
from MinMaxStackConstruction import MinMaxStack

class test_MinMaxStackConstruction(unittest.TestCase):    
    '''
    Class with unittests for MinMaxStackConstruction.py
    '''

    def SetUp(self):
        '''
        Set Up input stack.
        '''
        
        self.stack = MinMaxStack()
        self.stack.push(5)        
        self.stack.push(2)
        self.stack.push(7)        
        self.stack.push(8)
        self.stack.pop()        

        return self.stack

    # region Unittests
    def test_Min_method(self):   
        '''
        Checks if getMin() is correct.
        '''
        
        stack = self.SetUp()
        min_val = stack.getMin()
        self.assertEqual(min_val, 2)

    # region Unittests
    def test_Max_method(self):   
        '''
        Checks if getMax() is correct.
        '''
        
        stack = self.SetUp()
        max_val = stack.getMax()
        self.assertEqual(max_val, 7)
    # region Unittests

    def test_Peek_method(self):   
        '''
        Checks if peek() is correct.
        '''
        
        stack = self.SetUp()
        peek_val = stack.peek()
        self.assertEqual(peek_val, 7)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()