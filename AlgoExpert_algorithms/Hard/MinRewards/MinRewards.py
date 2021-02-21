'''
Min Rewards from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def minRewards(scores):
    '''
    Imagine that you're a teacher who's just
    graded the final exam in a class. You have
    a list of student scores on the final exam
    in a particular order (not necessarily sorted),
    and you want to reward your students. You decide
    to do so fairly by giving them arbitrary rewards
    following two rules:

    - 1) All students must receive at least one reward.
    - 2) Any given student must receive strictly fewer
        rewards than an adjacent student with a higher score.

    Write a function that takes in a list of scores and
    returns the minimum number of rewards that you must give out
    to students to satisfy the two rules.

    You can assume that all students have different scores;
    In other words, the scores are all unique.
    '''

    # O(n) space
    rewards = [1]*len(scores)

    # O(n) time 
    for idx in range(1, len(scores)):
        if scores[idx] > scores[idx-1]:
            rewards[idx] = rewards[idx-1] + 1
    # O(n) time 
    for idx in reversed(range(len(scores)-1)):
        if scores[idx] > scores[idx+1]:
            rewards[idx] = max(rewards[idx], rewards[idx+1] + 1)  
    # O(n) time 
    return sum(rewards)               