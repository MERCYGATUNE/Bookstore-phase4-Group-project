from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from server.models import db, BorrowedBook

borrowed_bp = Blueprint('borrowed_book_bp', __name__, url_prefix='/borrowed_books')
CORS(borrowed_bp)
api_bp = Api(borrowed_bp)

class BorrowedBookResource(Resource):
    def get(self, id=None):
        if id:
            borrowed_book = BorrowedBook.query.get_or_404(id)
            return jsonify(borrowed_book.serialize())
        else:
            borrowed_books = BorrowedBook.query.all()
            return jsonify([borrowed_book.serialize() for borrowed_book in borrowed_books])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True, help='User ID is required')
        parser.add_argument('book_id', type=int, required=True, help='Book ID is required')
        parser.add_argument('borrowed_date', type=str, required=True, help='Borrowed date is required')
        parser.add_argument('return_date', type=str, required=False)
        args = parser.parse_args()

        borrowed_book = BorrowedBook(
            user_id=args['user_id'],
            book_id=args['book_id'],
            borrowed_date=args['borrowed_date'],
            return_date=args.get('return_date')
        )

        db.session.add(borrowed_book)
        db.session.commit()

        return jsonify(borrowed_book.serialize()), 201

    def put(self, id):
        borrowed_book = BorrowedBook.query.get_or_404(id)
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int)
        parser.add_argument('book_id', type=int)
        parser.add_argument('borrowed_date', type=str)
        parser.add_argument('return_date', type=str)
        args = parser.parse_args()

        if args['user_id']:
            borrowed_book.user_id = args['user_id']
        if args['book_id']:
            borrowed_book.book_id = args['book_id']
        if args['borrowed_date']:
            borrowed_book.borrowed_date = args['borrowed_date']
        if args['return_date']:
            borrowed_book.return_date = args['return_date']

        db.session.commit()

        return jsonify(borrowed_book.serialize())

    def delete(self, id):
        borrowed_book = BorrowedBook.query.get_or_404(id)
        db.session.delete(borrowed_book)
        db.session.commit()
        return '', 204

api_bp.add_resource(BorrowedBookResource, '/', '/<int:id>')
