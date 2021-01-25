'''
Array of Products from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def arrayOfProducts(array):
    '''
    Write a function that takes in a non-empty
    array of integers and returns an array of
    the same length, where each element in the output
    array is equal to the product of every other number
    in the input array.

    In other words, the value at output[i] is equal to the
    product of every number in the input array other than
    input[i].

    Note that you're expected to solve this problem without using
    division.
    '''

    '''
    # o(n^2) time | O(n) space
    output_arr = []
    for idx in range(len(array)):
        product = 1
        
        for left_idx in reversed(range(idx)):
            product *= array[left_idx]

        for right_idx in range(idx+1, len(array)):
            product *= array[right_idx]

        output_arr.append(product)


    return output_arr
    '''

    # O(n) time | O(n) space
    # first update elements with left products
    # after that update elements with right product
    left_product = 1
    right_product = 1
    output_arr = []

    for idx in range(len(array)):
        output_arr.append(left_product)
        # update product with last left element
        left_product *= array[idx]

    for idx in reversed(range(len(array))):
        output_arr[idx] = (output_arr[idx]*right_product)
        # update product with last right element
        right_product *= array[idx]

    return output_arr