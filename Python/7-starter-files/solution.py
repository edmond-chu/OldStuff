# Given an unweighted undirected graph, return true if it is a Cycle graph;
# else return false. A Cycle Graph is one that contains a single cycle and every
# node belongs to that cycle (it looks like a circle).
# Note that a cycle is only defined on 3 or more nodes. Any graph that contains
# less than 3 nodes cannot be a cycle graph.


def is_cycle(adj_matrix):
    """adj_matrix is an n-by-n list of lists
    representing the adjacency matrix of a simple
    graph. adj_matrix[i][i] = 0 for all i from 0 to n-1 (inclusive).
    """
