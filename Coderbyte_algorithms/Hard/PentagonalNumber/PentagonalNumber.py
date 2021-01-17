'''
Pentagonal Number from Coderbyte
January 2021 Jakub Kazimierski
'''

def PentagonalNumber(num):
    '''
    Have the function PentagonalNumber(num) 
    read num which will be a positive integer 
    and determine how many dots exist in a 
    pentagonal shape around a center dot on the 
    Nth iteration. 
    
    For example, in the image below you can see that 
    on the first iteration there is only a single dot, 
    on the second iteration there are 6 dots, on the third 
    there are 16 dots, and on the fourth there are 31 dots.
    (picture is in current directory)
    
    Your program should return the number of dots that exist 
    in the whole pentagon on the Nth iteration.
    '''
    
    def count_dots(num):
        if num == 1:
            return 1
        # based on amount of dots, at next iterations at pictures
        return (num - 1)*5 + count_dots(num-1)    

    return count_dots(num)    