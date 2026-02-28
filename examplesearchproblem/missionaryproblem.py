from collections import deque
import time

INITIAL_STATE = (3, 3, 0)
GOAL_STATE = (0, 0, 1)

def is_valid(state):
    M, C, _ = state
    M_r = 3 - M
    C_r = 3 - C

    if M < 0 or C < 0 or M > 3 or C > 3:
        return False
    if M > 0 and C > M:
        return False
    if M_r > 0 and C_r > M_r:
        return False
    return True

def successors(state):
    M, C, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    result = []

    for m, c in moves:
        if boat == 0:
            new = (M-m, C-c, 1)
        else:
            new = (M+m, C+c, 0)

        if is_valid(new):
            result.append(new)

    return result

def bfs():
    start_time = time.time()
    queue = deque([(INITIAL_STATE, [])])
    visited = set()
    nodes = 0

    while queue:
        state, path = queue.popleft()
        nodes += 1

        if state == GOAL_STATE:
            return path + [state], nodes, time.time() - start_time

        if state not in visited:
            visited.add(state)
            for s in successors(state):
                queue.append((s, path + [state]))

    return None, nodes, time.time() - start_time

def dfs():
    start_time = time.time()
    stack = [(INITIAL_STATE, [])]
    visited = set()
    nodes = 0

    while stack:
        state, path = stack.pop()
        nodes += 1

        if state == GOAL_STATE:
            return path + [state], nodes, time.time() - start_time

        if state not in visited:
            visited.add(state)
            for s in successors(state):
                stack.append((s, path + [state]))

    return None, nodes, time.time() - start_time

def dls(limit):
    start_time = time.time()
    stack = [(INITIAL_STATE, [], 0)]
    nodes = 0

    while stack:
        state, path, depth = stack.pop()
        nodes += 1

        if state == GOAL_STATE:
            return path + [state], nodes, time.time() - start_time

        if depth < limit:
            for s in successors(state):
                stack.append((s, path + [state], depth + 1))

    return None, nodes, time.time() - start_time

def ids(max_depth=20):
    total_nodes = 0
    start_time = time.time()

    for depth in range(max_depth):
        result, nodes, _ = dls(depth)
        total_nodes += nodes
        if result:
            return result, total_nodes, time.time() - start_time

    return None, total_nodes, time.time() - start_time

def print_solution(result):
    path, nodes, time_taken = result

    if path:
        print("\nSolution Found!")
        print("Steps:", len(path))
        print("Nodes Expanded:", nodes)
        print("Time Taken:", round(time_taken, 6), "seconds")
        print("\nPath:")
        for step in path:
            print(step)
    else:
        print("\nNo Solution Found.")

def menu():
    while True:
        print("\n--- Missionaries and Cannibals ---")
        print("1. BFS")
        print("2. DFS")
        print("3. Depth Limited Search")
        print("4. Iterative Deepening Search")
        print("5. Compare All")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            print_solution(bfs())

        elif choice == '2':
            print_solution(dfs())

        elif choice == '3':
            limit = int(input("Enter depth limit: "))
            print_solution(dls(limit))

        elif choice == '4':
            max_depth = int(input("Enter max depth: "))
            print_solution(ids(max_depth))

        elif choice == '5':
            print("\nBFS:")
            print_solution(bfs())
            print("\nDFS:")
            print_solution(dfs())
            print("\nIDS:")
            print_solution(ids())

        elif choice == '0':
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()