'''
String Periods from Coderbyte
December 2020 Jakub Kazimierski
'''

def StringPeriods(strParam):
    '''
    Have the function StringPeriods(strParam) 
    take the str parameter being passed and 
    determine if there is some substring K that 
    can be repeated N > 1 times to produce the 
    input string exactly as it appears. 
    Your program should return the longest
    substring K, and if there is none of it 
    should return the string -1.

    For example: if str is "abcababcababcab" 
    then your program should return abcab because 
    that is the longest substring that is repeated 3 
    times to create the final string. 
    
    Another example: if str is "abababababab" then 
    your program should return ababab because it 
    is the longest substring. If the input string 
    contains only a single character, your program 
    should return the string -1.
    '''

    try:
        
        if len(strParam) == 1:
            return "-1"

        substring = ""
        pattern = ""
        substr_list = []

        # below cheks substrings of max lenght = len(strParam)//2
        for index in range(0, len(strParam)//2):
            substring += strParam[index]

            # below cheks if len of substring is divisor of len strParam
            if len(strParam) % len(substring) == 0:
                while len(pattern) < len(strParam):
                    pattern += substring 

                if pattern == strParam:
                    substr_list.append(substring)

                pattern = ""                

        if len(substr_list) != 0:
            return max(substr_list, key=len)

        return "-1"

    except(TypeError):
        return -1