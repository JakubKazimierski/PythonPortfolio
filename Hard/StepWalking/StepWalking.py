'''
Step Walking from Coderbyte
January 2021 Jakub Kazimierski
'''

from itertools import permutations

def StepWalking(num):
    '''
    Have the function StepWalking(num) 
    take the num parameter being passed 
    which will be an integer between 1 and 15 
    that represents the number of stairs you will 
    have to climb. You can climb the set of stairs 
    by taking either 1 step or 2 steps, and you can 
    combine these in any order. 
    
    So for example, to climb 3 steps you can either do: 
    (1 step, 1 step, 1 step) or (2, 1) or (1, 2). So for 3 
    steps we have 3 different ways to climb them, so your 
    program should return 3. Your program should return the 
    number of combinations of climbing num steps.
    '''
    
    # can be solved by approach to fibbonnaci sequence
    # as amount of steps at next level of stairs symbolize next
    # elem of fibbonnaci sequence


    if num == 0 or num == 1:
        return 1

    return StepWalking(num-1)+StepWalking(num-2)    


