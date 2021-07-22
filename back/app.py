from flask_migrate import Migrate
from flask_restful import Api
from api import (
    NoteApi, NoteMonthApi, CreateNote, Register, Login, Test
    )
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from __init__ import create_app

app = create_app()

jwt = JWTManager(app)
cors = CORS(app, resources=[r'/notes', r'/notes-month'], origins=["http://localhost:3000"])
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)

api.add_resource(NoteApi, '/notes')
api.add_resource(NoteMonthApi, '/notes-month')
api.add_resource(CreateNote, '/notes-create')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Test, '/test')


if __name__ == '__main__':
    app.run(debug=True)
