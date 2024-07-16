# server/__init__.py
import os
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from sqlalchemy import MetaData

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

# Set the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__, instance_relative_config=True) 

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'library.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = '12345678'
    app.json.compact = False
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Enable CORS
    CORS(app)

    # Initialize Flask-Restful
    api = Api(app)

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

    # Add resources to the API
    from .resources.user import UserResource
    from .resources.book import BookResource
    from .resources.profile import ProfileResource
    from .resources.borrowed_book import BorrowedBookResource
    from .resources.comment import CommentResource
    from .resources.favourite import FavouriteResource
    from .resources.auth import RegisterResource, LoginResource

    api.add_resource(UserResource, '/users', '/users/<int:id>')
    api.add_resource(BookResource, '/books', '/books/<int:id>')
    api.add_resource(ProfileResource, '/profiles', '/profiles/<int:id>')
    api.add_resource(BorrowedBookResource, '/borrowed_books', '/borrowed_books/<int:id>')
    api.add_resource(CommentResource, '/comments', '/comments/<int:id>')
    api.add_resource(FavouriteResource, '/favourites', '/favourites/<int:id>')
    api.add_resource(RegisterResource, '/auth/register')
    api.add_resource(LoginResource, '/auth/login')
    
    # Create database tables
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        response = make_response('<h1>Welcome to Inkwell Bookstore</h1>', 200)
        return response

    @app.route('/books/<int:id>')
    def book_by_id(id):
        book = Book.query.filter_by(id=id).first()
        if book:
            return make_response({'title': book.title, 'author': book.author}, 200)
        else:
            return make_response({'message': 'Book not found'}, 404)

    return app
