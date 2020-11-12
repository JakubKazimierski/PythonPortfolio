'''
MeanMode from Coderbyte
November 2020 Jakub Kazimierski
'''

from collections import Counter

def MeanMode(arr):
    '''
    return 1 if the mode equals the mean
    0 if they don't equal each other
    The input array will not be empty
    will only contain positive integers
    and will not contain more than one mode.
    '''
    try:

        #to find mode i'll use counter
        countElements = Counter(arr)

        #assign most common elem it will be mode
        #because input array will not have more than one mode
        #we can use below

        #below create list of tuple [(mostCOommonElement, howManyTimesItOccurs)]
        mode = countElements.most_common(1)


        #to find mean use math way
        #sum up all elements in list
        #and divide by amount of elements
        sumElements = sum(arr)
        amountOfElements = len(arr)
        mean = int(sumElements/amountOfElements)

        #output
        #[0] mean we only want to take first elem of list
        # which is tuple (elem, times_it_occurs)
        #next we have to take first elem of tuple
        #so mode[0][0]
        if mean == mode[0][0]:
            return 1
        else:
            return 0    

    except TypeError:
        return "Wrong Type Input"