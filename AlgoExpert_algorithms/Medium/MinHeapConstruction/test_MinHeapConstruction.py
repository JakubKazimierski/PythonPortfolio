'''
Unittests for MinHeapConstruction.py
February 2021 Jakub Kazimierski
'''

import unittest
from MinHeapConstruction import MinHeap

class test_MinHeapConstruction(unittest.TestCase):    
    '''
    Class with unittests for MinHeapConstruction.py
    '''

    def SetUp(self):
        '''
        Set Up input array.
        '''
        
        self.input_arr = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
        self.proper_heap = [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
        self.insert_76 = [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
        self.peek = -5
        self.removed_peek = [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
    
        self.proper_data = [
                            self.input_arr,
                            self.proper_heap,
                            self.insert_76,
                            self.peek,
                            self.removed_peek,
                            ]

        return self.proper_data

    # region Unittests
    def test_buildHeap(self):   
        '''
        Checks if Heap is built correctly.
        '''
        proper_data = self.SetUp()

        minHeap = MinHeap(proper_data[0])
        self.assertEqual(minHeap.heap, proper_data[1])

    def test_insert(self):   
        '''
        Checks if Heap is built correctly.
        '''
        proper_data = self.SetUp()

        minHeap = MinHeap(proper_data[0])
        minHeap.insert(76)
        self.assertEqual(minHeap.heap, proper_data[2])

    def test_peek(self):   
        '''
        Checks if Heap is built correctly.
        '''
        proper_data = self.SetUp()

        minHeap = MinHeap(proper_data[0])
        minHeap.insert(76)
        self.assertEqual(minHeap.peek(), proper_data[3])

    def test_remove_peek(self):   
        '''
        Checks if Heap is built correctly.
        '''
        proper_data = self.SetUp()

        minHeap = MinHeap(proper_data[0])
        minHeap.insert(76)
        minHeap.remove()
        self.assertEqual(minHeap.heap, proper_data[4])

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()