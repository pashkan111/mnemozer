import datetime, json
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import cast, DATE, extract
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# import psycopg2
# from psycopg2.extras import DictCursor
# conn = psycopg2.connect(
#     host="localhost",
#     database="mnemozer",
#     user="postgres",
#     password="1234")
# cur = conn.cursor(cursor_factory=DictCursor)


class Note(db.Model, SerializerMixin):
    __tablename__ = 'notes'
    __table_args__ = {'extend_existing': True}

    serialize_only = ('id', 'name', 'description', 'date', 'time', 'status')
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    date_created = db.Column(db.Date(), default=datetime.datetime.utcnow().date())
    date_remind = db.Column(db.Date())
    time = db.Column(db.Time(), default=datetime.datetime.utcnow().time())
    status = db.Column(db.Boolean, default=False)
    user = db.relationship("User", back_populates="note")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    media = db.relationship('NoteMedia', back_populates="note")
   
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def find_by_user_id(cls, user_id):
        notes = cls.query.filter_by(user_id=user_id).all()
        if not notes:
            return None
        return notes

    @classmethod
    def get_note_by_date(cls, date):
        notes = cls.query.filter_by(date_created=date).all()
        if not notes:
            return None
        return notes

    @classmethod
    def get_note_by_month(cls, month):
        notes = cls.query.filter(extract('month', cast(cls.date, DATE)) == month).all()
        # cur.execute('select * from notes where extract(MONTH from cast(date as DATE))=7')
        # results = cur.fetchall()
        # row_dict = [{k:v for k, v in record.items()} for record in results]
        if not notes:
            return None
        return notes

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, index=True)
    phone = db.Column(db.Integer, nullable=True)
    telegram = db.Column(db.Integer)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=True)
    registration = db.Column(db.Date(), default=datetime.datetime.utcnow().date())
    password = db.Column(db.String)
    messangers = db.Column(db.String, nullable=True) 
    note = db.relationship(Note, back_populates="user")
    billing = db.relationship('Billing', back_populates="user")
    media = db.relationship('NoteMedia', back_populates="user")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        

class Billing(db.Model):
    __tablename__ = 'billing'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship(User, back_populates="billing")
    date = db.Column(db.Date(), default=datetime.datetime.utcnow().date())
    sum = db.Column(db.Float)
    subscribe_type = db.Column(db.String)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)  


class NoteMedia(db.Model):
    __tablename__ = 'media'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship(User, back_populates="media")
    note_id = db.Column(db.Integer, db.ForeignKey("notes.id"))
    note = db.relationship(Note, back_populates="media")    
    added = db.Column(db.Date(), default=datetime.datetime.utcnow().date())
    file = db.Column(db.LargeBinary, nullable=True)
    file_name = db.Column(db.String(50), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)
    delete_date = db.Column(db.Date())

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)   
