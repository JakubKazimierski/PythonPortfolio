'''
Suffix Trie Construction from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        '''
        Populates suffix tree
        Time O(n^2) | space O(n^2)
        Where n is length of string.
        '''
        for idx in range(len(string)):
            self.insertFrom(idx, string)

    def insertFrom(self, idx, string):
        '''
        Time O(n) | space O(n) 
        where n is length of suffix
        Creates branch of tree.
        '''
        node = self.root
        for idx_2 in range(idx, len(string)):
            letter = string[idx_2]
            if letter not in node:
                # key : {} initialization
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True        


    def contains(self, string):
        '''
        Time O(n) | space O(1) 
        where n is length of suffix
        Check for suffix in tree.
        '''
        node = self.root

        for idx in range(len(string)):
            letter = string[idx]
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
