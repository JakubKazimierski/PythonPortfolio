'''
Staircase Traversal from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def staircaseTraversal(height, maxSteps):
    '''    
    You're given two positive integers representing 
    the height of a staircase and the maximum number 
    of steps that you can advance up the staircase at a time.
    Write a function that returns the number of ways in which 
    you can climb the staircase.

    For example, if you were given a staircase of height = 3 and
    maxSteps = 2 you could climb the staircase in 3 ways. You could
    take 1 step, 1 step, then 1 step, you could also take 1 step, then
    2 steps, and you could take 2 steps, then 1 step.

    Note that maxSteps <= height will always be true.
    '''

    # O(n) space where n is num of steps
    steps_combinations = [0]*(height+1)
    # no steps has only 1 possible solution
    steps_combinations[0] = 1


    # O(n*maxStep) time which is still O(n) time  in avg case (worst is n^2)
    for idx in range(1, len(steps_combinations)):
        for step_len in range(1, maxSteps+1):
            if idx < step_len:
                break
            else:
                steps_combinations[idx] += steps_combinations[idx-step_len]


    return steps_combinations[-1]

    # total space and time of above is:
    # O(n) Time | O(n) space