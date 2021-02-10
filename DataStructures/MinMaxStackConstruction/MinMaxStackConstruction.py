'''
Min Max Stack Construction from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

class MinMaxStack:
    '''
    Write a MinMaxStack class for
    a MinMaxStack. The class should 
    support:

        -Pushing and popping values on and off
            the stack.
        -Peeking at the value at the top of
            the stack.
        -Getting both the minimum and the maximum
            values in the stacj at any given point
            in time.

    All class methods, when considered independently,
    should run in constant time and with constant space.                
    '''

    def __init__(self):
        self.stack = []
        self.minMax = []

    def peek(self):
        '''
        Time O(1) | space O(1)
        Returns last elem at stack.
        '''
        return self.stack[-1]

    def pop(self):
        '''
        Time O(1) | space O(1)
        Removes and returns last elem from stack.
        And from dict of min max values.
        '''        
        self.minMax.pop()
        return self.stack.pop()
	
    def push(self, number):
        '''
        Time O(1) | space O(1)
        Appends new elem to stack.
        And updates dict of min max values.
        '''        

        self.stack.append(number)

        if len(self.minMax) > 0:

            curr_min, curr_max = self.minMax[-1][0], self.minMax[-1][1]

            if number < curr_min:
                curr_min = number
            if number > curr_max:
                curr_max = number

            self.minMax.append([curr_min, curr_max])    
        else:
            self.minMax.append([number, number])    


    def getMin(self):
        '''
        Time O(1) | space O(1)
        Returns min elem from stack.
        Based on dict of min max values.
        '''        
        return self.minMax[-1][0]

    def getMax(self):
        '''
        Time O(1) | space O(1)
        Returns max elem from stack.
        Based on dict of min max values.
        '''                
        return self.minMax[-1][1]
