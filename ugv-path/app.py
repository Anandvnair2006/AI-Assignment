from flask import Flask, render_template, request, jsonify
import heapq
import time

app = Flask(__name__)

def heuristic(a, b):
    # Manhattan distance on a square grid
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    nodes_explored = 0

    while open_list:
        current = heapq.heappop(open_list)[1]
        nodes_explored += 1

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, nodes_explored

        neighbors = [
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1]),
            (current[0], current[1] + 1),
            (current[0], current[1] - 1)
        ]

        for n in neighbors:
            r, c = n

            # Check boundaries
            if r < 0 or c < 0 or r >= rows or c >= cols:
                continue

            # Check for obstacles (1 is an obstacle)
            if grid[r][c] == 1:
                continue

            tentative = g_score[current] + 1

            if n not in g_score or tentative < g_score[n]:
                came_from[n] = current
                g_score[n] = tentative
                f = tentative + heuristic(n, goal)
                heapq.heappush(open_list, (f, n))

    # Return None if no path is found
    return None, nodes_explored

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/find_path", methods=["POST"])
def find_path():
    data = request.json

    grid = data["grid"]
    start = tuple(data["start"])
    goal = tuple(data["goal"])

    start_time = time.time()

    path, nodes = astar(grid, start, goal)

    execution_time = (time.time() - start_time) * 1000

    return jsonify({
        "path": path,
        "nodes": nodes,
        "time": round(execution_time, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
