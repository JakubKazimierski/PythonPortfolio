'''
QuestionMarks from Coderbyte
October 2020 Jakub Kazimierski
'''

from collections import Counter


def QuestionsMarks(strParam):
    '''
    Have the function QuestionsMarks(str) 
    take the str string parameter, 
    which will contain single digit numbers, 
    letters, and question marks, and check 
    if there are exactly 3 question marks between 
    every pair of two numbers that add up to 10. 
    
    If so, then your program should return the string true,
    otherwise it should return the string false. 
    If there aren't any two numbers that add up to 10 in 
    the string, then your program should return false as well.

    For example: if str is "arrb6???4xxbl5???eee5" 
    then your program should return true because there 
    are exactly 3 question marks between 6 and 4, 
    and 3 question marks between 5 and 5 at the end of the string.
    '''

    try:
        
        output = "true"
        previousDigit_remember = 0
        questionsMarks_counter = 0
        sum_to_ten_counter = 0

        for i in strParam:
            
            if i.isdigit():
                
                if int(i) + previousDigit_remember == 10:
                    
                    sum_to_ten_counter += 1
                    
                    if questionsMarks_counter != 3:
                        output = "false"
                
                # reset question_marks counter  
                questionsMarks_counter = 0    
            
                # remember previous digit
                previousDigit_remember = int(i)
            
            elif i == "?":
                questionsMarks_counter += 1

        if sum_to_ten_counter == 0:
          output = "false"  


        return output

    except(AttributeError, TypeError, ValueError):
       return -1

def _input():
    
    exampleInput = "arrb6???4xxbl5???eee5" 

    return exampleInput

def _input():
    
    exampleOutput = "true"

    return exampleOutput
