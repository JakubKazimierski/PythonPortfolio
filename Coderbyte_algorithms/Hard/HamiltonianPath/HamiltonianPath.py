'''
Hamiltonian Path from Coderbyte
January 2021 Jakub Kazimierski
'''

def HamiltonianPath(strArr):
    '''
    Have the function HamiltonianPath(strArr) 
    take strArr which will be an array of length three. 
    The first part of the array will be a list of vertices 
    in a graph in the form (A,B,C,...), the second part of 
    the array will be the edges connecting the vertices in the form 
    (A-B,C-D,...) where each edge is bidirectional. The last part of 
    the array will be a set of vertices in the form (X,Y,Z,...) 
    and your program will have to determine whether or not the set 
    of vertices given forms a Hamiltonian path on the graph which means 
    that every vertex in the graph is visited only once in the order given.

    For example: if strArr is ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C,A,D,B)"] 
    then the vertices (C,A,D,B) in this order do in fact form a Hamiltonian path on 
    the graph so your program should return the string yes. If for example the last 
    part of the array was (D,A,B,C) then this doesn't form a Hamiltonian path because 
    once you get to B you can't get to C in the graph without passing through the visited 
    vertices again. Here your program should return the vertex where the path had to terminate, 
    in this case your program should return B.

    The graph will have at least 2 vertices and all the vertices in the graph will be connected.
    '''
    
    vertices = strArr[0].replace("(", "").replace(")", "").split(",")
    edges = strArr[1].replace("(", "").replace(")", "").split(",")
    ham_path = strArr[2].replace("(", "").replace(")", "").split(",")

    graph = {}

    path = []

    for vert in vertices:
        graph[vert] = set()

    # create graph based on dictionary
    for edge in edges:
        vert_I, vert_II = edge.split("-")
        graph[vert_I].add(vert_II)
        graph[vert_II].add(vert_I)

    # below cheks if given at input path is hamilton path
    for vert_id in range(len(ham_path)):
        path.append(ham_path[vert_id])
        if vert_id<len(ham_path)-1 and\
              ham_path[vert_id+1] in graph[ham_path[vert_id]]:
            continue
        else:
            break

    if path == ham_path:
        return "yes"
    else:
        return path[-1]    
