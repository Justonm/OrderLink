from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate  # Import Flask-Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orderlink.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "your_secret_key"

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

# Import and register routes
from routes.auth import auth_bp
from routes.orders import orders_bp
from routes.menu import menu_bp

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(orders_bp, url_prefix="/api/orders")
app.register_blueprint(menu_bp, url_prefix="/api/menu")

if __name__ == "__main__":
    app.run(debug=True)
