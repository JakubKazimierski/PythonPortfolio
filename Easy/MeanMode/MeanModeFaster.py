'''
MeanMode from CoderByte
Faster way of coding
November 2020 Jakub Kazimierski
'''

#to use built in functions mean and mode
import statistics


def MeanModeFaster(arr):
    '''
    Have the function MeanMode(arr) 
    take the array of numbers stored in arr 
    and return 1 if the mode equals the mean, 
    0 if they don't equal each other 
    (ie. [5, 3, 3, 3, 1] should return 1 
    because the mode (3) equals the mean (3)). 
    The array will not be empty, 
    will only contain positive integers, 
    and will not contain more than one mode.
    '''
  
    try:
        # built in mode raises StatisticsError if there is more than one mode
        # (use counter mostcommon if there is more than one mode)
        mean = statistics.mean(arr)
        mode = statistics.mode(arr)

        if mean == mode:
            return 1
        else:
            return 0    

    except TypeError:
        return "Wrong Type Input"

