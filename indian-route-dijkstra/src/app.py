import os
from flask import Flask, render_template, request, jsonify

from data_loader import load_graph
from dijkstra import dijkstra


# Base project directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Flask app with correct template/static paths
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


# Load dataset
data_path = os.path.join(BASE_DIR, "data", "indian_cities_distances.csv")

graph = load_graph(data_path)

cities = sorted(list(graph.keys()))


# Home page
@app.route("/")
def home():
    return render_template("index.html", cities=cities)


# Route API
@app.route("/route", methods=["POST"])
def route():

    data = request.get_json()

    start = data["start"]
    goal = data["goal"]

    distance, path = dijkstra(graph, start, goal)

    return jsonify({
        "distance": distance,
        "path": path
    })


# Run server
if __name__ == "__main__":
    app.run(debug=True)
