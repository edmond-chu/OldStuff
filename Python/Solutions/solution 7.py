# Given an unweighted undirected graph, return true if it is a Cycle graph;
# else return false. A Cycle Graph is one that contains a single cycle and every
# node belongs to that cycle (it looks like a circle).
# Note that a cycle is only defined on 3 or more nodes. Any graph that contains
# less than 3 nodes cannot be a cycle graph.

#this program uses a depth first search helper function that is recursively called
#to check for every visited vertex whether or not there is an adjacent vertex that
#is already visited, but not the parent of the vertex currently visited. If true,
#it returns true. Time complexity is O(V+E), with space complexity of O(V)

#This method takes four parameters, the matrix, the vertex, a set that holds
#the visited nodes, and the parent. When we find an adjacent vertex that
#is not the parent, it returns true
def dfs(adj_matrix,v, visited, parent):
    #adds vertex to visited set
    visited.add(v)
    for curr in range(len(adj_matrix[0])):
        if (adj_matrix[v][curr]):
            #if it is the parent, it skips the recursive call
            if(curr == parent):
                continue
            if(curr in visited) or (dfs(adj_matrix,curr,visited,v)):
                return True
    #if the true condition is not met, it returns false
    return False

#This method takes a given graph and outputs true if a cycle is found by calling
#the helper
def is_cycle(adj_matrix):
    """adj_matrix is an n-by-n list of lists
    representing the adjacency matrix of a simple
    graph. adj_matrix[i][i] = 0 for all i from 0 to n-1 (inclusive).
    """
    #if it is none, returns false
    if adj_matrix == None:
        return False
    #creates a visited set
    visited = set()
    #for all vertices j in the graph, if j is not in the visited set,
    #then perform the dfs recursive call. If it is itrue, return true
    for j in range(len(adj_matrix)):
        if(j in visited):
            continue
        if(dfs(adj_matrix,j,visited,-1)):
            return True
    return False
