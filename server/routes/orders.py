from flask import Blueprint, request, jsonify
from app import db
from models import Order, User, MenuItem

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["GET"])
def get_all_orders():
    orders = Order.query.all()
    return jsonify([{"id": o.id, "status": o.status, "menu_item": o.menu_item.name, "user": o.user.username} for o in orders])

@orders_bp.route("/my-orders", methods=["GET"])
def get_my_orders():
    user_id = request.args.get("user_id")
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": o.id, "status": o.status, "menu_item": o.menu_item.name} for o in orders])

@orders_bp.route("/", methods=["POST"])
def place_order():
    data = request.get_json()
    new_order = Order(
        user_id=data["user_id"],
        menu_item_id=data["menu_item_id"],
        table_number=data["table_number"]
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order placed successfully!"})

@orders_bp.route("/<int:order_id>", methods=["PATCH"])
def update_order_status(order_id):
    order = Order.query.get(order_id)
    if order:
        order.status = "Ready"
        db.session.commit()
        return jsonify({"message": "Order marked as ready"})
    return jsonify({"message": "Order not found"}), 404
