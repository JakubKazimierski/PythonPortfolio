'''
Dijkstra's Algorithm from ALgoExprert.io
March 2021 Jakub Kazimierski
'''

def dijkstra_sAlgorithm(start, edges):
    '''
    The list is what's called an adjacency list, and it
    represents a graph. The number of vertices in the graph
    is equal to the length of edges, where each idex i in edges
    contains vertex i's outbound edges, in no particular order.
    Each individual edge is represented by an pair of two numbers,
    [destination, distance], where the destination is a positive
    integer denoting the destination vertex and the distance is 
    a positive integer representing the length of the edge (the 
    distance from vertex i to vertex destination). Note that these
    edges are directed, meaning that you can only travel from a particular
    vertex to its destination-not the other way around (unless the destination
    vertex itself has an unbound edge to the original vertex).

    Write a function that computes the lengths of the shortest paths between
    start and all of other vertices in the graph using Dijkstra's algorithm and
    returns them in an array. Each index i in the output array
    should represent the length of the shortest path between start and vertex
    i. If no path is found from start to vertex i, then output[i] should be -1.

    Note that the graph represented by edges won't contain any self-loops
    (vertices that have an outbound edge to themselves) and will only
    have positively weighted edges (i.e., no negative distances).
    '''

    numberOfVertices = len(edges)

    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    minDistancesHeap = MinHeap([(idx, float("inf")) for idx in range(numberOfVertices)])
    minDistancesHeap.update(start, 0)

    while not minDistancesHeap.isEmpty():

        vertex, currentMinDistance = minDistancesHeap.remove()

        if currentMinDistance == float("inf"):
            break

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]

            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
                minDistancesHeap.update(destination, newPathDistance)

    return list(map(lambda x: -1 if x== float("inf") else x, minDistances))   

class MinHeap:
    def __init__(self, array):

        self.vertexMap = {idx: idx for idx in range(len(array))} 

        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        firstParentIdx = (len(array) -2 ) // 2

        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)

        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx*2 + 1

        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx*2 + 2 if currentIdx*2 + 2 < endIdx else -1

            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
                idxToSwap = childTwoIdx

            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap][1] < heap[currentIdx][1]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx*2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) //2
        while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def remove(self):
        if self.isEmpty():
            return

        self.swap(0, len(self.heap) - 1, self.heap)
        vertex, distance = self.heap.pop()
        self.vertexMap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return vertex, distance

    def swap(self, i, j, heap):
        self.vertexMap[heap[i][0]] = j
        self.vertexMap[heap[j][0]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def update(self, vertex, value):
        self.heap[self.vertexMap[vertex]] = (vertex, value)
        self.siftUp(self.vertexMap[vertex], self.heap)
                                                            
