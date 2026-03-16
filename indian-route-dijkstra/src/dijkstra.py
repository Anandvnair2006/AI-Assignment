import heapq


def dijkstra(graph, start, goal):

    pq = [(0, start, [])]
    visited = set()

    while pq:

        cost, city, path = heapq.heappop(pq)

        if city in visited:
            continue

        visited.add(city)

        path = path + [city]

        if city == goal:
            return cost, path

        for neighbor, dist in graph.get(city, []):
            heapq.heappush(pq, (cost + dist, neighbor, path))

    return None, []
