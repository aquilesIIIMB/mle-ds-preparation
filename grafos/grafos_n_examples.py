
class Node:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex  # The vertex this node represents
        self.weight = weight  # Weight of the edge (for weighted graphs)
        self.next = None      # Reference to the next node
    
    def __str__(self):
        weight_str = f" (weight: {self.weight})" if self.weight is not None else ""
        return f"{self.vertex}{weight_str}"

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def insert(self, vertex, weight=None):
        """Insert a new vertex at the beginning of the list (O(1) operation)"""
        new_node = Node(vertex, weight)
        new_node.next = self.head
        self.head = new_node
    
    def contains(self, vertex):
        """Check if a vertex exists in the linked list"""
        current = self.head
        while current:
            if current.vertex == vertex:
                return True
            current = current.next
        return False
    
    def remove(self, vertex):
        """Remove a vertex from the linked list"""
        # If the list is empty, nothing to remove
        if not self.head:
            return
        
        # If the head is the vertex to remove
        if self.head.vertex == vertex:
            self.head = self.head.next
            return
        
        # Otherwise, traverse the list
        current = self.head
        while current.next and current.next.vertex != vertex:
            current = current.next
        
        # If found, remove it
        if current.next:
            current.next = current.next.next
    
    def get_vertices(self):
        """Return all vertices in the linked list"""
        vertices = []
        current = self.head
        while current:
            vertices.append((current.vertex, current.weight))
            current = current.next
        return vertices
    
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current))
            current = current.next
        return " -> ".join(result) if result else "Empty"

## Graph Implementation Using Linked Lists

class Graph:
    def __init__(self, directed=False, weighted=False):
        self.adjacency_list = {}  # Dictionary mapping vertices to their linked lists
        self.directed = directed  # Is the graph directed?
        self.weighted = weighted  # Is the graph weighted?
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph if it doesn't exist"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = LinkedList()
    
    def add_edge(self, source, destination, weight=None):
        """Add an edge between source and destination vertices"""
        # Add vertices if they don't exist
        self.add_vertex(source)
        self.add_vertex(destination)
        
        # Only use weight if the graph is weighted
        edge_weight = weight if self.weighted else None
        
        # Add the edge from source to destination
        if not self.adjacency_list[source].contains(destination):
            self.adjacency_list[source].insert(destination, edge_weight)
        
        # For undirected graphs, add the reverse edge
        if not self.directed and not self.adjacency_list[destination].contains(source):
            self.adjacency_list[destination].insert(source, edge_weight)
    
    def remove_edge(self, source, destination):
        """Remove an edge between source and destination vertices"""
        if source in self.adjacency_list and destination in self.adjacency_list:
            self.adjacency_list[source].remove(destination)
            
            # For undirected graphs, remove the reverse edge too
            if not self.directed:
                self.adjacency_list[destination].remove(source)
    
    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges from the graph"""
        if vertex not in self.adjacency_list:
            return
        
        # Remove all edges pointing to this vertex
        for v in self.adjacency_list:
            self.adjacency_list[v].remove(vertex)
        
        # Remove the vertex itself
        del self.adjacency_list[vertex]
    
    def get_neighbors(self, vertex):
        """Get all adjacent vertices of the given vertex"""
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex].get_vertices()
        return []
    
    def has_edge(self, source, destination):
        """Check if there's an edge from source to destination"""
        if source in self.adjacency_list:
            return self.adjacency_list[source].contains(destination)
        return False
    
    def __str__(self):
        """String representation of the graph"""
        result = []
        for vertex, edges in self.adjacency_list.items():
            result.append(f"{vertex}: {edges}")
        return "\n".join(result)

#-------------------------------------
## Implementing Common Graph Algorithms
### 1. Depth-First Search (DFS)

def dfs(graph, start_vertex, visited=None):
    """Perform a depth-first search starting from start_vertex"""
    # Initialize visited set if this is the first call
    if visited is None:
        visited = set()
    
    # Mark current vertex as visited
    visited.add(start_vertex)
    print(f"Visited: {start_vertex}")
    
    # Recursively visit all unvisited neighbors
    for neighbor, _ in graph.get_neighbors(start_vertex):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

#-------------------------------------
### 2. Breadth-First Search (BFS)

from collections import deque

def bfs(graph, start_vertex):
    """Perform a breadth-first search starting from start_vertex"""
    # Set to keep track of visited vertices
    visited = set([start_vertex])
    
    # Queue for BFS
    queue = deque([start_vertex])
    
    while queue:
        # Remove a vertex from the queue
        vertex = queue.popleft()
        print(f"Visited: {vertex}")
        
        # Visit all unvisited neighbors
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited

#-------------------------------------
### 3. Dijkstra's Algorithm for Shortest Path

import heapq

def dijkstra(graph, start_vertex):
    """
    Find shortest paths from start_vertex to all other vertices
    using Dijkstra's algorithm
    """
    # Verify the graph is weighted
    if not graph.weighted:
        raise ValueError("Dijkstra's algorithm requires a weighted graph")
    
    # Initialize distances dictionary
    distances = {vertex: float('infinity') for vertex in graph.adjacency_list}
    distances[start_vertex] = 0
    
    # Initialize priority queue with start vertex
    priority_queue = [(0, start_vertex)]
    
    # Keep track of visited vertices
    visited = set()
    
    while priority_queue:
        # Get vertex with minimum distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If we've already processed this vertex, skip it
        if current_vertex in visited:
            continue
        
        # Mark vertex as visited
        visited.add(current_vertex)
        
        # If the current distance is greater than what we have stored, skip
        if current_distance > distances[current_vertex]:
            continue
        
        # Check all neighbors
        for neighbor, weight in graph.get_neighbors(current_vertex):
            if neighbor in visited:
                continue
            
            # Calculate distance to neighbor through current vertex
            distance = current_distance + weight
            
            # If this is a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

#-------------------------------------
# Create a directed, weighted graph
graph = Graph(directed=True, weighted=True)

# Add vertices
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

# Add edges
graph.add_edge("A", "B", 5)
graph.add_edge("A", "C", 3)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "D", 1)
graph.add_edge("C", "D", 8)

# Print the graph
print("Graph structure:")
print(graph)

# Perform DFS
print("\nDFS starting from A:")
dfs(graph, "A")

# Perform BFS
print("\nBFS starting from A:")
bfs(graph, "A")

# Find shortest paths using Dijkstra's algorithm
print("\nShortest paths from A:")
distances = dijkstra(graph, "A")
for vertex, distance in distances.items():
    print(f"Distance to {vertex}: {distance}")
