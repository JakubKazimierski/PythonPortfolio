import random


def matrix(n, m):
    
    matrixOutput = []

    #O(n)
    #create matrix
    for i in range(0,n):
        matrixOutput.append([])

    #O(n*m) it's not to cool
    #update matrix with values
    for i in range(0, n):
        for j in range(0, m):
            #thanks to mod 2, only output from random is 0 or 1
            matrixOutput[i].append(( int(1000*random.random()))%2)

    return matrixOutput
