'''
Check Nums from codersbyte
October 2020 Jakub Kazimierski
'''

def CheckNums(num1,num2):
    '''
    Have the function CheckNums(num1,num2) 
    take both parameters being passed and return 
    the string true if num2 is greater than num1, 
    otherwise return the string false. 
    If the parameter values are equal to 
    each other then return the string -1.
    '''

    #Below works for each comparable type
    if num1 < num2 :
        return "true"
    elif num1 == num2:
        return "-1"
    # num2 < num1  
    else:
        return "false"

