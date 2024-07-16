
from flask_restful import Resource,Api,reqparse
from models import db, BorrowedBook
from flask import Blueprint

profile_bp = Blueprint('Borrowed_book',__name__,url_prefix='/borrowed_book')
profile_api = Api({BorrowedBook_bp})





borrowed_book_parser = reqparse.RequestParser()
borrowed_book_parser.add_argument('user_id', type=int, required=True, help='User ID is required')
borrowed_book_parser.add_argument('book_id', type=int, required=True, help='Book ID is required')


class BorrowedBookResource(Resource):
    def get(self, id):
        borrowed_book = BorrowedBook.query.get_or_404(id)
        return borrowed_book.serialize()

    def put(self, id):
        data = borrowed_book_parser.parse_args()
        borrowed_book = BorrowedBook.query.get_or_404(id)
        borrowed_book.user_id = data['user_id']
        borrowed_book.book_id = data['book_id']
        borrowed_book.return_date = data.get('return_date', borrowed_book.return_date)
        db.session.commit()
        return borrowed_book.serialize()

    def delete(self, id):
        borrowed_book = BorrowedBook.query.get_or_404(id)
        db.session.delete(borrowed_book)
        db.session.commit()
        return {'message': 'Borrowed book record deleted successfully'}

class BorrowedBookListResource(Resource):
    def get(self):
        borrowed_books = BorrowedBook.query.all()
        return [borrowed_book.serialize() for borrowed_book in borrowed_books]

    def post(self):
        data = borrowed_book_parser.parse_args()
        new_borrowed_book = BorrowedBook(user_id=data['user_id'], book_id=data['book_id'])
        db.session.add(new_borrowed_book)
        db.session.commit()
        return new_borrowed_book.serialize(), 201

borrowed_books_api.add_resource(BorrowedBookResource, '/<int:id>')
borrowed_books_api.add_resource(BorrowedBookListResource, '')