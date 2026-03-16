# Indian Route Finder using Dijkstra Algorithm

## Overview

This project implements **Dijkstra's Algorithm (Uniform Cost Search)** to find the **shortest road distance between cities in India**.

The system models Indian cities as nodes in a graph and the road distances between them as weighted edges. Using **Uniform Cost Search**, the algorithm computes the optimal path between a selected start city and goal city.

A **web-based user interface** allows users to select cities and visualize the shortest route.

---

## Concepts Used

### State Space Representation

* **States:** Cities in India
* **Actions:** Roads connecting cities
* **Cost:** Distance between cities

The goal is to find the **minimum-cost path** from a start city to a destination city.

---

### Evaluation Function

Dijkstra's algorithm uses:

f(n) = g(n)

Where:

* **g(n)** = cost from the start node to node *n*

The algorithm always expands the node with the **lowest cumulative cost**.

---

## Algorithm

Dijkstra’s Algorithm works as follows:

1. Initialize distance to all nodes as infinity.
2. Set the distance of the start node to 0.
3. Use a **priority queue** to always expand the lowest-cost node.
4. Update distances to neighboring nodes if a shorter path is found.
5. Continue until the destination node is reached.

This guarantees the **optimal shortest path**.

---

## Project Structure

```
indian-route-dijkstra/
│
├── data/
│   └── indian_cities_distances.csv
│
├── src/
│   ├── app.py
│   ├── dijkstra.py
│   └── data_loader.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Pandas
* Graph Algorithms

---

## Dataset

The dataset contains road distances between Indian cities.

Example:

```
Origin,Destination,Distance
Agra,Delhi,240
Agra,Lucknow,334
Ahmedabad,Mumbai,526
Ahmedabad,Pune,663
```

This dataset is converted into a **graph structure** for route computation.

---

## Installation

Install dependencies:

```
pip install flask pandas
```

---

## Running the Application

Navigate to the source folder:

```
cd src
```

Run the Flask server:

```
python app.py
```

Open the application in a browser:

```
http://127.0.0.1:5000
```

---

## Features

* Interactive web UI
* City selection using dropdown menus
* Shortest path calculation
* Distance computation using Dijkstra's algorithm
* Fast response using Flask backend

---

## Example Output

Start City: **Agra**
Destination: **Mumbai**

Result:

```
Path: Agra → Delhi → Jaipur → Ahmedabad → Mumbai
Distance: XXXX km
```

---

## Measures of Effectiveness

The performance of the algorithm can be evaluated using:

* Path length (total distance)
* Number of nodes expanded
* Computation time
* Memory usage

---

## Applications

This approach can be applied in:

* GPS navigation systems
* Logistics route planning
* Transportation optimization
* Autonomous vehicle navigation

---

## Future Improvements

Possible improvements include:

* Interactive map visualization using OpenStreetMap
* Larger datasets with more cities
* Real-time traffic integration
* Advanced pathfinding algorithms such as **A*** or **D***.

---

## Author

Anand Nair
Computer Science Student

---

