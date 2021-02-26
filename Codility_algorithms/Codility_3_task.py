'''
Codility 3 task February 2021
Jakub Kazimierski
'''

def solution(X, Y, A):
    N = len(A)
    result = -1
    nX = 0
    nY = 0
    for i in range(N):
        if A[i] == X:
            nX += 1
        if A[i] == Y:
            nY += 1
        if nX == nY:
            result = i
    return result
