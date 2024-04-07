from flask import Flask
from .extensions import db
from .api.event import event_blueprint
import os

# Configuration
DATABASE_URI = os.environ.get("DATABASE_URL")
# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    # Initialize app with SQLAlchemy

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(event_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # Create database tables for our data models
    app.run(host="0.0.0.0", port=3001)