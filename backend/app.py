from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/log', methods=['POST'])
def log_workout():
    data = request.json
    user = data["user"]
    if user not in users:
        users[user] = []
    users[user].append(data["workout"])
    return jsonify({"message": "Тренування збережено!"})

@app.route('/history/<user>', methods=['GET'])
def get_history(user):
    return jsonify(users.get(user, []))

if __name__ == '__main__':
    app.run(debug=True)
