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
        self.adjacency_list[start_node].append(edge)

# Size()
#    Returns the total number of nodes in the graph
    def size(self):
        return len(self.adjacency_list)
        
# Traversal method
    def breadth_first_search(self, start_node):
        visited = [False] * (len(self.adjacency_list))
        queue = [start_node]
        visited[start_node] = True

        while queue:
            vtx = queue.pop(0)
            
            for node in self.adjacency_list[vtx]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True

# GetNodes()
#    Returns all of the nodes in the graph as a collection (set, list, or similar)
    def get_vertices(self, start_node):
        all_nodes = self.breadth_first_search(start_node)
        return all_nodes


# GetNeighbors()
#    Returns a collection of edges connected to the given node
#    Takes in a given node
#    Include the weight of the connection in the returned collection
    def get_neighbors(self):
        pass


class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        pass


class Edge:
    def __init__(self, end_vertex, weight=1):
        self.vertex = end_vertex
        self.weight = weight





if __name__ == "__main__":
    # graph = Graph()
    graph = Graph()
    starting = graph.add_vertex('spam')
    first_node = graph.add_vertex('egg')
    second_node = graph.add_vertex('sausage')
    third_node = graph.add_vertex('bacon')
    graph.add_edge(starting, first_node)
    graph.add_edge(first_node, starting)
    graph.add_edge(starting, second_node)
    graph.add_edge(second_node, starting)
    graph.add_edge(starting, third_node)
    graph.add_edge(first_node, second_node)
    print('Size: ', graph.size())
    print('BFS: ', graph.breadth_first_search(starting))
    # print('Nodes: ', graph.get_vertices(starting))
