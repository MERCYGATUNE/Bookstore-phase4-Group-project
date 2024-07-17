
from flask_restful import Resource,Api,reqparse
from models import db, BorrowedBook
from flask import Blueprint
from datetime import datetime

borrowed_bp = Blueprint('borrowed',__name__,url_prefix='/borrowed')
borrowed_api = Api(borrowed_bp)





borrowed_parser = reqparse.RequestParser()
borrowed_parser.add_argument('user_id', type=int, required=True, help='User ID is required')
borrowed_parser.add_argument('book_id', type=int, required=True, help='Book ID is required')
borrowed_parser.add_argument('title', type=str, required=True, help='Book title is required')
borrowed_parser.add_argument('return_date', type=str, required=False, help='Return date in ISO format (optional)')
borrowed_parser.add_argument('borrowed_date', type=str, required=False, help='Borrowed date in ISO format (optional)')
class BorrowedBookResource(Resource):
    def get(self, id):
        borrowed = BorrowedBook.query.get_or_404(id)
        return borrowed.serialize()

    def put(self, id):
        data = borrowed_parser.parse_args()
        borrowed = BorrowedBook.query.get_or_404(id)
        borrowed.user_id = data['user_id']
        borrowed.book_id = data['book_id']
        borrowed.title = data.get('title', borrowed.title) 
        borrowed.return_date = data.get('return_date', borrowed.return_date)
        borrowed.borrowed_date = data.get('borrowed_date', borrowed.borrowed_date)
        db.session.commit()
        return borrowed.serialize()

    def delete(self, id):
        borrowed = BorrowedBook.query.get_or_404(id)
        db.session.delete(borrowed)
        db.session.commit()
        return {'message': 'Borrowed book record deleted successfully'}

class BorrowedBookListResource(Resource):
    def get(self):
        borroweds = BorrowedBook.query.all()
        return [borrowed.serialize() for borrowed in borroweds]

    def post(self):
        data = borrowed_parser.parse_args()
        new_borrowed= BorrowedBook(user_id=data['user_id'], book_id=data['book_id'],title=data.get('title'),borrowed_date=data.get('borrowed_date'),return_date=data.get('return_date'))
        db.session.add(new_borrowed)
        db.session.commit()
        return new_borrowed.serialize(), 201

borrowed_api.add_resource(BorrowedBookResource, '/<int:id>')
borrowed_api.add_resource(BorrowedBookListResource, '/borrowedlist')

#localhost:5555/borrowed/1
#localhost:5555/borrowed/borrowedlist