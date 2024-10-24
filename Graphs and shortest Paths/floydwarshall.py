
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
