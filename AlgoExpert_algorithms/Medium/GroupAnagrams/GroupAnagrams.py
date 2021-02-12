'''
Group Anagrams from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def groupAnagrams(words):
    '''
    Write a function that takes in
    an array of strings and groups
    anagrams together.

    Anagrams are strings made up of
    exactly the same letters, where order
    doesn't matter. For example, "cinema"
    and "iceman" are anagrams; similarly,
    "foo" and "ofo" are anagrams.

    Your function should return a list
    of anagram groups in no particular order.
    '''

    if len(words) == 0:
        return []

    # Time O(words*n*log(n)) | space O(words*n) whre n is longest word
    sortedWords = ["".join(sorted(word)) for word in words]    
    indexes_arr = [idx for idx in range(len(words))]
    # sort indexes by alphabetical order of words idxs represents
    # Time O(n*words*log(words)) | space O(words) 
    indexes_arr.sort(key=lambda idx: sortedWords[idx])

    output_arr = []
    current_group = []
    current_anagram = sortedWords[indexes_arr[0]]
  
    # Time O(n) | Space O(n*words)
    for idx in indexes_arr:
        if sortedWords[idx] == current_anagram:
            current_group.append(words[idx])
            continue

        output_arr.append(current_group)
        current_group = [words[idx]]
        current_anagram = sortedWords[idx]

    # when loop ends one group still left, so append it
    output_arr.append(current_group)        

    return output_arr

def compare_lists(list_I, list_II):
    '''
    Method for tests, checks if both lists have the same elements.
    Time O(n^2) where n is length of list | space O(1)
    '''
    if len(list_I) != len(list_II):
        return False
    for elem in list_I:
        if elem not in list_II:
            return False    
    return True