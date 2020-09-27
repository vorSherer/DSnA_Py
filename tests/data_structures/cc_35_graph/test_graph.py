import pytest

from dsna_py.data_structures.cc_35_graph.graph import (
    Graph,
    Vertex,
    Edge,
)


def test_add_graph():
    graph = Graph()
    assert graph


# Node can be successfully added to the graph
def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex('spam')
    assert vertex.value == 'spam'


# An edge can be successfully added to the graph
def test_add_edge():
    graph = Graph()
    starting = graph.add_vertex('spam')
    ending = graph.add_vertex ('egg')
    graph.add_edge(starting, ending)
    assert graph.adjacency_list[starting][0].vertex == ending


def test_add_edge_get_size_pass():
    graph = Graph()
    starting = graph.add_vertex('spam')
    ending = graph.add_vertex ('egg')
    graph.add_edge(starting, ending)
    assert len(graph.adjacency_list) == 2


def test_add_edge_get_size_fail():
    graph = Graph()
    starting = graph.add_vertex('spam')
    ending = graph.add_vertex ('egg')
    graph.add_edge(starting, ending)
    assert len(graph.adjacency_list) != 3


def test_add_two_edges():
    graph = Graph()
    starting = graph.add_vertex('spam')
    first_node = graph.add_vertex('egg')
    second_node = graph.add_vertex('sausage')
    graph.add_edge(starting, first_node)
    graph.add_edge(starting, second_node)
    assert graph.adjacency_list[starting][1].vertex == second_node


# A collection of all nodes can be properly retrieved from the graph
@pytest.mark.skip
def test_get_vertices():
    graph = Graph()
    starting = graph.add_vertex('spam')
    first_node = graph.add_vertex('egg')
    second_node = graph.add_vertex('sausage')
    third_node = graph.add_vertex('bacon')
    graph.add_edge(starting, first_node)
    graph.add_edge(starting, second_node)
    graph.add_edge(starting, third_node)
    vertices = graph.get_vertices
    assert vertices == ['spam', 'egg', 'sausage', 'bacon']


# All appropriate neighbors can be retrieved from the graph

# Neighbors are returned with the weight between nodes included

# The proper size is returned, representing the number of nodes in the graph

# A graph with only one node and edge can be properly returned

# An empty graph properly returns null
