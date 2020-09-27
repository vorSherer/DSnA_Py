class Graph:
    def __init__(self):
        self.adjacency_list = {}

# AddNode()
#    Adds a new node to the graph
#    Takes in the value of that node
#    Returns the added node
    def add_vertex(self, value):
        new_vertex = Vertex(value)
        # add vertex to the adjacency list
        self.adjacency_list[new_vertex] = []
        return new_vertex

# AddEdge()
#    Adds a new edge between two nodes in the graph
#    Include the ability to have a “weight”
#    Takes in the two nodes to be connected by the edge
#    Both nodes should already be in the Graph
    def add_edge(self, start_node, end_node, weight=1):
        # check that both nodes exist in the graph
        if start_node not in self.adjacency_list:
            raise KeyError('Starting node not in the graph')
        if end_node not in self.adjacency_list:
            raise KeyError('Ending node not in the graph')
        edge = Edge(end_node, weight)
        adjacencies = self.adjacency_list[start_node]
        adjacencies.append(edge)

# Size()
#    Returns the total number of nodes in the graph
    def size(self):
        return len(self.adjacency_list)
        
# GetNodes()
#    Returns all of the nodes in the graph as a collection (set, list, or similar)
    def get_vertices(self):
        pass


# GetNeighbors()
#    Returns a collection of edges connected to the given node
#    Takes in a given node
#    Include the weight of the connection in the returned collection


class Vertex:
    def __init__(self, value):
        self.value = value



class Edge:
    def __init__(self, end_vertex, weight=1):
        self.vertex = end_vertex
        self.weight = weight




if __name__ == "__main__":
    graph = Graph('a')
    print(Graph)
