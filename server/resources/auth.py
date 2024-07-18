from flask import Blueprint, request, jsonify, session
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import db, User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
CORS(auth_bp)
auth_api = Api(auth_bp)
bcrypt = Bcrypt()

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({"msg": "Invalid email or password"}), 401

        session['user_id'] = user.id
        return jsonify({"msg": "Login successful"}), 200

class ProfileResource(Resource):
    def get(self):
        if 'user_id' not in session:
            return jsonify({"msg": "Unauthorized"}), 401

        user_id = session['user_id']
        user = User.query.get_or_404(user_id)
        return jsonify(user.serialize()), 200

class LogoutResource(Resource):
    def post(self):
        session.pop('user_id', None)
        return jsonify({"msg": "Logout successful"}), 200

auth_api.add_resource(LoginResource, '/login')
auth_api.add_resource(ProfileResource, '/profile')
auth_api.add_resource(LogoutResource, '/logout')
