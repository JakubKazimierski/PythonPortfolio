'''
Fizz Buzz from Coderbyte
December 2020 Jakub Kazimierski
'''

def FizzBuzz(num):
    '''
    Have the function FizzBuzz(num) 
    take the num parameter being passed 
    and return all the numbers from 1 to num 
    separated by spaces, but replace every number 
    that is divisible by 3 with the word "Fizz", 
    replace every number that is divisible by 5 with 
    the word "Buzz", and every number that is divisible
    by both 3 and 5 with the word "FizzBuzz". 
    
    For example: if num is 16, then your program should 
    return the string 
    "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16". 
    The input will be within the range 1 - 50.
    '''
    try:
    
        output_list = []

        for number in range(1, num+1):
            if number % 15 == 0:
                output_list.append("FizzBuzz")
            elif number % 5 == 0:
                output_list.append("Buzz")
            elif number % 3 == 0:
                output_list.append("Fizz")
            else:
                output_list.append(str(number))

        return " ".join(output_list)                    
    
    except(TypeError):
        return -1