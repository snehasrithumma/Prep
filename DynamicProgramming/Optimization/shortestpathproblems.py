
# Dijkstra's Algorithm
# Purpose:
# Finds the shortest path from a single source vertex to all other vertices
#  in a weighted graph (where weights are non-negative).

import heapq

def dijkstra(graph, start):
    pd = []
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    heapq.heappush(pd, (0, start))

    while pd:
        current_distance, current_vertex = heapq.heappop(pd)
        if current_distance > distances[current_vertex]:
            continue
        for neighbour, weight in (graph[current_vertex].items()):
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pd, (distance, neighbour))
        print(current_vertex, pd)
    return distances



# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
print('---------')
# Floyd-Warshall Algorithm
# Purpose:
# Finds the shortest paths between all pairs of vertices in a weighted graph 
# (including both positive and negative weights, but no negative weight cycles).
def floyd_warshall(graph):
    distances = {v: dict(graph[v]) for v in graph} 
    print(distances)
    for v in graph:
        distances[v][v] = 0

    for k in graph:
        for i in graph:
            for j in graph:
                print(distances)
                distances[i][j] = min(distances[i][j], distances[i][k]+ distances[k][j])

    return distances



graph = {
    'A': {'A': 0, 'B': 3, 'C': float('infinity'), 'D': 7},
    'B': {'A': 8, 'B': 0, 'C': 2, 'D': float('infinity')},
    'C': {'A': 5, 'B': float('infinity'), 'C': 0, 'D': 1},
    'D': {'A': 2, 'B': float('infinity'), 'C': float('infinity'), 'D': 0}
}

print(floyd_warshall(graph))

# Comparison and Use Cases
    # Dijkstra's Algorithm:
        # Best for finding the shortest path from a single source to all other nodes.
        # Efficient with priority queues.
        # Only works with non-negative weights.
    # Floyd-Warshall Algorithm:
        # Best for finding the shortest paths between all pairs of nodes.
        # Handles both positive and negative weights.
        # Simpler to implement but less efficient for large graphs due to 𝑂(𝑉**3) complexity
