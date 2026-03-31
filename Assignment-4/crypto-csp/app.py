from flask import Flask, render_template, jsonify
from solver.crypto import solve_crypt

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/solve")
def solve():
    result = solve_crypt()
    if result:
        mapping, send, more, money = result
        return jsonify({
            "mapping": mapping,
            "equation": f"{send} + {more} = {money}"
        })
    return jsonify({"error": "No solution"})

if __name__ == "__main__":
    app.run(debug=True)
