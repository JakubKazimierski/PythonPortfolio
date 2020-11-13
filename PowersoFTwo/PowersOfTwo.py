'''
PowersOfTwo from Coderbyte
November 2020 Jakub Kazimierski
'''

def PowersOfTwo(num):
    '''
    return the string true if input is a power of two.
    If it's not return the string false
    '''

    if type(num) == int:
        #work on variable with input value
        #not directly on input
        buforNum = num


        #while 2^2 to check condition 2^1 and dont get 1 after division which is power of 2
        #also make it real for negatives
        while buforNum > 2 or buforNum <(-2):

            #if odd
            if (buforNum)%2 != 0:
                return "false"
                
            else:
                #if division gives odd
                if(buforNum/2)%2 != 0:
                    return "false"
                else:
                    #assert type division gives float output
                    buforNum = int(buforNum/2)

            #odd number cannot be power of two
            #so if it is odd return false
            #if it is even divide it and check if output is even
            #if not return "false", else continue process
            #if any of conditions defining false output wasnt used
            #then number is power of two

        return "true"

    else:
        return -1

    
