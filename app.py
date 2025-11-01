from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120), nullable=False)


with app.app_context():
    db.create_all()


# API endpoints
@app.route("/api/create_user", methods=["POST"])
def api_create_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully."}), 201


@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"success": False, "error": "User not found"}), 404
    if user.password == password:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "error": "Invalid password"}), 401


@app.route("/api/users", methods=["GET"])
def api_show_users():
    users = [user.username for user in User.query.all()]
    return jsonify({"users": users})


# Frontend endpoints
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    message = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            message = "Username and password required."
        elif User.query.filter_by(username=username).first():
            message = "User already exists."
        else:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            message = "User created successfully."
    return render_template("register.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if not user:
            message = "User not found."
        elif user.password == password:
            message = "Login successful."
        else:
            message = "Invalid password."
    return render_template("login.html", message=message)


@app.route("/users")
def show_users():
    users = [user.username for user in User.query.all()]
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
