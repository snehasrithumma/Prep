
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
