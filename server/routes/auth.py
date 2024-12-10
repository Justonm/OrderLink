from flask import Blueprint, request, jsonify
from app import db, bcrypt
from models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    new_user = User(username=data["username"], password_hash=hashed_password, role=data.get("role", "customer"))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials"}), 401
