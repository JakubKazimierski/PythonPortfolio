'''
Bipartite Matching from Coderbyte
January 2021 Jakub Kazimierski
'''

from itertools import permutations

def BipartiteMatching(strArr):
    '''
    Have the function BipartiteMatching(strArr) 
    read strArr which will be an array of hyphenated 
    letters representing paths from the first node to 
    the second node. 
    
    For example: ["a->d", "a->e", "b->f", "c->e"] means 
    that there is a path from node a to d, a to e, b to f, and so on. 
    The graph will be bipartite meaning that it is possible to separate 
    the nodes into two disjoint sets such that every edge only connects 
    a node from the lefthand side to a node on the righthand side. 
    Your program should determine the maximum cardinality matching of 
    the bipartite graph, which means finding the largest possible number 
    of non-adjacent edges that are matching. 
    
    So for the example above, your program should return 3 because it is 
    possible to connect every single node on the left to a node on the right.

    The input will only contain lowercase alphabetic characters 
    with a -> between them signifying an edge between them going 
    from the left node to the right node. The input will contain at 
    least 1 edge connecting 2 nodes.
    '''
    
    possible_maxes = []
    perm = list(permutations(strArr, len(strArr)))

    for possibility in perm:

        from_node = []
        to_node = []
        
        for edge in possibility:
            if edge[0] not in from_node and\
                edge[-1] not in to_node:
                
                from_node.append(edge[0])
                to_node.append(edge[-1])

        possible_maxes.append(len(to_node))

    return max(possible_maxes)

