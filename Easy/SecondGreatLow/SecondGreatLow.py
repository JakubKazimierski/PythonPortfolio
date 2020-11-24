'''
SecondGreatLow from codersbyte
November 2020 Jakub Kazimierski
'''

def SecondGreatLow(arr):
    '''
    return the second lowest and second greatest numbers, respectively
    '''
    
    try:
        #default values for output
        secondMin = None
        secondMax = None

        #range values to work with
        secondMinBufor = min(arr)
        secondMaxBufor = max(arr)

        #if array has length > 2 we can use algo under
        if len(arr) > 2:
            #check all values in arr range values
            while secondMinBufor < max(arr):

                #iterate from min to max by 1 step
                secondMinBufor += 1
                
                #if at some of steps value is in arr we have looked for value
                if secondMinBufor in arr:
                    secondMin = secondMinBufor
                    #loop has to end working aat this moment
                    break
                else:
                    continue    

            while secondMaxBufor > min(arr):

                #iterate from min to max by 1 step
                secondMaxBufor -= 1
                
                #if at some of steps value is in arr we have looked for value
                if secondMaxBufor in arr:
                    secondMax = secondMaxBufor
                    break
                else:
                    continue    

        #if array contain just 2 elem    
        else:
            secondMin = arr[0]
            secondMax = arr[1]


        return  str(secondMin) + " " + str(secondMax)

    except Exception:
        return -1

    