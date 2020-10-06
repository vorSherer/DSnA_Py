#  Create a function that accepts an adjacency list as a graph, and conducts a depth first traversal. Without utilizing any of the built-in methods available to your language, return a collection of nodes in their __pre-order__ depth-first traversal order.
from dsna_py.data_structures.cc_35_graph import Graph
# Need to import Stack

# Traversal method
def depth_first_search(graph):
    visited = []
    # Specify a starting node
    start_node = graph.adjacency_list[0]
    stack = Stack(start_node)
    visited.append(start_node)

    while stack:
        current = stack.pop()
        
        for neighbor in graph.adjacency_list[current]:
            if not neighbor in visited:
                stack.append(neighbor)
                visited.append(neighbor)

        # Traversal goes here
    return visited
