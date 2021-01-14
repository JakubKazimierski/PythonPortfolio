'''
SecondGreatLow from codersbyte
November 2020 Jakub Kazimierski
'''

def SecondGreatLow(arr):
    '''
    Have the function SecondGreatLow(arr) 
    take the array of numbers stored in arr 
    and return the second lowest and second greatest 
    numbers, respectively, separated by a space. 
    
    For example: if arr contains [7, 7, 12, 98, 106] 
    the output should be "12 98". 
    The array will not be empty and will contain at least 2 numbers. 
    It can get tricky if there's just two numbers!
    '''
    
    try:

        # make set of uniqe values
        setOfNumbers = set(arr)

        # if there are just 2 uniqe values max is second min, and min is second max
        if len(setOfNumbers) < 3:
            secondMinValue = max(setOfNumbers)
            secondMaxValue = min(setOfNumbers)
            return " ".join([str(secondMinValue), str(secondMaxValue)])
        else:
            # for set containing more than 2 elements pop max and pop min
            # and assign min and max values (if it is the same number it also fullfills task condition)
            sortedSet = sorted(setOfNumbers)
            sortedSet.pop(0)
            sortedSet.pop()

            secondMinValue = min(sortedSet)
            secondMaxValue = max(sortedSet)

            return " ".join([str(secondMinValue), str(secondMaxValue)])


    except (AttributeError, TypeError, ValueError):
        return -1

