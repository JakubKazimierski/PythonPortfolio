'''
Nearest Smaller Values from Coderbyte
December 2020 Jakub Kazimierski
'''

def NearestSmallerValues(arr):
    '''
    Have the function NearestSmallerValues(arr) 
    take the array of integers stored in arr, 
    and for each element in the list, search all 
    the previous values for the nearest element that 
    is smaller than the current element and create a 
    new list from these numbers. If there is no element 
    before a certain position that is smaller, input a -1. 
    
    For example: if arr is [5, 2, 8, 3, 9, 12] then the nearest 
    smaller values list is [-1, -1, 2, 2, 3, 9]. 
    
    The logic is as follows:
    For 5, there is no smaller previous value so the list so far is [-1]. 
    For 2, there is also no smaller previous value, so the list is now [-1, -1]. 
    For 8, the nearest smaller value is 2 so the list is now [-1, -1, 2]. 
    For 3, the nearest smaller value is also 2, so the list is now [-1, -1, 2, 2]. 
    This goes on to produce the answer above. 
    
    Your program should take this final list and return the elements as a string
    separated by a space: -1 -1 2 2 3 9
    '''
    
    # before first element is nothing
    output_arr = [-1]

    for num_id in range(1, len(arr)):

        appended_smaller = False
        
        # traverse left from number before arr[num_id]
        for num in reversed(arr[:num_id]):
            # if previous num was smaller, append it to new array
            # at coderbyte solution (condition should be <= to pass tests)
            if num < arr[num_id]:
                output_arr.append(num)
                appended_smaller = True
                break

        if appended_smaller == False:
            # if none was smaller
            output_arr.append(-1)    

    return " ".join(str(num) for num in output_arr)
