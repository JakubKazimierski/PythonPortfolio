'''
Unittests for TreeConstructor.py 
October 2020 Jakub Kazimierski
'''

import unittest
import TreeConstructor


class test_TreeConstructor(unittest.TestCase):
    '''
    Class contains unittests for TreeConstructor.py
    '''

    #region Unittests
    def test_ProperTree(self):
        '''
        Checks if output is true for proper binary tree at input.
        '''
        #tree where root is 5
        output = TreeConstructor.TreeConstructor(["(1,2)","(3,2)","(2,5)","(6,5)"])
        self.assertEqual(output, "true")

    #return true for empty input
    def test_EmptyTree(self):
        '''
        Checks if output is false for empty input.
        '''
        output = TreeConstructor.TreeConstructor([])
        self.assertEqual(output, "false")

    def test_JustRoot(self):
        '''
        Checks if output is true for just one node.
        '''
        output = TreeConstructor.TreeConstructor(["(,1)"])
        self.assertEqual(output, "true")

    def test_JustLeaf(self):
        '''
        Checks if output is true for just one node.
        '''
        output = TreeConstructor.TreeConstructor(["(1,)"])
        self.assertEqual(output, "true")

    def test_ThreeTimeParent(self):
        '''
        Checks if output is false if parent appear more than once.
        '''
        output = TreeConstructor.TreeConstructor(["(1,2)","(3,2)","(5,2)","(6,5)"])
        self.assertEqual(output, "false")

    def test_SelfParent(self):
        '''
        Checks if output is false if leaf is parent of itself
        (it mean input is wrong).
        '''
        output = TreeConstructor.TreeConstructor(["(2,2)"])
        self.assertEqual(output, "false")

    def test_NotUniqeChild(self):
        '''
        Checks if output is false if child appear more than once.
        '''
        output = TreeConstructor.TreeConstructor(["(1,2)","(3,2)","(1,5)"])
        self.assertEqual(output, "false")

    def test_RepeatedInput(self):
        '''
        Checks if output is false when input value repeat.
        '''
        output = TreeConstructor.TreeConstructor(["(1,2)","(1,2)"])
        self.assertEqual(output, "false")

    def test_ChildIsParentOfParent(self):
        '''
        Checks if output is false if child is parent of it's parent.
        '''
        output = TreeConstructor.TreeConstructor(["(1,2)","(2,1)"])
        self.assertEqual(output, "false")
    #endregion
    
if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()