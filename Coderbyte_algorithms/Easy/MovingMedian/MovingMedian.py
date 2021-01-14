'''
Moving Median from Coderbyte
December 2020 Jakub Kazimierski
'''

import statistics

def MovingMedian(arr):
    '''
    Have the function MovingMedian(arr) 
    read the array of numbers stored in arr 
    which will contain a sliding window size, N, 
    as the first element in the array and the rest 
    will be a list of numbers. Your program should 
    return the Moving Median for each element based 
    on the element and its N-1 predecessors, where N 
    is the sliding window size. The final output should 
    be a string with the moving median corresponding 
    to each entry in the original array separated by commas.

    Note that for the first few elements 
    (until the window size is reached), the median is computed 
    on a smaller number of entries. 
    
    For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1] 
    then your program should output "1,2,3,5,6,6,4,3"
    '''
    try:
        median_list = []
        for i in range(1, len(arr)):
            if i < arr[0]:
                median_list.append(int(statistics.median(arr[1:i+1])))
            else:
                # n=arr[0], (n-1)th element before i, starts from index i+1-n
                start = i+1-arr[0]
                median_list.append(int(statistics.median(arr[start:i+1])))    

        return ",".join(str(median) for median in median_list)        

    except(TypeError):
        return -1    