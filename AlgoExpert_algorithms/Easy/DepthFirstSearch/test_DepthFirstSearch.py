'''
Unittests for DepthFirstSearch.py
January 2021 Jakub Kazimierski
'''

import unittest
from DepthFirstSearch import Node, setUp

class test_DepthFirstSearch(unittest.TestCase):    
    '''
    Class with unittests for DepthFirstSearch.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        # below creates linked Binary Tree        
        root = setUp()
    
        def traverse_for_output(node, array_out):
            '''
            Creates list of children from left down traversing
            and returns it.
            '''
            array_out.append(node.name)
            for child in node.children:
                traverse_for_output(child, array_out)

            return array_out
            
        array_out = traverse_for_output(root, [])

        output = root.depthFirstSearch([])
        self.assertEqual(output, array_out)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()