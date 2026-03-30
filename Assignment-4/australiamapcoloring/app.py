from flask import Flask, render_template, jsonify

app = Flask(__name__)

REGIONS = ['WA', 'NT', 'SA', 'QLD', 'NSW', 'V', 'T']

NEIGHBORS = {
    'WA':  ['NT', 'SA'],
    'NT':  ['WA', 'SA', 'QLD'],
    'SA':  ['WA', 'NT', 'QLD', 'NSW', 'V'],
    'QLD': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'QLD', 'V'],
    'V':   ['SA', 'NSW'],
    'T':   []
}

COLORS = ['Red', 'Green', 'Blue']

def is_valid(region, color, assignment):
    return all(assignment.get(n) != color for n in NEIGHBORS[region])

def backtrack(assignment, steps):
    if len(assignment) == len(REGIONS):
        steps.append({'type': 'solved', 'assignment': dict(assignment)})
        return True

    region = next(r for r in REGIONS if r not in assignment)

    for color in COLORS:
        if is_valid(region, color, assignment):
            assignment[region] = color
            steps.append({'type': 'assign', 'region': region, 'color': color, 'assignment': dict(assignment)})

            if backtrack(assignment, steps):
                return True

            del assignment[region]
            steps.append({'type': 'backtrack', 'region': region, 'assignment': dict(assignment)})

        else:
            steps.append({'type': 'conflict', 'region': region, 'color': color, 'assignment': dict(assignment)})

    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/solve')
def solve_api():
    steps = []
    backtrack({}, steps)
    print("STEPS:", len(steps))   # DEBUG
    return jsonify({"steps": steps})

if __name__ == '__main__':
    app.run(debug=True)
