from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from server.models import db, Comment

comment_bp = Blueprint('comment_bp', __name__, url_prefix='/comments')
CORS(comment_bp)
api_bp = Api(comment_bp)

class CommentResource(Resource):
    def get(self, id=None):
        if id:
            comment = Comment.query.get_or_404(id)
            return jsonify(comment.serialize())
        else:
            comments = Comment.query.all()
            return jsonify([comment.serialize() for comment in comments])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True, help='User ID is required')
        parser.add_argument('book_id', type=int, required=True, help='Book ID is required')
        parser.add_argument('text', type=str, required=True, help='Text is required')
        args = parser.parse_args()

        comment = Comment(
            user_id=args['user_id'],
            book_id=args['book_id'],
            text=args['text']
        )

        db.session.add(comment)
        db.session.commit()

        return jsonify(comment.serialize()), 201

    def put(self, id):
        comment = Comment.query.get_or_404(id)
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int)
        parser.add_argument('book_id', type=int)
        parser.add_argument('text', type=str)
        args = parser.parse_args()

        if args['user_id']:
            comment.user_id = args['user_id']
        if args['book_id']:
            comment.book_id = args['book_id']
        if args['text']:
            comment.text = args['text']

        db.session.commit()

        return jsonify(comment.serialize())

    def delete(self, id):
        comment = Comment.query.get_or_404(id)
        db.session.delete(comment)
        db.session.commit()
        return '', 204

api_bp.add_resource(CommentResource, '/', '/<int:id>')
