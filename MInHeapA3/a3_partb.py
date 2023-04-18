from a2d import Graph
#from a1_partb import SetList
from a1_partc import DisjointSet
#from a3_parta import MinHeap

#version 1 (By William, test passed):
# Purpose of this function: This function is to find the minimum spanning tree of graph (MST)
# Accept arguments of: A graph object
# Restructions: The passed in graph object must be valid (contains edges formed by weight, vertex, and end point)
# Return: An array of edges that consist of a tuple of two vertices sorted by weight and vertex in accending order
# def minimum_spanning_tree(graph):
#     # Create empty array to store the minimum spanning tree vertices
#     mst = []

#     # Create a SET for each vertex to keep track of which vertices will be in the same set
#     # Initially, each vertex is in its own set
#     sets = {v: {v} for v in graph.get_vertices()}  # a dictionary type is more efficient in this case

#     # Copy and process all the edges from the graph data to an array
#     edges = []
#     for u in graph.get_vertices():
#         for v, w in graph.get_connected(u):
#             edges.append((w, u, v))

#     # Sort the edges in accsending order by weight
#     edges.sort()

# # Iterate over the edges, adding each one to the minimum spanning tree if the set of u and v are not in the same
# set for w, u, v in edges: if sets[u] is not sets[v]:                  # if they are not in the same set,
# we can append them to the mst array mst.append((u, v))

# sets[u].update(sets[v])                 # Update the set u by merging set v for w in sets[v]:
# The loop is to update the set v so that it contains the same sets as set u sets[w] = sets[u]

#     # Return the minimum spanning tree
#     return mst


#Version 2 (By Steven, Kruskal's algorithm using disjoint set):
def mst_maze(graph):
    MST = []
    edgeSet = []
    for vA in range(len(graph)):
        for vB, w in graph[vA]:
            edgeSet.append((vA,vB,w))
    edgeSet.sort(key= lambda element: element[2])
    dSet = DisjointSet()
    for v in range(len(graph)):
        dSet.make_set(v)
    for i, j, w in edgeSet:
        ep1 = dSet.find_set(i)
        ep2 = dSet.find_set(j)
        if ep1 != ep2:
            dSet.union_set(ep1,ep2)
            MST.append((i,j))
    return MST
# Version 3 Nonthachai (edit from william to use function of dictionary)

def minimum_spanning_tree2(graph):
    mst = []
    sets = {v: {v} for v in graph.keys()}

    edges = []
    for u in graph.keys():
        for v, w in graph[u].items():
            edges.append((w,u,v))
    edges.sort()

    for w,u,v in edges:
        if sets[u] is not sets[v]:
            mst.append((u,v))
            sets[u].update(sets[v])
            for w in sets[v]:
                sets[w] = sets[u]
    return mst
