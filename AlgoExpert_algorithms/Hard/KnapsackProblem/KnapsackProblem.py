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

    # Time O(items*capacity) | Space O(items*capacity)

    # 2d array of capacity and items
    knapsackValues = [[0 for _ in range(0, capacity + 1)] for _ in range(0, len(items) + 1)]

    for idx in range(1, len(items) + 1):
        currWeight = items[idx - 1][1]
        currValue = items[idx - 1][0]

        for cap in range(0, capacity + 1):
            # previous max value
            if currWeight > cap:
                knapsackValues[idx][cap] = knapsackValues[idx - 1][cap]
            # new max value
            else:
                knapsackValues[idx][cap] = max(knapsackValues[idx-1][cap], knapsackValues[idx-1][cap-currWeight] + currValue)
        
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]

def getKnapsackItems(knapsackValues, items):
    '''
    Returns indexes of packed to knapsack items            
    Time O(items*capacity) | Space O(1)
    '''

    sequence_items = []
    idx = len(knapsackValues) - 1
    cap = len(knapsackValues[0]) - 1

    while idx > 0:
        if knapsackValues[idx][cap] == knapsackValues[idx-1][cap]:
            idx -= 1
        else:
            # due to extra index in 2d array decrement
            sequence_items.append(idx-1)
            cap -= items[idx-1][1]
            idx -= 1
        if cap == 0:
            break
    return list(reversed(sequence_items))        

