def MineLand(matrix, field):


    #all sublist in matrix list, has to have the same length, otherwise there is no matrix
    #field[0] has to be in range n, and field[1] has to be in range m

    indexN = field[0]
    indexM = field[1]


    if indexN in range(0, len(matrix)) and indexM in range(0, len(matrix[0])):

        #we dont like to work on originall data
        outputMatrix = matrix
        visitedFieldList = []


        #field from which we start
        visitedFieldList.append([indexN, indexM])

        #if we didnt hit 1 end program
        if outputMatrix[indexN][indexM] == 1:
            return 1
        else:
            return -1

        return visitedFieldList
    else:
        return -1