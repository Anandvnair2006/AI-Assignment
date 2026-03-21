from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "turing_secret"

# Predefined AI responses
ai_responses = [
    "That's interesting. Tell me more.",
    "Why do you think that?",
    "I see. How does that make you feel?",
    "Can you explain further?",
    "That sounds fascinating!"
]

# Simulated human responses
human_responses = [
    "Haha that reminds me of something funny.",
    "Honestly, I’m not sure about that.",
    "I completely agree with you!",
    "That’s actually a tough question.",
    "Wait, let me think about that."
]

@app.route("/")
def home():
    # Randomly decide if user chats with AI or Human
    session["agent_type"] = random.choice(["AI", "Human"])
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    agent = session.get("agent_type")

    if agent == "AI":
        reply = random.choice(ai_responses)
    else:
        reply = random.choice(human_responses)

    return jsonify({"reply": reply})

@app.route("/guess", methods=["POST"])
def guess():
    user_guess = request.json["guess"]
    actual = session.get("agent_type")

    if user_guess == actual:
        result = "Correct! You passed the Turing Test!"
    else:
        result = f"Wrong! It was actually {actual}."

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)