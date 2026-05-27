from flask import Flask, request, jsonify

app = Flask(__name__)

places = {
    'beach': ['Goa', 'Pondicherry'],
    'mountains': ['Manali', 'Ooty'],
    'history': ['Hampi', 'Jaipur']
}


@app.route('/')
def home():
    return "Travel Planner API Running"


@app.route('/plan', methods=['POST'])
def plan_trip():

    data = request.json

    budget = data['budget']
    preference = data['preference']
    days = data['days']

    recommendations = places.get(preference, [])

    estimated_cost = days * 3000

    return jsonify({
        'recommended_places': recommendations,
        'estimated_cost': estimated_cost,
        'budget_ok': estimated_cost <= budget
    })


if __name__ == '__main__':
    app.run(debug=True)