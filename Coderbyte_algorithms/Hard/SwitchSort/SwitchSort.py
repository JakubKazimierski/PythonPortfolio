'''
Switch Sort from Coderbyte
January 2021 Jakub Kazimierski
'''

def SwitchSort(arr):
    '''
    Have the function SwitchSort(arr) 
    take arr which will be an an array 
    consisting of integers 1...size(arr) 
    and determine what the fewest number of 
    steps is in order to sort the array from 
    least to greatest using the following 
    technique: Each element E in the array can 
    swap places with another element that is arr[E] 
    spaces to the left or right of the chosen element. 
    You can loop from one end of the array to the other. 
    
    For example: if arr is the array [1, 3, 4, 2] then 
    you can choose the second element which is the number 3, 
    and if you count 3 places to the left you'll loop around the 
    array and end up at the number 4. Then you swap these elements 
    and arr is then [1, 4, 3, 2]. From here only one more step is required, 
    you choose the last element which is the number 2, count 2 places to the 
    left and you'll reach the number 4, then you swap these elements and you 
    end up with a sorted array [1, 2, 3, 4]. Your program should return an integer 
    that specifies the least amount of steps needed in order to sort the array using 
    the following switch sort technique.

    The array arr will at most contain five elements and will contain at least two elements.
    '''

    def is_sorted(array):
        for index in range(len(arr)-1):
            if arr[index] > arr[index+1]:
                return False
        return True

    arr_len, steps = len(arr), 0

    index = 0    
    while not is_sorted(arr):
        
        # indexs reached after move left or right
        move_right = (index + arr[index]) % arr_len
        move_left = (index - arr[index]) % arr_len

        # index in sorted array is one less than value at that index
        if arr[index] == index + 1:
            index = (index + 1)  % arr_len
            continue
        elif move_right + 1 == arr[index]:
            steps += 1
            arr[index], arr[move_right] = arr[move_right], arr[index]
            index = (index + 1)  % arr_len
        elif move_left + 1 == arr[index]:
            steps += 1
            arr[index], arr[move_left] = arr[move_left], arr[index]
            index = (index + 1)  % arr_len
        # if it is not possible for current value to get proper index continue
        else:
            index = (index + 1)  % arr_len

    return steps
