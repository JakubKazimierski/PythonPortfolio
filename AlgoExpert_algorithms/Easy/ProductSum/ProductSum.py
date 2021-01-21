'''
Product Sum from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def productSum(array):
    '''
    Write a function that takes in a "special"
    array and returns its product sum.

    A "special" array is a non-empty array that contains either
    integers or other "special" arrays. The product sum of a "special"
    array is the sum of its elements, where "special" arrays inside
    it are summed themselves and then multiplied by their level of depth.

    The depth of a "special" array is how far nested it is. For instance,
    the depth of [] is 1; the depth of the inner array in [[]]
    is 2 the depth of the innermost array in [[[]]] is 3.

    Therefore, the product sum of [x, y] is x + y; the product sum
    of [x, [y, z]] is x + 2*(y+z); the product sum of [x, [y, [z]]]
    is x + 2 *(y  +3z).
    '''
    
    def factorial(n):
        if n == 1:
            return 1
        return n*factorial(n-1)    

    def sum_list(arr, factor, sum):
        for elem in arr:
            if type(elem) is int:
                sum += factorial(factor)*elem
            else:
                sum = sum_list(elem, factor + 1, sum)
        return sum

    return sum_list(array, 1, 0)