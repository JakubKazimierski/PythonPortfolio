'''
Unittests for YoungestCommonAncestor.py
January 2021 Jakub Kazimierski
'''

import unittest
from YoungestCommonAncestor import AncestralTree, getYoungestCommonAncestor

class test_YoungestCommonAncestor(unittest.TestCase):    
    '''
    Class with unittests for YoungestCommonAncestor.py
    '''

    def setUp(self):
        '''
        SetUp tree for tests.
        '''

        self.root = AncestralTree('A')
        self.B = AncestralTree('B')
        self.C = AncestralTree('C')
        self.D = AncestralTree('D')
        self.E = AncestralTree('E')
        self.F = AncestralTree('F')
        self.G = AncestralTree('G')
        self.H = AncestralTree('H')
        self.I = AncestralTree('I')
        
        self.B.ancestor = self.root
        self.C.ancestor = self.root
        self.D.ancestor = self.B
        self.E.ancestor = self.B
        self.H.ancestor = self.D
        self.I.ancestor = self.D
        self.F.ancestor = self.C
        self.G.ancestor = self.C

        return self.root, self.E, self.I, self.B


    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        topAncestor, descendantOne, descendantTwo, output_node = self.setUp() 
        output = getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo)
        self.assertEqual(output, output_node)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()