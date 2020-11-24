'''
Off Line Minimum from Coderbyte
November 2020 Jakub Kazimierski
'''

def OffLineMinimum(strArr):
    '''
    take the strArr parameter being passed 
    which will be an array of integers ranging from 1...n and the letter "E" 
    return the correct subset based on the following rules. 
    The input will be in the following format: ["I","I","E","I",...,"E",...,"I"] 
    where the I's stand for integers and the E means: 
    -take out the smallest integer currently in the whole set (set mean intigers till E letter). 
    When finished, your program should return that new set
    created from taken out integers separated by commas
    '''

    #assert input type str and len
    if len(strArr) > 0:
        for i in strArr:
            if type(i) != str:
                return -1
    else:
        return -1

    #bufor list of integers till E letter
    buforList = []

    #output list
    outputList = []

    #output string because output has to be in string format
    output = ""

    #traverse input array
    for i in strArr:

        #add integers to buforList till E letter
        if i != "E":
            buforList.append(int(i))
        #when E letter
        else:
            #assert that in bufor list is at least one number
            if len(buforList) > 0:
                #add min integer to output
                outputList.append(min(buforList))
                #remove min element from buforList
                buforList.remove(min(buforList))
            else:
                continue

        #continue process till end of strArr    


    #prepare output string
    for i in outputList:

        #assign str value of integer
        output += str(i)
            
        #separate with coma if not last elemnt in list
        if i != outputList[-1]:
            output += ","



    return output