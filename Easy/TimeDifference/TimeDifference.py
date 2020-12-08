'''
TimeDifference from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import combinations
from datetime import datetime
import operator

def TimeDifference(strArr):
    '''
    Have the function TimeDifference(strArr) 
    read the array of strings stored in strArr 
    which will be an unsorted list of times in a 
    twelve-hour format like so: HH:MM(am/pm). 
    
    Your goal is to determine the smallest difference 
    in minutes between two of the times in the list. 
    
    For example: if strArr is ["2:10pm", "1:30pm", "10:30am", "4:42pm"] 
    then your program should return 40 because the smallest difference is 
    between 1:30pm and 2:10pm with a difference of 40 minutes. 
    The input array will always contain at least two elements and all 
    of the elements will be in the correct format and unique.
    '''
    
    try:

        countable_form = []

        for time in strArr:
            countable_form.append(datetime.strptime(time, '%I:%M%p'))

        possible_combinations = list(combinations(countable_form, 2))
        
        possible_diffs = []

        # below looks for min difference in both direction of clock
        for combination in possible_combinations:
            possible_diffs.append((max(combination[0], combination[1]) \
                              - min(combination[0], combination[1])).seconds)

            possible_diffs.append((min(combination[0], combination[1]) \
                              - max(combination[0], combination[1])).seconds)
        
        min_diff_minutes = min(possible_diffs)/60

        return int(min_diff_minutes)
        
    except(AttributeError, TypeError):
        return -1

