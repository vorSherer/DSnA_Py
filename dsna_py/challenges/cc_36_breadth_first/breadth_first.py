 # Only copied in from cc_35, not yet integrated
 
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
