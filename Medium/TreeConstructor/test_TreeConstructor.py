'''
Unittests for TreeConstructor.py from codersbyte
October 2020 Jakub Kazimierski
'''

import unittest
import TreeConstructor


class test_TreeConstructor(unittest.TestCase):
    '''
    class with unittests for TreeConstructor.py
    '''

    #region Unittests
    def test_ProperTree(self):
        '''
        check if output is true
        for proper binary tree at input
        '''
        #tree where root is 5
        output = TreeConstructor.TreeConstructor(["(1,2)","(3,2)","(2,5)","(6,5)"])
        self.assertEqual(output, "true")

    #return true for empty input
    def test_EmptyTree(self):
        '''
        check if output is false
        for empty input
        '''
        output = TreeConstructor.TreeConstructor([])
        self.assertEqual(output, "false")

    def test_JustRoot(self):
        '''
        check if output is true
        for just one node
        '''
        output = TreeConstructor.TreeConstructor(["(,1)"])
        self.assertEqual(output, "true")

    def test_JustLeaf(self):
        '''
        check if output is true
        for just one node
        '''
        output = TreeConstructor.TreeConstructor(["(1,)"])
        self.assertEqual(output, "true")

    def test_ThreeTimeParent(self):
        '''
        check if output is false
        if parent appear more than once
        '''
        output = TreeConstructor.TreeConstructor(["(1,2)","(3,2)","(5,2)","(6,5)"])
        self.assertEqual(output, "false")

    def test_SelfParent(self):
        '''
        check if output is false
        if leaf is parent of itself
        (it mean input is wrong)
        '''
        output = TreeConstructor.TreeConstructor(["(2,2)"])
        self.assertEqual(output, "false")

    def test_NotUniqeChild(self):
        '''
        check if output is false
        if child appear more than once
        '''
        output = TreeConstructor.TreeConstructor(["(1,2)","(3,2)","(1,5)"])
        self.assertEqual(output, "false")

    def test_RepeatedInput(self):
        '''
        check if uotput is false
        when input value repeat
        '''
        output = TreeConstructor.TreeConstructor(["(1,2)","(1,2)"])
        self.assertEqual(output, "false")

    def test_ChildIsParentOfParent(self):
        '''
        check if output is false
        if child is parent of it's parent
        '''
        output = TreeConstructor.TreeConstructor(["(1,2)","(2,1)"])
        self.assertEqual(output, "false")
    #endregion
    
if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()