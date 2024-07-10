from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from models import db, User, Book, Order, Borrowed, Favourite, Comment
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return "<h1>Online Bookstore</h1>"

# User routes
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route("/users/<int:id>", methods=['GET', 'DELETE'])
def get_user(id):
    user_by_id = User.query.get(id)
    if not user_by_id:
        return {"error": "User not found"}, 404
    
    if request.method == 'GET':
        return jsonify(user_by_id.to_dict()), 200
    elif request.method == 'DELETE':
        db.session.delete(user_by_id)
        db.session.commit()
        return {}, 204

# Book routes
@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route("/books/<int:id>", methods=['GET'])
def get_book(id):
    book_by_id = Book.query.get(id)
    if not book_by_id:
        return {"error": "Book not found"}, 404
    
    return jsonify(book_by_id.to_dict()), 200

# Order routes
@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    try:
        new_order = Order(
            user_id=data.get("user_id"),
            book_id=data.get("book_id"),
            quantity=data.get("quantity"),
        )
    except ValueError as e:
        return {"errors": ["validation errors"]}, 400 
    
    db.session.add(new_order)
    db.session.commit()

    return jsonify(new_order.to_dict()), 201

# Borrowed routes
@app.route("/borrowed", methods=["POST"])
def create_borrowed():
    data = request.get_json()

    new_borrowed = Borrowed(
        user_id=data.get("user_id"),
        book_id=data.get("book_id"),
        borrowed_date=data.get("borrowed_date"),
        return_date=data.get("return_date")
    )
    
    db.session.add(new_borrowed)
    db.session.commit()

    return jsonify(new_borrowed.to_dict()), 201

@app.route("/borrowed/<int:id>", methods=['GET', 'DELETE'])
def get_borrowed(id):
    borrowed_by_id = Borrowed.query.get(id)
    if not borrowed_by_id:
        return {"error": "Borrowed record not found"}, 404
    
    if request.method == 'GET':
        return jsonify(borrowed_by_id.to_dict()), 200
    elif request.method == 'DELETE':
        db.session.delete(borrowed_by_id)
        db.session.commit()
        return {}, 204

# Favourite routes
@app.route("/favourites", methods=["POST"])
def create_favourite():
    data = request.get_json()

    new_favourite = Favourite(
        user_id=data.get("user_id"),
        book_id=data.get("book_id")
    )
    
    db.session.add(new_favourite)
    db.session.commit()

    return jsonify(new_favourite.to_dict()), 201

@app.route("/favourites/<int:id>", methods=['GET', 'DELETE'])
def get_favourite(id):
    favourite_by_id = Favourite.query.get(id)
    if not favourite_by_id:
        return {"error": "Favourite not found"}, 404
    
    if request.method == 'GET':
        return jsonify(favourite_by_id.to_dict()), 200
    elif request.method == 'DELETE']:
        db.session.delete(favourite_by_id)
        db.session.commit()
        return {}, 204

# Comment routes
@app.route("/comments", methods=["POST"])
def create_comment():
    data = request.get_json()

    new_comment = Comment(
        user_id=data.get("user_id"),
        book_id=data.get("book_id"),
        content=data.get("content")
    )
    
    db.session.add(new_comment)
    db.session.commit()

    return jsonify(new_comment.to_dict()), 201

@app.route("/comments/<int:id>", methods=['GET', 'DELETE'])
def get_comment(id):
    comment_by_id =
