from flask import Flask, render_template, request, jsonify
from solver.sudoku import solve_sudoku

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    board = request.json["board"]

    if solve_sudoku(board):
        return jsonify({"solution": board})
    return jsonify({"error": "No solution"})

if __name__ == "__main__":
    app.run(debug=True)
