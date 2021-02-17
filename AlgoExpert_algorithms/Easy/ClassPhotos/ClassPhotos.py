'''
Class Photos from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def classPhotos(redShirtHeights, blueShirtHeights):
    '''    
    It's photo day at the local school, and you're the 
    photographer assigned to take class photos. The class 
    that you'll be photographing has an even number of students, 
    and all these students are wearing red or blue shirts. In fact,
    exactly half of the class is wearing red shirts, and the other 
    half is wearing blue shirts. You're responsible for arranging the 
    students in two rows before taking the photo. Each row should 
    contain the same number of the students and should adhere to the 
    following guidelines:

        - All students wearing red shirts must be in the same row.
        - All students wearing blue shirts must be in the same row.
        - Each student in the back row must be strictly taller than 
            the student directly in front of them in the front row.

    You're given two input arrays: one containing the heights of all
    the students with red shirts and another one containing the heights
    of all the students with blue shirts. These arrays will always have
    the same length, and each height will be a positive integer. Write
    a function that returns whether or not a class photo that follows
    the stated guidelines can be taken.

    Note: you can assume that each class has at least 2 students.        
    '''

    # Time O(nlog(n)) | space O(1) where n is num of students in total
    redShirtHeights = sorted(redShirtHeights, reverse=True)
    blueShirtHeights = sorted(blueShirtHeights, reverse=True)
    
    redHigher = False
    blueHigher = False

    # below defines highest student shirt Time O(1) | space O(1) 
    if redShirtHeights[-1] > blueShirtHeights[-1]:
        redHigher = True
    elif redShirtHeights[-1] < blueShirtHeights[-1]:
        blueHigher = True
    else:
        return False            
    
    # below loop checks if rows are properly created Time O(n) | space O(1)
    for stud_I, stud_II in zip(blueShirtHeights, redShirtHeights):
        if stud_I < stud_II and blueHigher:
            return False
        elif stud_I > stud_II and redHigher:
            return False

    return True

    # Total time and space of above:
    # Time O(nlog(n)) | space O(1)