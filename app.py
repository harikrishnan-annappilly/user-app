from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def root():
    return "App running..."


if __name__ == "__main__":
    app.run(debug=True)
