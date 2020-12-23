'''
Pair Searching from Coderbyte
December 2020 Jakub Kazimierski
'''

def PairSearching(num):
    '''
    Have the function PairSearching(num) 
    take the num parameter being passed and 
    perform the following steps. First take 
    all the single digits of the input number 
    (which will always be a positive integer greater than 1) 
    and add each of them into a list. Then take the input number 
    and multiply it by any one of its own integers, then take this
    new number and append each of the digits onto the original list. 
    Continue this process until an adjacent pair of the same number 
    appears in the list. Your program should return the least number of 
    multiplications it took to find an adjacent pair of duplicate numbers.

    For example: if num is 134 then first append each of the integers into a list: 
    [1, 3, 4]. Now if we take 134 and multiply it by 3 (which is one of its own integers), 
    we get 402. Now if we append each of these new integers to the list, we get: 
    [1, 3, 4, 4, 0, 2]. We found an adjacent pair of duplicate numbers, namely 4 and 4. 
    So for this input your program should return 1 because it only took 1 multiplication to find 
    this pair.

    Another example: if num is 46 then we append these integers onto a list: [4, 6]. 
    If we multiply 46 by 6, we get 276, and appending these integers onto the list we 
    now have: [4, 6, 2, 7, 6]. Then if we take this new number, 276, and multiply it by 2 
    we get 552. Appending these integers onto the list we get: [4, 6, 2, 7, 6, 5, 5, 2]. 
    Your program should therefore return 2 because it took 2 multiplications to find a pair 
    of adjacent duplicate numbers (5 and 5 in this case).
    '''
    
    steps, nums, num_lists = 0, [num], [list(str(num))]

    while True:
        # below checks for pair
        for digit in '0123456789':
                if any(2*digit in ''.join(num_list) for num_list in num_lists): 
                    return steps
    
        steps += 1
        new_nums, new_num_lists = [], []

        # below for each digit from num, creates new num_list with added product of multiplication
        # also creates new numbers which are products of multiplication, and previous, checked for pair
        # are overwritten
        for num, num_list in zip(nums, num_lists):
            for digit in str(num):
                new_nums.append(num*int(digit))
                new_num_lists.append(num_list + list(str(num*int(digit))))
        # old list are reassigned, in order not to get repeatition in algorithm        
        nums, num_lists = new_nums, new_num_lists
            