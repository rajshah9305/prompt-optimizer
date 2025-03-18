from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prompt_optimizer.db"
db = SQLAlchemy(app)

def create_app():
    """Create the Flask application instance"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prompt_optimizer.db"
    db = SQLAlchemy(app)
    return app
