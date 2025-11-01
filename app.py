from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}


@app.route("/api/create_user", methods=["POST"])
def api_create_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = password
    return jsonify({"message": "User created successfully."}), 201


@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username not in users:
        return jsonify({"success": False, "error": "User not found"}), 404
    if users[username] == password:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "error": "Invalid password"}), 401


@app.route("/api/users", methods=["GET"])
def api_show_users():
    return jsonify({"users": list(users.keys())})


if __name__ == "__main__":
    app.run(debug=True)
