'''
Star Rating from Coderbyte
December 2020 Jakub Kazimierski
'''


def StarRating(strParam):
    '''
    Have the function StarRating(strParam) 
    take the str parameter being passed which 
    will be an average rating between 0.00 and 5.00, 
    and convert this rating into a list of 5 image 
    names to be displayed in a user interface to 
    represent the rating as a list of stars and half 
    stars. Ratings should be rounded to the nearest 
    half. There are 3 image file names available: 
    "full.jpg", "half.jpg", "empty.jpg". 
    The output will be the name of the 5 images 
    (without the extension), from left to right, 
    separated by spaces. 
    For example: if str is "2.36" 
    then this should be displayed by the following image:
    
    [star][star][half][empty][empty]
    '''
    
    try:

        integer_num = int(float(strParam))
        after_point = float(strParam) - integer_num

        stars = []

        for star in range(0, integer_num):
            stars.append("full")

        if len(stars) < 5:

            if after_point < 0.25:
                stars.append("empty")
            elif after_point > 0.25 and after_point < 0.75  :
                stars.append("half")
            else:
                stars.append("full")

            for star in range(0, 5 - integer_num - 1):
                stars.append("empty")


        return " ".join(stars)

    except(ValueError):
        return -1    