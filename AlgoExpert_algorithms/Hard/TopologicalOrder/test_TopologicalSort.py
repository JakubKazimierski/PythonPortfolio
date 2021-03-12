'''
Unittests for TopologicalSort.py
March 2021 Jakub Kazimierski
'''


import unittest
from TopologicalSort import topologicalSort

class test_TopologicalSort(unittest.TestCase):    
    '''
    Class with unittests for TopologicalSort.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_jobs = [1,2, 3, 4]
        self.input_deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
        self.output = [1, 4, 3, 2]

        return self.input_jobs, self.input_deps, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        jobs, deps, output = self.setUp()
        output_method = topologicalSort(jobs, deps)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()