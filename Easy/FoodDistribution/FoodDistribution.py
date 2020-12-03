'''
FoodDistribution from Coderbyte
December2020 Jakub Kazimierski
'''

def count_diff(arr):
    diff_list = []
    index_list = []
    for index in range(1, len(arr)-1):
        if arr[index] >= arr[index+1]:
            diff_list.append(arr[index]-arr[index+1])
            index_list.append(index)
        else:    
            diff_list.append(arr[index+1]-arr[index])
            index_list.append(index+1)


    max_diff = max(diff_list)
    key_max_diff = diff_list.index(max_diff)
    index_max_diff = index_list[key_max_diff]

    return (max_diff, index_max_diff, diff_list)

def FoodDistribution(arr):
    '''
    Have the function FoodDistribution(arr) 
    read the array of numbers stored in arr 
    which will represent the hunger level of 
    different people ranging from 0 to 5 
    (0 meaning not hungry at all, 5 meaning very hungry). 
    
    You will also have N sandwiches to give out which will 
    range from 1 to 20. The format of the array will be 
    [N, h1, h2, h3, ...] where N represents the number of 
    sandwiches you have and the rest of the array will 
    represent the hunger levels of different people. 
    
    Your goal is to minimize the hunger difference 
    between each pair of people in the array using the 
    sandwiches you have available.

    For example: if arr is [5, 3, 1, 2, 1], this means 
    you have 5 sandwiches to give out. You can distribute 
    them in the following order to the people: 2, 0, 1, 0. 
    Giving these sandwiches to the people their hunger levels now become: 
    [1, 1, 1, 1]. The difference between each pair of people is now 0, 
    the total is also 0, so your program should return 0. 
    Note: You may not have to give out all, or even any, of your sandwiches 
    to produce a minimized difference.

    Another example: if arr is [4, 5, 2, 3, 1, 0] then you can distribute 
    the sandwiches in the following order: [3, 0, 1, 0, 0] 
    which makes all the hunger levels the following: [2, 2, 2, 1, 0]. 
    The differences between each pair of people is now: 0, 0, 1, 1 
    and so your program should return the final minimized difference of 2.
    '''
    tuple_returned = count_diff(arr)

    old_max_diff, index_max_diff, diff_sum = tuple_returned[0], tuple_returned[1], sum(tuple_returned[2])
    
    old_sandwich = arr[0]

    if arr[0] >= old_max_diff:
        arr[0] = arr[0] - old_max_diff
        arr[index_max_diff] = arr[index_max_diff] - old_max_diff
    else:
        arr[index_max_diff] = arr[index_max_diff] - arr[0]
        arr[0] = 0

    tuple_returned = count_diff(arr)

    next_max_diff, index_max_diff, next_diff_sum = tuple_returned[0], tuple_returned[1], sum(tuple_returned[2])
 
    while old_sandwich + diff_sum + old_max_diff == next_max_diff + next_diff_sum + arr[0] and next_max_diff != 0: 
        tuple_returned = count_diff(arr)
        next_max_diff, index_max_diff = tuple_returned[0], tuple_returned[1]
         
        next_diff_sum = sum(tuple_returned[2])    
       
        if arr[0] == 0:
            break

        if arr[0] >= next_max_diff:
            arr[0] = arr[0] - next_max_diff
            arr[index_max_diff] = arr[index_max_diff] - next_max_diff
        else:
            arr[index_max_diff] = arr[index_max_diff] - arr[0]
            arr[0] = 0
        

    return next_diff_sum - arr[0]

def _input():

    sampleList = [5, 2, 3, 4, 5]

    return sampleList

def _output():

    sampleString = 1
    return sampleString
