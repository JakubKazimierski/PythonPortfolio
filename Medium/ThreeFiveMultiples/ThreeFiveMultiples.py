'''
ThreeFive Multiples from Coderbyte
December 2020 Jakub Kazimierski
'''

def ThreeFiveMultiples(num):
    '''
    Have the function ThreeFiveMultiples(num) 
    return the sum of all the multiples of 3 and 5 
    that are below num. 
    
    For example: if num is 10, the multiples of 3 and 5 
    that are below 10 are 3, 5, 6, and 9, and adding them 
    up you get 23, so your program should return 23. 
    The integer being passed will be between 1 and 100.
    '''

    multiples_list = []

    for number in range(1, num):
        if number % 5 == 0 or number % 3 == 0:
            multiples_list.append(number)
        
    return sum(multiples_list)