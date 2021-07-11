import json, datetime
from flask_restful import Resource
from flask import request
from models import Note
from sqlalchemy.ext.serializer import loads, dumps


class NoteApi(Resource):

    def get(self):
        data = request.get_json()
        try:
            date = data.get('date')
        except KeyError:
            return {'status': 'data has no attribute'}, 400
        notes = Note.get_note_by_date(date)
        if notes:
            list_of_notes = []
            for i in notes:
                list_of_notes.append(i.to_dict())
            return list_of_notes
        return None



    def post(self):
        data = request.get_json()
        try:
            # name = data.get('name')
            # description = data.get('description')
            # date = data.get('date')
            # time = data.get('')
            # status = data.get('')
            note = Note(**data)
            note.save_to_db()
            return {'status': 'ok'}, 200
        except Exception:
            return {'status': 'fail'}, 400

