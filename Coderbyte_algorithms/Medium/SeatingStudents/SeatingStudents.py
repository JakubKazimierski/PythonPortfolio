'''
Seating Students from Coderbyte
December 2020 Jakub Kazimierski
'''

def SeatingStudents(arr):
    '''
    Have the function SeatingStudents(arr) 
    read the array of integers stored in arr 
    which will be in the following format: [K, r1, r2, r3, ...] 
    where K represents the number of desks in a classroom, and the 
    rest of the integers in the array will be in sorted order and will 
    represent the desks that are already occupied. All of the desks will 
    be arranged in 2 columns, where desk #1 is at the top left, desk #2 is 
    at the top right, desk #3 is below #1, desk #4 is below #2, etc. Your 
    program should return the number of ways 2 students can be seated next 
    to each other. This means 1 student is on the left and 1 student on the 
    right, or 1 student is directly above or below the other student.

    For example: if arr is [12, 2, 6, 7, 11] then this classrooms looks like 
    the following picture:

    1  [2]
    3   4
    5  [6]
    [7]  8
     9   10
    [11] 12

    Based on above arrangement of occupied desks, 
    there are a total of 6 ways to seat 2 new students next to 
    each other. The combinations are: 
    [1, 3], [3, 4], [3, 5], [8, 10], [9, 10], [10, 12]. 
    So for this input your program should return 6. K will range from 
    2 to 24 and will always be an even number. After K, the number of 
    occupied desks in the array can range from 0 to K.

    '''
    
    free_desks = []

    # number of desks starting from 1
    for desk_id in range(1, arr[0]+1):
        if desk_id not in arr[1:]:
            free_desks.append(desk_id)

    ways_vert = 0 
    ways_horiz = 0    

    for desk_id in free_desks:
        # for even desks check left side and table under
        if desk_id % 2 == 0:
            if desk_id - 1 in free_desks:
                ways_vert += 1
            if desk_id + 2 in free_desks:
                ways_horiz += 1
        # for odd desks check just table under, to avoid repeatition
        if desk_id % 2 == 1:
            if desk_id + 2 in free_desks:
                ways_horiz += 1


    return ways_horiz + ways_vert
            





