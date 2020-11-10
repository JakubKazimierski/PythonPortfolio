'''
Array Addition I from Codersbyte
November 2020 Jakub Kazimierski
'''

def ArrayAdditionI(arr):
    '''
    return the string true if any
    combination of numbers in the array
    (excluding the largest number) 
    can be added up to equal the largest number in the array
    '''
    try:
        #arrayBufor to not work at given in input array
        arrBuf = arr
        #max value in arr
        maxNum = max(arr)
        
        #remove max elem from arrBuf
        arrBuf.remove(maxNum)

        #if sum in array without max elem 
        #is equal to maxNum program ends
        if sum(arrBuf) == maxNum:
            return 'true'
        #if sum is larger    
        elif sum(arrBuf) > maxNum:
            #check differnce between sum and maxNumber
            diff = sum(arrBuf) - maxNum
            #if arrBuf contains elem that equal differnce
            #summing up all elements is possible (just do not contain difference elem)
            if diff in arrBuf:
                return 'true'
        #if differnce is not in arrBuf summing up elements to be equal
        #maxNumber is not possible        
        return 'false'

    except TypeError:
        return -1
