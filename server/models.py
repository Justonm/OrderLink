from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), default="customer")  # customer or chef
    orders = db.relationship("Order", back_populates="user")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship("Order", back_populates="menu_item")

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    menu_item_id = db.Column(db.Integer, db.ForeignKey("menu_item.id"))
    status = db.Column(db.String(50), default="Pending")
    table_number = db.Column(db.String(20), nullable=False)

    user = db.relationship("User", back_populates="orders")
    menu_item = db.relationship("MenuItem", back_populates="orders")
