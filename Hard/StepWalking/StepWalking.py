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
    
    combinations_amount = 0
    max_steps_comb = []
    max_steps = num // 2
    
    # fill max_steps_comb with max possible amount of 2steps
    for _ in range(max_steps):
        max_steps_comb.append(2)
    if num % 2 != 0:
        max_steps_comb.append(1)
        upper_range = len(max_steps_comb)-2
    else:
        upper_range = len(max_steps_comb)-1

    # reverse index iteration till 0
    for index in range(upper_range, -1, -1):
        combinations_amount += len(set(permutations(max_steps_comb, len(max_steps_comb))))
        # after each counted combination, replace 2step with two of 1 step and repeat process
        max_steps_comb.append(1)
        max_steps_comb[index] = 1

    # last combination is built from all 1's and for loop does not count it
    combinations_amount += 1

    return combinations_amount


