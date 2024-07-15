from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from server.models import db, Book

book_bp = Blueprint('book_bp', __name__, url_prefix='/books')
CORS(book_bp)
api_bp = Api(book_bp)

class BookResource(Resource):
    def get(self, id=None):
        if id:
            book = Book.query.get_or_404(id)
            return jsonify(book.serialize())
        else:
            books = Book.query.all()
            return jsonify([book.serialize() for book in books])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('author', type=str, required=True, help='Author is required')
        args = parser.parse_args()

        book = Book(title=args['title'], author=args['author'])
        db.session.add(book)
        db.session.commit()

        return jsonify(book.serialize()), 201

    def put(self, id):
        book = Book.query.get_or_404(id)
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('author', type=str)
        args = parser.parse_args()

        if args['title']:
            book.title = args['title']
        if args['author']:
            book.author = args['author']

        db.session.commit()

        return jsonify(book.serialize())

    def delete(self, id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return '', 204

api_bp.add_resource(BookResource, '/', '/<int:id>')
