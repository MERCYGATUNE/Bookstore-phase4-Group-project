from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from server.models import db, Favourite

favourite_bp = Blueprint('favourite_bp', __name__, url_prefix='/favourites')
CORS(favourite_bp)
api_bp = Api(favourite_bp)

class FavouriteResource(Resource):
    def get(self, id=None):
        if id:
            favourite = Favourite.query.get_or_404(id)
            return jsonify(favourite.serialize())
        else:
            favourites = Favourite.query.all()
            return jsonify([favourite.serialize() for favourite in favourites])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True, help='User ID is required')
        parser.add_argument('book_id', type=int, required=True, help='Book ID is required')
        args = parser.parse_args()

        favourite = Favourite(
            user_id=args['user_id'],
            book_id=args['book_id']
        )

        db.session.add(favourite)
        db.session.commit()

        return jsonify(favourite.serialize()), 201

    def delete(self, id):
        favourite = Favourite.query.get_or_404(id)
        db.session.delete(favourite)
        db.session.commit()
        return '', 204

api_bp.add_resource(FavouriteResource, '/', '/<int:id>')
