# server/__init__.py
import os
from flask import Flask, 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from sqlalchemy import MetaData
from .models import db
from auth import jwt

migrate = Migrate(app ,db )




app = Flask(__name__) 

    # Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '12345678'
app.json.compact = False
    
db.init_app(app)

jwt.init_app(app)
    
    # Enable CORS
CORS(app)




    # Import and register blueprints using relative imports
from .resources.auth import auth_bp
from .resources.book import book_bp
from .resources.borrowed_book import borrowed_bp
from .resources.comment import comment_bp
from .resources.favourite import favourite_bp
from .resources.profile import profile_bp
from .resources.user import user_bp

app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)
app.register_blueprint(borrowed_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(favourite_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(user_bp)

 
   


if __name__ == "__main__":
    app.run(debug=True, port=5555)
