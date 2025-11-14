from flask import Flask, jsonify, request, render_template
import os
import json

app = Flask(__name__)

# Path to leaderboard.json
LEADERBOARD_FILE = 'leaderboard.json'

# Ensure leaderboard.json exists with initial structure
def init_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        initial_data = {"circle": [], "square": [], "triangle": []}
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump(initial_data, f, indent=2)

# Initialize leaderboard file on startup
init_leaderboard()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leaderboard.json', methods=['GET'])
def get_leaderboard():
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        print(f"Error reading leaderboard: {e}")
        return jsonify({"circle": [], "square": [], "triangle": []}), 200

@app.route('/leaderboard.json', methods=['POST'])
def update_leaderboard():
    try:
        data = request.get_json()
        if not data or not isinstance(data, dict) or 'circle' not in data or 'square' not in data or 'triangle' not in data:
            return jsonify({"error": "Invalid leaderboard data"}), 400
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        return jsonify({"message": "Leaderboard updated"}), 200
    except Exception as e:
        print(f"Error updating leaderboard: {e}")
        return jsonify({"error": "Failed to update leaderboard"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)