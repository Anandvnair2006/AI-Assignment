# UGV Battlefield Path Planner

A web-based simulation of an Unmanned Ground Vehicle (UGV) navigating a 70x70 unit battlefield grid. This project uses the **A* (A-Star) search algorithm** to find the optimal, shortest path from a starting position to a goal while avoiding known static obstacles and adapting to dynamic obstacles.

## 🚀 Features

* **70x70 Grid Environment:** Represents a large-scale area (e.g., 70x70 Km) for the UGV to traverse.
* **A* Pathfinding Algorithm:** Calculates the shortest path using the Manhattan distance heuristic, optimized with Python's `heapq` priority queue.
* **Random Obstacle Generation:** Quickly populate the battlefield with obstacles at three different density levels:
  * Low Density (15%)
  * Medium Density (30%)
  * High Density (45%)
* **Continuous Replanning (Dynamic Obstacles):** Simulates real-time sensor updates. If a new obstacle is placed directly on the current path, the system instantly recalculates a new optimal route without requiring a manual reset.
* **Performance Metrics:** Real-time tracking of:
  * Path Length (Total distance)
  * Nodes Explored (Algorithm efficiency)
  * Execution Time (in milliseconds)

## 📂 Folder Structure

To run this project correctly, ensure your files are organized exactly like this:

```text
UGV_Project/
│
├── app.py                # Main Flask server and A* algorithm logic
│
├── templates/
│   └── index.html        # Main web page interface
│
└── static/
    ├── style.css         # Styling and grid layout
    └── script.js         # Frontend logic, API calls, and dynamic rendering
