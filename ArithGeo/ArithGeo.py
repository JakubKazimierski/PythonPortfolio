'''
ArithGeo from codersbyte
November 2020 Jakub Kazimierski
'''

def ArithGeo(arr):
    '''
    Have the function ArithGeo(arr) take the array 
    of numbers stored in arr and return the string 
    "Arithmetic" if the sequence follows an arithmetic pattern 
    or return "Geometric" if it follows a geometric pattern. 
    If the sequence doesn't follow either pattern return -1. 
    An arithmetic sequence is one where the difference between each of the numbers is consistent, 
    where as in a geometric sequence, each term after the first is multiplied by some constant 
    or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. 
    Negative numbers may be entered as parameters, 0 will not be entered, 
    and no array will contain all the same elements.
    '''
    try:
        #Those var will define output
        #default both are True
        isArythmetic = "True"
        isGeometric = "True"

        #Differences in sequences
        diffArytm = arr[1] - arr[0]
        sequenceArythmetic = arr[0]
        
        #If division output is different than integer
        #bufGeo will be float
        diffGeo = arr[1]/arr[0]
        sequenceGeometric = arr[0]

        #Complexity O(n)
        for i in arr:
            #In arythmetic sequence, difference beetween
            #each element coming up from previous one is const
            if sequenceArythmetic != i:
                isArythmetic = "False" 
            sequenceArythmetic += diffArytm        

            #In geometric sequence value of division beetwen 
            #two coming up elements of sequence is const
            if sequenceGeometric != i:
                isGeometric = "False"
            sequenceGeometric *= diffGeo    

        #First condition assert that sequence will not be 
        #geometric and arithmetic at the same time
        if isArythmetic == "True" and isGeometric == "True":
            return "Input array contains same elements"
        elif isArythmetic == "True":
            return "Arithmetic"               
        elif isGeometric == "True":
            return "Geometric"    
        else:    
            return -1
            
    except ZeroDivisionError:
        return -1