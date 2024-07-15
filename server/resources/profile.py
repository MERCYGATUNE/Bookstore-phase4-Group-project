from flask import jsonify, request, Blueprint
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import db, Profile

profile_bp = Blueprint('profile_bp', __name__, url_prefix='/profiles')
CORS(profile_bp)
api_bp = Api(profile_bp)

class ProfileResource(Resource):
    @jwt_required()
    def get(self, id=None):
        if id:
            profile = Profile.query.get_or_404(id)
            return jsonify(profile.serialize())
        else:
            profiles = Profile.query.all()
            return jsonify([profile.serialize() for profile in profiles])

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        profile_parser = reqparse.RequestParser()
        profile_parser.add_argument('bio', type=str, required=False)
        profile_parser.add_argument('avatar', type=str, required=False)
        args = profile_parser.parse_args()

        profile = Profile(
            user_id=user_id,
            bio=args.get('bio'),
            avatar=args.get('avatar')
        )

        db.session.add(profile)
        db.session.commit()

        return jsonify(profile.serialize()), 201

    @jwt_required()
    def put(self, id):
        profile = Profile.query.get_or_404(id)
        user_id = get_jwt_identity()
        if profile.user_id != user_id:
            return jsonify({'message': 'Unauthorized access'}), 403

        profile_parser = reqparse.RequestParser()
        profile_parser.add_argument('bio', type=str)
        profile_parser.add_argument('avatar', type=str)
        args = profile_parser.parse_args()

        if args['bio'] is not None:
            profile.bio = args['bio']
        if args['avatar'] is not None:
            profile.avatar = args['avatar']

        db.session.commit()

        return jsonify(profile.serialize())

    @jwt_required()
    def delete(self, id):
        profile = Profile.query.get_or_404(id)
        user_id = get_jwt_identity()
        if profile.user_id != user_id:
            return jsonify({'message': 'Unauthorized access'}), 403

        db.session.delete(profile)
        db.session.commit()
        return '', 204

# Register the resource with the blueprint's API
api_bp.add_resource(ProfileResource, '/', '/<int:id>')
