
from flask_restful import Resource,Api,reqparse
from models import db, Book
from flask import Blueprint

book_bp = Blueprint('Book',__name__,url_prefix='/Book')
book_api = Api(book_bp)



book_parser = reqparse.RequestParser()
book_parser.add_argument('title', type=str, required=True, help='Title is required')
book_parser.add_argument('author', type=str, required=True, help='Author is required')

class BookResource(Resource):
    def get(self, id):
        book = Book.query.get_or_404(id)
        return book.serialize()

    def put(self, id):
        data = book_parser.parse_args()
        book = Book.query.get_or_404(id)
        book.title = data['title']
        book.author = data['author']
        db.session.commit()
        return book.serialize()

    def delete(self, id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return {'message': 'Book deleted successfully'}

class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return [book.serialize() for book in books]

    def post(self):
        data = book_parser.parse_args()
        new_book = Book(title=data['title'], author=data['author'])
        db.session.add(new_book)
        db.session.commit()
        return new_book.serialize(), 201
    
book_api.add_resource(BookResource, '/<int:id>')
book_api.add_resource(BookListResource, '')
