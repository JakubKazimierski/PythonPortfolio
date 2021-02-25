'''
Number Of Ways To Traverse Graph from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def numberOfWaysToTraverseGraph(width, height):
    '''
    O(width + height) time | O(1) space
    Permutation based approach.
    '''
    x_ways_right = width - 1
    y_ways_down = height - 1

    def factorial(num):
        '''
        O(num) time | o(1) space
        Returns factorial of numebr.
        '''

        factorial = 1

        for number in range(2, num+1):
            factorial = factorial*number

        return factorial

    # newton fomula
    factor_up = (factorial(x_ways_right+y_ways_down))
    factor_down = (factorial(x_ways_right)*factorial(y_ways_down))
    return factor_up//factor_down    