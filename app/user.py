from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required
from app import db
from app.models import UserModel

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()

        new_user = UserModel(
            username=data['username'],
            password=data['password']
        )

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        current_user = UserModel.query.filter_by(username=data['username']).first()

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}, 401

        if data['password'] == current_user.password:
            access_token = create_access_token(identity={'username': current_user.username})
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token
            }
        else:
            return {'message': 'Wrong credentials'}, 401

class GetUser(Resource):
    def get(self):
        current_user = UserModel.query.all()
        out_data = []
        for user in current_user:
            data = {
                "username" : user.username,
                "password" : user.password,
            }
            out_data.append(data)
        return out_data

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return {'message': 'This is a protected resource'}
