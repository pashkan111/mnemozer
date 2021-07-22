from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'qwppqpje34jeejejejje1289hjhhdhd'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/mnemozer"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app
