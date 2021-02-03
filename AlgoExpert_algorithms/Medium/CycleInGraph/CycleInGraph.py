'''
Cycle in Graph from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def cycleInGraph(edges):
    '''
    You're given a list of edges representing
    an unweighted, directed graph with at least
    one node. Write a function that returns a
    boolean representing whether the given graph
    contains a cycle.

    For the purpose of this question, a cycle is defined
    as any number of vertices, including just one vertex
    in which the first vertex is the same as the last.

    The given list is what's called an adjacency list,
    and it represents a graph. The number of vertices in the graph
    is equal to the length of edges, where each index i in edges 
    contains vertex i's outbond edges, in no particular order.
    Each individual edge is represented by a positive integer
    that denotes an index (a destination vertex) in the list
    that this vertex is connected to. Note that these edges are
    directed, meaning that you can only travel from a particular
    vertex to its destination, non the other way around (unless the
    destination vertex itself has an outbound edge to the original 
    vertex).

    Also note that this graph may contain self-loops. A self-loop is an edge
    that has the same destination and origin; in other words, it's an edge
    that connects a vertex to itself. For the purpose of this question,
    a self-loop is considered a cycle.
    '''

    # time O(vertices+edges) | spaceO(vertices) (array of colors)
    # at each stack call dfs checks given vertex edges, and in worst case there will be v(vertices) stack calls 

    # 0- white (unvisited), 1-gray (visited and on the stack), 2-black (done)
    colors = [0 for _ in range(len(edges))]

    is_cycle = False
    def depthFirstSearch(vertex_id, is_cycle):
        '''
        Time O(vertices+edges) | space O(1)
        '''

        # if vertex already is at stack, we have a cycle 
        if colors[vertex_id] == 1:
            is_cycle = True
            return is_cycle
        # mark unvisited yet vertex as grey
        elif colors[vertex_id] == 0:
            colors[vertex_id] = 1
        # if vertex is black just return    
        else:
            return

        # below loop cheks all possible edges
        for vertex in edges[vertex_id]:
            is_cycle = depthFirstSearch(vertex, is_cycle)
            # if cycle was found in one of possible ways, return true
            if is_cycle == True:
                return is_cycle

        # after checking all of edges mark as done
        colors[vertex_id] = 2
        
    # loop over vertices O(v) < O(v+e)
    return True if any(depthFirstSearch(vertex_idx, is_cycle) for vertex_idx in range(len(edges))) else False
