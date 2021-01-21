'''
Minimum Waiting Time from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

from itertools import permutations

def minimumWaitingTime(queries):
    # Write your code here.
    '''
    You're given a non-empty array of positive integers
    representing the amounts of time that specific queries
    take to execute. Only one query can be executed at 
    a time, but the queries can be executed in any order.

    A query's waiting time is defined as the amount of time 
    that it must wait before its execution starts. In other words,
    if a query is executed second, then its waiting time is the duration
    of the first query; If a query is executed third, then its
    waiting time is the sum of the durations of the first two queries.

    Write a function that returns the minimum amount of total waiting time for all
    of the queries. For example, if you're given the queries of
    durations [1, 4, 5], then the total waiting time if the queries were 
    executed in order [5, 1, 4] would be (0) + (5) + (5+1) = 11.
    The first query of duration 5 would be executed immidiately, so its
    waiting time would be 0, the second query of duration 1 would have to wait
    5 seconds (the duration of the first query) to be executed, and the last
    query would have to wait the duration of the first two queries before being
    executed.

    Note: you're allowed to mutate the input array.
    '''
    # time O(nlogn) | space O(1)
    sorted_query = sorted(queries)

    def count_times(list):
        time = []
        curr_time = 0
        for elem_id in range(1, len(list)):
            curr_time += list[elem_id-1]            
            time.append(curr_time)
        return sum(time)

    return count_times(sorted_query)
