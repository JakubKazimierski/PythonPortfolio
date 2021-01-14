'''
Command Line from Coderbyte
December 2020 Jakub Kazimierski
'''

def CommandLine(strParam):
    '''
    Have the function CommandLine(strParam) 
    take the str parameter being passed which 
    represents the parameters given to a command in 
    an old PDP system. The parameters are alphanumeric 
    tokens (without spaces) followed by an equal sign 
    and by their corresponding value. 
    Multiple parameters/value pairs can be placed on the 
    command line with a single space between each pair. 
    Parameter tokens and values cannot contain equal 
    signs but values can contain spaces. 
    The purpose of the function is to isolate the parameters 
    and values to return a list of parameter and value lengths. 
    It must provide its result in the same format and in the 
    same order by replacing each entry (tokens and values) 
    by its corresponding length.

    For example, if str is: 
    "SampleNumber=3234 provider=Dr. M. Welby patient=John Smith priority=High" 
    then your function should return the string 
    "12=4 8=12 7=10 8=4" because "SampleNumber" is a 12 character token 
    with a 4 character value ("3234") followed by "provider" which is 
    an 8 character token followed by a 12 character value ("Dr. M. Welby"), etc.
    '''

    try:
     
        lenghts = []
        segments = strParam.split('=')

        # rsplit start splitting from right, so spaces inside parameters
        # will be saved
        for segment in segments[:-1]:
            for substring in segment.rsplit(' ', 1):
                lenghts.append(len(substring))

        lenghts.append(len(segments[-1]))

        # parameters are at even indexes, and values of those at odd
        return ' '.join(f'{paramI}={paramII}' for paramI, paramII in zip(lenghts[::2], lenghts[1::2]))
    
    except(AttributeError, TypeError):
        return -1