'''
Largest Range from AlgoExpert
October 2020 Jakub Kazimierski
'''
def LargestRange(array):
    '''
    Method check for largest range of numbers coming right after each other 
    in given array e.g in array [1,2,3,6,7] largest range is [1,2,3]
    so output is [1,3]
    '''

    #first step make hash table of numbers
    #it helps to find numbers in O(n)
    numbers = {x:0 for x in array}

    #range at left and right side
    #default is zero
    left = right = 0

    for number in array:
        #condition under mean if number was not visited yet
        if numbers[number] == 0:
            left_counter = number - 1
            right_counter = number + 1

            while left_counter in numbers:
                #mark visited ones
                numbers[left_counter] = 1 
                left_counter -= 1
            #because previous one was not in numbers
            # it was for condition check value    
            # we has to return to last left counter in numbers
            left_counter += 1    
                
            while right_counter in numbers:
                #mark visited ones
                numbers[right_counter] = 1 
                right_counter += 1
            #because previous one was not in numbers
            # it was for condition check value
            # we has to return to last right counter in numbers    
            right_counter -= 1    

            #make sure that output values match loop values, and we need 
            #largest range, so smaller ones
            #does not should be remembered
            if (right - left) <= (right_counter - left_counter):
                right = right_counter
                left = left_counter

    return [left, right]