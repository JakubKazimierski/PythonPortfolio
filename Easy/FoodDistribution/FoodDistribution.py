'''
FoodDistribution from Coderbyte
December2020 Jakub Kazimierski
'''


import math


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

    sandwitch_cnt = arr[0]
    arr_hung_lvl = arr[1:]
    
    while sandwitch_cnt > 0 and diff_sum(arr_hung_lvl) > 0:
    
        arr_benefit = benefit_gained(arr_hung_lvl, sandwitch_cnt)
        
        # if giving sandwiches still brings optimalization
        if max(arr_benefit) > 0:
    
            best_choice_ind = arr_benefit.index(max(arr_benefit))
            arr_hung_lvl[best_choice_ind] -= 1
            sandwitch_cnt -= 1
        
        else:
            break

    output = int(diff_sum(arr_hung_lvl))
    return output

def benefit_gained(arr, sandwitch_cnt):
    '''
    This method assign to each hungLvl in array
    number which is defining to which person with 
    hungLvl we should give sandwich to gain best optimalization.

    If some people have higher lvl, than previous ones we gain better
    result if we start decreasing their lvl, than if we decrease low level
    , so their prioity is higer i queue. Also if few people have the same level
    tempDict create sequence of those levels (if those are neighbours) and assign
    them equal optimalisation number, and cheks next person, so for example
    [2,3,3,4] priorities will be like [-1,0,0,1].

    This agorithm will optimize all previous hunger level with same value as next high levels,
    but later if amount of sandwiches will be enough it will decrease those next higher levels, like it
    was done with previous ones.
    '''

    arr_benefit = []
    optimLvl = 0  # increase if next element is higher hungerLvl, decrease if it is lower
    temp = arr[0]  # used to find all equal elements in the sequence in arr
    tempDict = {0: 'Sequence start'}
    for i in range(1, len(arr)):
        
        # below makes dict longer, if neighbours' hunger levels are the same
        if arr[i] == temp:
            tempDict[i] = 'In sequence'
        
        if arr[i] != temp or i == len(arr)-1:
        
            if arr[i] < temp:
                optimLvl += 1    

            if arr[i] > temp:
                optimLvl -= 1

            # assign equal optimalization level to neighbours with same hunger level     
            if sandwitch_cnt >= len(tempDict):
                benefit = optimLvl / len(tempDict)     
            else:
                benefit = 0

            # assign the same benefit for neighbours with same hungLvl
            for _ in range(len(tempDict)):
                arr_benefit.append(benefit)
            
            if temp < arr[i]:
                optimLvl = 1  
            else:
                optimLvl = -1

            temp = arr[i]
            if i < len(arr)-1:
                tempDict = {i: 'Sequence start'}   
        
            # considering last element in the array if it's different that the previous one
            if i == len(arr)-1 and arr[i-1] != temp:
                arr_benefit.append(optimLvl)
        
    return arr_benefit

def diff_sum(arr):
    ''' 
    Returns sum of abs differences between
    next two elements in given arr
    '''
  
    diff = 0
    for i in range(len(arr)-1):
        diff += math.fabs(arr[i]-arr[i+1])
    return diff


def _input():

    sampleList = [5, 2, 3, 4, 5]

    return sampleList

def _output():

    sampleString = 1
    return sampleString
