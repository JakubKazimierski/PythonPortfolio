'''
Farthest Node from Coderbyte
January 2021 Jakub Kazimierski
'''

import copy

def FarthestNode(strArr):
    '''
    Have the function FarthestNodes(strArr) 
    read strArr which will be an array of hyphenated
    letters representing paths between those two nodes. 
    
    For example: ["a-b","b-c","b-d"] means that there 
    is a path from node a to b (and b to a), b to c, and b to d.
    Your program should determine the longest path that exists in the graph 
    and return the length of that path. So for the example above, your 
    program should return 2 because of the paths a-b-c and d-b-c. 
    The path a-b-c also means that there is a path c-b-a. No cycles 
    will exist in the graph and every node will be connected to some 
    other node in the graph.
    '''
    
    paths = []
    for edge in strArr:

        path = []
        path.append(edge[0])
        path.append(edge[-1])

        edgeArr = copy.copy(strArr)
        edgeArr.pop(edgeArr.index(edge))

        # pop found edge if it is connected with path
        # and search for all remaining
        # below loop assert each edge is checked 
        for _ in range(len(edgeArr)):
            
            for edges in edgeArr:
                if path[-1] in edges:
                    if path[-1] == edges[0]:
                        path.append(edges[-1])
                    else:
                        path.append(edges[0])
                    edges = edgeArr.pop(edgeArr.index(edges))

                elif path[0] in edges:
                    if path[0] == edges[0]:
                        path.insert(0, edges[-1])
                    else:
                        path.insert(0, edges[0])
                    edges = edgeArr.pop(edgeArr.index(edges))

            if len(edgeArr) == 0:
                break

        paths.append(path)

    longest_path = max(paths, key=len)

    # longest_path contains nodes, so edges = |nodes|-1
    return len(longest_path)-1  
