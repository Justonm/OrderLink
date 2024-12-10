from flask import Blueprint, request, jsonify
from app import db
from models import MenuItem

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/", methods=["GET"])
def get_menu():
    menu_items = MenuItem.query.all()
    return jsonify([{"id": m.id, "name": m.name, "price": m.price} for m in menu_items])

@menu_bp.route("/", methods=["POST"])
def add_menu_item():
    data = request.get_json()
    new_item = MenuItem(name=data["name"], price=data["price"])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Menu item added!"})
