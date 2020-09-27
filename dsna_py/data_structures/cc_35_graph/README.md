# Graph
This exercise explores the implementation of graph data structure in python.

## Challenge
### Features
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

1. __AddNode()__
    - Adds a new node to the graph
    - Takes in the value of that node
    - Returns the added node <br>

1. __AddEdge()__
    - Adds a new edge between two nodes in the graph
    - Include the ability to have a “weight”
    - Takes in the two nodes to be connected by the edge
    - Both nodes should already be in the Graph <br>

1. __GetNodes()__
    - Returns all of the nodes in the graph as a collection (set, list, or similar) <br>

1. __GetNeighbors()__
    - Returns a collection of edges connected to the given node
    - Takes in a given node
    - Include the weight of the connection in the returned collection <br>

1. __Size()__
    - Returns the total number of nodes in the graph <br>

### Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

1. Node can be successfully added to the graph
1. An edge can be successfully added to the graph
1. A collection of all nodes can be properly retrieved from the graph
1. All appropriate neighbors can be retrieved from the graph
1. Neighbors are returned with the weight between nodes included
1. The proper size is returned, representing the number of nodes in the graph
1. A graph with only one node and edge can be properly returned
1. An empty graph properly returns null


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
This method has access to the full functionality of __Linked Lists__ for collision resolution.

My code is [here](./graph.py)

---

## Code Challenge 35 whiteboards:
<!-- ![CC-35 graph - 1](./RELATIVE_PATH) -->

---

## Task Checklist: <br>
- [X] Top-level README “Table of Contents” is updated <br>
- [ ] Feature tasks for this challenge are completed <br>
- [ ] Unit tests written and passing <br>
    - [ ] “Happy Path” - Expected outcome <br>
    - [ ] Expected failure <br>
    - [ ] Edge Case (if applicable/obvious) <br>
- [ ] README for this challenge is complete <br>
    - [ ] Summary, Description, Approach & Efficiency, Solution <br>
    - [X] Link to code <br>
    - [ ] Pictures of whiteboards <br>

---

###### PR for new directory: PR
Initial commit - https://github.com/vorSherer/DSnA_Py/pull/41
