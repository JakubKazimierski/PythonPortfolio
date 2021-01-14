'''
Largest Range from AlgoExpert
and Tech with Tim tutorial
October 2020 Jakub Kazimierski
'''
def LargestRange(array):
    '''
    Write a function that takes an array of integers
    and returns an array of length 2 representing the largest
    range of numbers contained in that array. The first number in 
    the output array should be the first number in the range while
    the second number should be the last number in the range.
    A range of numbers is defined as a set of numbers that come
    right after each other in the set of real integers. For instance
    the output array [2,6] represents the range {2,3,4,5,6}, which is
    a range of length 5. Note that numbers do not need to be ordered or
    adjacent in the array in order to form a range. Assume that there
    will be only one largest range.

    Sample input: [1,11,3,0,15,5,2,4,10,7,12,6]
    Sample Output: [0,7]
    '''

    #region Commentary
    #One of possible ways to solve task is to 
    #sort given array, and then iterate it in order to
    #find largest range of numbers, it is 100% correct
    #but takes O(nlogn) time because of sorting O(logn)
    #method implemented below takes O(2n) time so it is
    #still O(n) (first iterates array in O(n) to create hashtable
    # then iterates array to find largest range with help of hash table
    # it also takes O(n) time) so the second one algorithm is more efficient.

    #Below creates hash table of given numbers
    #with key 0 if not visited and 1 if visited
    #at the beginning all values are unvisited
    #it helps to find numbers in O(1)
    #althought to create hash table of n numbers
    #we have to iterate over list of this numbers
    #so it takes O(n) time
    #endregion

    try:
        # create dictionary of numbers (0 mean unvisited, 1 visited) 
        # dict in python is based on hashtables
        numbers = {x:0 for x in array}

        #range velues: left and right, default zero
        left = right = 0

        #Below loop iterates over array of n numbers in O(n) time
        for number in array:
            #If number was not visited yet 
            #(it prevents iterate over vistied values again, so algorithm does not waste time)
            if numbers[number] == 0:
                #check if numbers one less and one greater are in hashtable
                left_counter = number - 1
                right_counter = number + 1

                while left_counter in numbers:
                    #Marks visited ones
                    numbers[left_counter] = 1 
                    #Assigns next less value to left_counter
                    left_counter -= 1

                #when while loop ends left_counter is not in hashtable
                #so assign last value which was in hashtable
                left_counter += 1    

                #Same logic as for left_counter is for right_counter    
                while right_counter in numbers:
                    
                    numbers[right_counter] = 1 
                    right_counter += 1

                right_counter -= 1    

                
                #Below assigns largest found range to output values 
                if (right - left) <= (right_counter - left_counter):
                    right = right_counter
                    left = left_counter

        return [left, right]

    except TypeError:
        return "Wrong input"

