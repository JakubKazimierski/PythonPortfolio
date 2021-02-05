'''
Min Heap Construction fron AlgoExpert.io
February 2021 Jakub Kazimierski
'''

class MinHeap:
    '''
    Implement a MinHeap class that supports:

        -Building a Min Heap from an input array of integers
        -Inserting integers in the heap
        -Removing the heap's minimum/root value.
        -Peeking at the heap's minimum/root value.
        -Sifting integers up and down the heap,
            which is to be used when inserting and removing values

    Note that the heap should be represented in the form of an array.
    '''        

    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        '''
        Uses siftDown to build heap.
        Time o(n) | space O(1) 
        For siftUp it would be O(nlog(n)) time.
        Below link to max heap complexity (it's alike min heap)
        http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
        '''
        # starts from middle of heap (due to indexing)
        first_parent_idx = len(array)-2 // 2
        for idx in reversed(range(first_parent_idx + 1)):
            self.siftDown(idx, len(array)-1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        '''
        Sifts node down.
        Time O(log(n)) | space O(1)
        Takes heap as input, does not uses self.heap
        because this method is used when heap is building.
        '''
        left_child_idx = currentIdx*2 + 1
        while left_child_idx <= endIdx:
            
            right_child_idx = currentIdx*2 + 2 if currentIdx*2 + 2 <= endIdx else -1
            if right_child_idx != -1 and heap[left_child_idx] > heap[right_child_idx]:
                idx_to_swap = right_child_idx
            else:
                idx_to_swap = left_child_idx
            if heap[idx_to_swap] < heap[currentIdx]:
                self.swap(idx_to_swap, currentIdx, heap)
                currentIdx = idx_to_swap
                left_child_idx = currentIdx*2 + 1
            else:
                break            


    def siftUp(self, currentIdx, heap):
        '''
        Sifts node up.
        Time O(log(n)) | space O(1)
        Takes heap as input parameter. 
        (althought heap is already built when thos method is used)
        '''
        while currentIdx > 0:
            parent_idx = (currentIdx-1) // 2
            if heap[parent_idx] > heap[currentIdx]:
                self.swap(currentIdx, parent_idx, heap)
                currentIdx = parent_idx
            else:
                break    

    def peek(self):
        '''
        Returns top of min heap.
        O(1) time | O(1) space
        Can use self.heap because heap is already built
        '''
        return self.heap[0]


    def remove(self):
        '''
        Remove top of the heap.
        O(log(n)) time | O(1) space
        Can use self.heap because heap is already built.
        '''
        self.swap(0, len(self.heap)-1, self.heap)
        val_removed = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        
        return val_removed


    def insert(self, value):
        '''
        Insert value to min heap.
        O(log(n)) time | O(1) space
        Can use self.heap because heap is already built.
        '''
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)

    def swap(self, idx_I, idx_II, heap):
        '''
        Swaps node in heap.
        O(1) time | O(1) space
        Takes heap as input, does not uses self.heap
        because this method is also used when heap is building.
        '''
        heap[idx_I], heap[idx_II] = heap[idx_II], heap[idx_I]

