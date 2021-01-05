'''
RREF Matrix from Coderbyte
January 2021 Jakub Kazimierski
'''

def RREF_Matrix(strArr):
    '''
    Have the function RREFMatrix(strArr) 
    take strArr which will be an array of 
    integers represented as strings. Within 
    the array there will also be "<>" elements 
    which represent break points. The array 
    will make up a matrix where the (number of 
    break points + 1) represents the number of rows. 
    
    Here is an example of how strArr may look: 
    ["5","7","8","<>","1","1","2"]. There is one "<>", 
    so 1 + 1 = 2. Therefore there will be two rows in 
    the array and the contents will be row1=[5 7 8] and 
    row2=[1 1 2]. Your program should take the given array 
    of elements, create the proper matrix, and then through 
    the process of Gaussian elimination create a reduced row 
    echelon form matrix (RREF matrix). For the array above, 
    the resulting RREF matrix would be: row1=[1 0 3], row2=[0 1 -1]. 
    Your program should return that resulting RREF matrix in string 
    form combining all the integers, like so: "10301-1". The matrix 
    can have any number of rows and columns (max=6x6 matrix and min=1x1 matrix). 
    The matrix will not necessarily be a square matrix. If the matrix is an nx1 
    matrix it will not contain the "<>" element. The integers in the array will 
    be such that the resulting RREF matrix will not contain any fractional numbers.
    '''
    
    rows = ",".join(strArr).split(",<>,")
    
    matrix = []

    for row in rows:
        matrix.append([int(elem) for elem in row.split(",")])


  row = 0 
  for col in range(0 , m):
    for i in range(row , n ):
      if matr[i][col] !=0:
        if  row != i :
          matr[i] , matr[row] = matr[row] , matr[i]

        break 

    if matr[row][col] == 0 :
      continue 

    for i in range(0 , n):
      if i == row :
        continue 
      
      a = matr[row][col]
      b = matr[i][col]

      for  k in range(0 , m):
        matr[i][k] =int( matr[i][k] * a) -int( matr[row][k] * b )


    row = row + 1 
    if row == n :
      break 


  row  = 0 
  for col in range(0, m):
    if matr[row][col] == 0 :
      continue

    for k in range(col + 1 , m ):
      matr[row][k] =matr[row][k] // matr[row][col]
       
    matr[row][col] = 1 
    row = row + 1 
    if row == n :
       break


  return "".join("".join(map(str,x)) for x in matr) 

    rref_matrix = rref(matrix)

    return 0