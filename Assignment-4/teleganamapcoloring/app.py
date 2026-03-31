from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    # Run coloring script
    subprocess.run(["python", "color_map.py"])

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
