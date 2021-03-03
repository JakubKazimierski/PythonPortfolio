'''
Knapsack Problem from AlgoExpert.io
March 2021 Jakub Kazimierski
'''

def knapsackProblem(items, capacity):
    '''
    You're given an array of arrays where each 
    subarray holds two integer values and represents 
    an item; the first integer is the item's value, 
    and the second integer is the item's weight. 
    You're also given an integer representing the
    maximum capacity of a knapsack that you have.

    Your goal is to fit items in your knapsack without 
    having the sum of their weights exceed the knapsack's 
    capacity, all the while maximizing their combined value. 
    Note that you only have one of each item at your disposal.
    
    Write a function that returns the maximized combined value 
    of the items that you should pick as well as an array of 
    the indices of each item picked.
    
    If there are multiple combinations of items that maximize 
    the total value in the knapsack, your function can return 
    any of them.
    '''