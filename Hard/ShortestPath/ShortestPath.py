'''
Shortest Path from Coderbyte
January 2021 Jakub Kazimierski
'''

def ShortestPath(strArr):
    '''
    Have the function ShortestPath(strArr) 
    take strArr which will be an array of 
    strings which models a non-looping Graph. 
    The structure of the array will be as follows: 
    The first element in the array will be the number 
    of nodes N (points) in the array as a string. 
    The next N elements will be the nodes which can be 
    anything (A, B, C .. Brick Street, Main Street .. etc.). 
    Then after the Nth element, the rest of the elements in 
    the array will be the connections between all of the nodes. 
    They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.). 
    Although, there may exist no connections at all.

    An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. 
    Your program should return the shortest path from the first Node to the last 
    Node in the array separated by dashes. So in the example above the output should 
    be A-B-D. 
    
    Here is another example with strArr being 
    ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]. 
    The output for this array should be A-E-D-F-G. There will only ever be one 
    shortest path for the array. If no path between the first and last node exists, 
    return -1. The array will at minimum have two nodes. Also, the connection A-B for 
    example, means that A can get to B and B can get to A.
    '''

    vertex_amount = int(strArr[0])
    vertex = strArr[1:vertex_amount+1]
    edges = strArr[vertex_amount+1:]
    graph = {}

    #graph implementation based on dictionary
    for node in vertex:
        graph[node] = set()
    
    for edge in edges:  
        # assign nodes connected to each other
        vert1, vert2 = edge.split('-')
        graph[vert1].add(vert2)
        graph[vert2].add(vert1)

    def dfs(graph, start, goal):
        '''
        Depth first search algorithm.
        Explore each possibility, before backtracking.
        Here based on stack.
        '''
        result = []
        # stack contains node, and path connected to this node
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            if vertex in graph:
                for possible_next in (graph[vertex]-set(path)):
                    if possible_next == goal:
                        result.append("-".join(path + [possible_next]))
                    else:
                        stack.append((possible_next, path + [possible_next]))
        return result
    
    output = dfs(graph, vertex[0], vertex[-1])
    return -1 if output == [] else sorted(output, key = len)[0]
