'''
Unittests for DiskStacking.py
March 2021 Jakub Kazimierski
'''


import unittest
from DiskStacking import diskStacking

class test_DiskStacking(unittest.TestCase):    
    '''
    Class with unittests for DiskStacking.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
        
        self.output = [[2, 1, 2], [3, 2, 3], [4, 4, 5]]

        return self.input_disks, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        disks, output = self.setUp()
        output_method = diskStacking(disks)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()