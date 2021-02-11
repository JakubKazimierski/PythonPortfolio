'''
Longest Palindromic Substring from AlgoExpert.io
February 2021 Jakub Kazimierski
''' 

def longestPalindromicSubstring(string):
    '''
    Write a function that, given a string, returns
    its longest palindromic substring.

    A palindrome is defined as a string that's written 
    the same forward and backward. Note that single-character
    strings are palindromes.

    You can assume that there will only be one longest
    palindromic substring.
    '''

    def getLongestPalindrome(string, left_idx, right_idx):
        '''
        Returns indexes of begining and end of palindromic substring.
        Time O(n) | space O(1)
        '''
        while left_idx >= 0 and right_idx < len(string):
            if string[left_idx] != string[right_idx]:
                break
            left_idx -= 1
            right_idx += 1
        # if loop is break (string[left_idx] != string[left_idx]
        # or idxs are out of range so in both cases we have to return
        # incremented left idx and left right idx becuse range of string is till 
        # right_idx but not include it)    
        return [left_idx+1, right_idx]    

    # array of indexes (letter itself is palindorme)
    currentLongest = [0,1]

    for idx in range(len(string)):
        #Time O(n) | space O(1)

        odd_idx = getLongestPalindrome(string, idx-1, idx+1)
        even_idx = getLongestPalindrome(string, idx-1, idx)
        
        longest = max(odd_idx, even_idx, key = lambda arr: arr[1] - arr[0] )

        currentLongest = max(currentLongest, longest, key = lambda arr: arr[1] - arr[0] )
    
    # space O(n)
    return string[currentLongest[0]:currentLongest[1]]   

    # Total time and space of above algorithm:
    # Time O(n^2) | space O(n)