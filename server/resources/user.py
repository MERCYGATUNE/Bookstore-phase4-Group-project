from flask import jsonify, request, Blueprint
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS
from models import db, User
import bcrypt

user_bp = Blueprint('User', __name__, url_prefix='/user')
CORS(user_bp)
user_api = Api(user_bp)

class UserResource(Resource):
    @jwt_required()
    def get(self, id=None):
        if id:
            user = User.query.get_or_404(id)
            return jsonify(user.serialize())
        else:
            users = User.query.all()
            return jsonify([user.serialize() for user in users])

    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
            return jsonify({'message': 'User already exists'}), 409

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(username=username, email=email, password=hashed_password.decode('utf-8'))

        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.serialize()), 201

    @jwt_required()
    def put(self, id):
        user = User.query.get_or_404(id)
        user_id = get_jwt_identity()
        if user.id != user_id:
            return jsonify({'message': 'Unauthorized access'}), 403

        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        db.session.commit()
        return jsonify(user.serialize())

    @jwt_required()
    def delete(self, id):
        user = User.query.get_or_404(id)
        user_id = get_jwt_identity()
        if user.id != user_id:
            return jsonify({'message': 'Unauthorized access'}), 403

        db.session.delete(user)
        db.session.commit()
        return '', 204

# Register the resource with the blueprint's API
user_api.add_resource(UserResource, '/', '/<int:id>')
#localhost:5555/User/id like 1