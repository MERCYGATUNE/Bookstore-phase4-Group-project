from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
CORS(auth_bp)
auth_api = Api(auth_bp)
bcrypt = Bcrypt()

jwt = JWTManager()  # Initialize JWTManager

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({"msg": "Invalid email or password"}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token, "msg": "Login successful"}), 200

class ProfileResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)
        return jsonify(user.serialize()), 200

class LogoutResource(Resource):
    @jwt_required()
    def post(self):
        return jsonify({"msg": "Logout successful"}), 200

auth_api.add_resource(LoginResource, '/login')
auth_api.add_resource(ProfileResource, '/profile')
auth_api.add_resource(LogoutResource, '/logout')
