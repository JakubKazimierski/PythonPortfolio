'''
MeanMode from CoderByte
Faster way of coding
November 2020 Jakub Kazimierski
'''

#to use built in functions mean and mode
import statistics


def MeanModeFaster(arr):
    '''
    return 1 if the mode equals the mean
    0 if they don't equal each other
    The input array will not be empty
    will only contain positive integers
    and will not contain more than one mode.
    '''
  
    try:
        #collection statistics has built in
        #functions mean and mode
        mean = statistics.mean(arr)
        mode = statistics.mode(arr)

        if mean == mode:
            return 1
        else:
            return 0    

    except TypeError:
        return "Wrong Type Input"

