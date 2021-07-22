import json, datetime
from flask_restful import Resource
from flask import request, jsonify
from models import Note, User
from parce_json import  UserSchema, NoteSchema
from marshmallow import ValidationError
from utils import make_dict_out_of_list
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    # jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    # get_raw_jwt,
)


class Register(Resource):
    def post(self):
        try:
            data = UserSchema.get_user_data(request.get_json())
        except ValidationError as vr:
            return vr.messages, 400
        try:
            email = data.get('email')
            phone = data.get('phone')
            password = data.get('password')
        except KeyError:
            return {'message': 'data is not full'}, 400
        if User.get_user_by_email(email):
            return {'message': 'Пользователь с таким email уже существует'}, 400
        if User.get_user_by_phone(phone):
            return {'message': 'Пользователь с таким телефоном уже существует'}, 400
        user = User(email=email, phone=phone, password=password)
        user.save_to_db()
        return user.make_json()

class Login(Resource):
    def post(self):
        try:
            data = UserSchema.get_user_data(request.get_json())
        except ValidationError as vr:
            return vr.messages, 400
        if data.__contains__('phone'):
            user = User.get_user_by_phone(data['phone'])
        elif data.__contains__('email'):
            user = User.get_user_by_email(data['email'])
        else:
            return {'message': 'Введите телефон или email'}, 400
        if not user:
            return {'message': 'Вы не зарегистрированы'}, 400
        else:
            if user['password'] == data['password']:
                access_token = create_access_token(fresh=True, identity=user['id'])
                refresh_token = create_refresh_token(identity=user['id'])
                return {
                    "id": user['id'],
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }, 200
            else:
                return {'message': 'Пароль неверный'}, 400


class NoteApi(Resource):

    def post(self):
        data = request.get_json()
        try:
            date = data.get('date')
        except KeyError:
            return {'status': 'data has no attribute'}, 400
        notes = Note.get_note_by_date(date)
        list_of_notes = []
        if notes:
            for i in notes:
                list_of_notes.append(i.to_dict())
            return list_of_notes


class NoteMonthApi(Resource):
    def post(self):
        data = request.get_json()
        try:
            month = data.get('month')
        except KeyError:
            return {'status': 'data has no attribute'}, 400
        notes = Note.get_note_by_month(month)
        result = make_dict_out_of_list(notes)
        return result


class CreateNote(Resource):
    def post(self):
        data = NoteSchema.get_note(request.get_json())
        print(data)
        try:
            user = User.query.first()
            note = Note(**data, user=user)
            note.save_to_db()
            return note.to_dict(), 201
        except Exception:
            return {'status': 'fail'}, 400


class Test(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        if user_id:
            user = User.query.filter_by(id=user_id).first()
            if user:
                return user.make_json()
            else:
                return 400
        return 401