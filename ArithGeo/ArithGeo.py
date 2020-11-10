'''
ArithGeo from codersbyte
November 2020 Jakub Kazimierski
'''

def ArithGeo(arr):
    '''
    method check if given sequence is
    arithmetic or geometric sequence
    input not contain same symbols
    also input not contain 0
    '''
    try:
        #those var will define output
        #default both are True
        isArythmetic = "True"
        isGeometric = "True"

        #bufors for differences in sequences
        bufArytm = float(arr[1]) - float(arr[0])
        bufGeo = float(arr[1])/float(arr[0])



        #in arythmetic sequence, difference beetween
        #each element coming up from previous one is const
        #iterate array till last-1 elem
        for i in range(0, len(arr)-1):
            
            bufLoopAryt = float(arr[i+1]) - float(arr[i])
            #check if value changes
            if bufArytm != bufLoopAryt:
                isArythmetic = "False"

        #in gEometric sequence value of division beetwen 
        #two coming up elements of sequence is const
        for j in range(0, len(arr)-1):

            bufLoopGeo = float(arr[j+1])/float(arr[j])
            #check if value changes
            if bufLoopGeo != bufGeo:
                isGeometric = "False"

        if isArythmetic == "True":
            return "Arithmetic"               
        elif isGeometric == "True":
            return "Geometric"
        else:    
            return -1
            
    except ZeroDivisionError:
        return -1