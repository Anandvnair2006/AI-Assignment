from collections import deque
import time

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start, goal):
    start_time = time.time()
    queue = deque([(start, [start])])
    visited = set()
    nodes = 0

    while queue:
        node, path = queue.popleft()
        nodes += 1

        if node == goal:
            return path, nodes, time.time() - start_time

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return None, nodes, time.time() - start_time


def dfs(start, goal):
    start_time = time.time()
    stack = [(start, [start])]
    visited = set()
    nodes = 0

    while stack:
        node, path = stack.pop()
        nodes += 1

        if node == goal:
            return path, nodes, time.time() - start_time

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))

    return None, nodes, time.time() - start_time


def dls(start, goal, limit):
    start_time = time.time()
    stack = [(start, [start], 0)]
    nodes = 0

    while stack:
        node, path, depth = stack.pop()
        nodes += 1

        if node == goal:
            return path, nodes, time.time() - start_time

        if depth < limit:
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor], depth + 1))

    return None, nodes, time.time() - start_time


def ids(start, goal, max_depth=10):
    total_nodes = 0
    start_time = time.time()

    for depth in range(max_depth):
        result, nodes, _ = dls(start, goal, depth)
        total_nodes += nodes
        if result:
            return result, total_nodes, time.time() - start_time

    return None, total_nodes, time.time() - start_time


def print_result(result):
    path, nodes, time_taken = result
    if path:
        print("\nPath:", path)
        print("Steps:", len(path))
        print("Nodes Expanded:", nodes)
        print("Time Taken:", round(time_taken, 6), "seconds")
    else:
        print("\nNo Path Found")


def menu():
    while True:
        print("\n--- Uninformed Search on Graph ---")
        print("1. BFS")
        print("2. DFS")
        print("3. Depth Limited Search")
        print("4. Iterative Deepening")
        print("5. Compare All")
        print("0. Exit")

        choice = input("Enter choice: ")
        start = input("Enter start node: ")
        goal = input("Enter goal node: ")

        if choice == '1':
            print_result(bfs(start, goal))

        elif choice == '2':
            print_result(dfs(start, goal))

        elif choice == '3':
            limit = int(input("Enter depth limit: "))
            print_result(dls(start, goal, limit))

        elif choice == '4':
            max_depth = int(input("Enter max depth: "))
            print_result(ids(start, goal, max_depth))

        elif choice == '5':
            print("\nBFS:")
            print_result(bfs(start, goal))
            print("\nDFS:")
            print_result(dfs(start, goal))
            print("\nIDS:")
            print_result(ids(start, goal))

        elif choice == '0':
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()