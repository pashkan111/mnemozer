from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_migrate import Migrate
from api import NoteApi

app = Flask(__name__)

app.secret_key = 'qwppqpje34jeejejejje12hdhd'


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/mnemozer"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

from models import db
migrate = Migrate(app, db)

api = Api(app)


api.add_resource(NoteApi, '/notes')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)