'''
Largest Range from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def largestRange(array):
    '''
    Write a function that takes in an array
    of integers and returns an array of length
    2 representing the largest range of integers
    contained in that array.

    The first number in the output array should be
    the first number in the range, while the second
    number should be the last number in the range.

    A range of numbers is defined as a set of numbers
    that come right after each other in the set of real
    integers. For instance, the output
    array [2, 6] represents the range {2, 3, 4, 5, 6},
    which is a range of length 5. Note that numbers don't
    need to be sorted or adjacent in the input array in order
    to form a range.

    You can assume that there will only be one largest range.
    '''

    def check_range(num, num_dict, range):
        '''
        Based on info in dict if num was visited
        create range of adjacent numbers to given
        number at input. 
        
        Looking in dict takes O(1) time.
        
        Time O(n) | Space worst case O(n)
        '''
        
        if num_dict[num] == 1:
            return

        range.append(num)
        num_dict[num] = 1
        
        left_pointer = num - 1
        right_pointer = num + 1

        go_left = True
        go_right = True

        while go_left:
            if left_pointer in num_dict:
                range.append(left_pointer)
                num_dict[left_pointer] = 1
                left_pointer -= 1
            else:
                break    

        while go_right:
            if right_pointer in num_dict:
                range.append(right_pointer)
                num_dict[right_pointer] = 1    
                right_pointer += 1
            else:
                break

        return range            


    num_visited = {}
    ranges = []

    # takes O(n) time | O(n) space
    for num in array:
        num_visited[num] = 0

    for num in array:
        range = check_range(num, num_visited, [])
    
        if range is not None:
            ranges.append(range)

    max_range = max(ranges, key=len)
    return [min(max_range), max(max_range)]