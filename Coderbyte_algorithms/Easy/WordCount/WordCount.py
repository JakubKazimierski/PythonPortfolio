'''
WordCount from Coderbyte
October 2020 Jakub Kazimierski
'''

def WordCount(strParam):
    '''
    Have the function WordCount(str) 
    take the string parameter being passed 
    and return the number of words the string contains 
    (e.g. "Never eat shredded wheat or cake" would return 6). 
    Words will be separated by single spaces.
    '''

    try:
        return sum(1 for word in strParam.split(" ") if len(strParam) > 0)

    except (AttributeError, TypeError):
        return -1

