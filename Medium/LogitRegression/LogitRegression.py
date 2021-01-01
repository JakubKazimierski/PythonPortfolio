'''
Logit Regression from Coderbyte
December 2020 Jakub Kazimierski
'''

import math

def LogitRegression(arr):
    '''
    Have the function LogitRegression(arr) 
    read the input array of 4 numbers x, y, a, b, 
    separated by space, and return an output of two numbers 
    for updated a and b (assume the learning rate is 1). 
    Save up to 3 digits after the decimal points for a and b. 
    The output should be a string in the format: a, b

    Logistic regression is a simple approach to do classification, 
    and the same formula is also commonly used as the output layer 
    in neural networks. We assume both the input and output variables 
    are scalars, and the logistic regression can be written as:
    
    y = 1.0 / (1.0 + exp(-ax - b))

    After observing a data example (x, y), the parameter a and b 
    can be updated using gradient descent with a learning rate.
    '''
    
    x, y, a, b = arr[0], arr[1], arr[2], arr[3]
    y_pred = 1/(1+math.exp(-a*x-b))
    
    return str(round(a-((y-y_pred)*x), 3))+", "+str(round(b-(y-y_pred),3))