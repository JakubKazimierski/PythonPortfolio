'''
NumberAddition from Coderbyte
November 2020 Jakub Kazimierski
'''

def NumberAddition(strParam):
    '''
    Have the function NumberSearch(str) 
    take the str parameter, search for all 
    the numbers in the string, add them together, 
    then return that final number. 
    For example: if str is "88Hello 3World!" 
    the output should be 91. 
    
    You will have to differentiate between single digit numbers 
    and multiple digit numbers like in the example above. 
    So "55Hello" and "5Hello 5" should return two different answers. 
    Each string will contain at least one letter or symbol.
    '''

    try:

        #numBufor
        numberBufor = ""
        #List of numbers
        numberList = []
        #final sum
        finalSum = 0

        #complexity is O(n)

        #traverse strParam array
        #if sign is digit add to buforNum
        #is sign is not digit add bufor to list of nums
        #and reset bufor

        for i in strParam:
            
            if i.isdigit():
                numberBufor += i
                #if we get last elem which is digit
                #else statement will not get to work
                #so append last num to bufor
                if i == strParam[-1]:
                    numberList.append(numberBufor)
                    numberBufor = ""        
            else:
                numberList.append(numberBufor)    
                numberBufor = ""


        #O(n) also
        #so whole function works in O(n) time
        #add up each value from list
        for j in numberList:
            #to avoid empty elements of list
            #which symbolize letters
            if j.isdigit():
                finalSum += int(j)

        return finalSum

    #if input type is wrong return error
    except TypeError:
        return -1