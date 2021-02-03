'''
Task Assignment from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def taskAssignment(k, tasks):
    '''
    You're given an integer k representing a number 
    of workers and an array of positive integers 
    representing a number of workers and an
    array of positive integers representing durations 
    of tasks that must be completed by the workers. 
    Specifically, each worker must complete two unique
    tasks and can only work on one task at a time. The 
    number of tasks will always be equal to 2k such that 
    each worker always has exactly two tasks to complete. 
    All tasks are independent of one another and can be completed in
    any order. Workers will complete their assigned tasks 
    in parallel, and the time taken to complete all tasks 
    will be equal to the time taken to complete the longest 
    pair of tasks (see the sample output for an explanation).
        
    Write a function that returns the optimal assignment of 
    tasks to each worker such that the tasks are completed 
    as fast as possible. Your function should return a list of 
    pairs, where each pair stores the indices of the tasks that
    should be completed by one worker. The pairs should be in the 
    following format: [task1, task2], where the order of task1 and
    task 2 doesn't matter. Your function can return the pairs in 
    any order. If multiple optimal assignments exist, any correct
    answer will be accepted.

    Note: you'll always be given at least one worker (i.e. k will 
    always be greater than 0).
    '''

    # time O(nlog(n)) n-num of tasks | space O(n)

    # below takes O(n) time | O(n) space
    list_task_idx = []
    for idx in range(len(tasks)):
        list_task_idx.append([tasks[idx], idx])


    # time O(nlog(n)) for sort by keys which are times of duration for tasks
    list_task_idx = sorted(list_task_idx, key=lambda x: x[0])
    output_arr = []

    # below is O(n) time
    while len(list_task_idx) > 0:
        output_arr.append([list_task_idx.pop(0)[1], list_task_idx.pop(-1)[1]])

    return output_arr
