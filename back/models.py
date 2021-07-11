from db import db
import datetime
from sqlalchemy_serializer import SerializerMixin

class Note(db.Model, SerializerMixin):
    __tablename__ = 'notes'
    __table_args__ = {'extend_existing': True}

    serialize_only = ('id', 'name', 'description', 'date', 'time', 'status')

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.Date, default=datetime.datetime.utcnow().date())
    time = db.Column(db.Time, default=datetime.datetime.utcnow().time())
    status = db.Column(db.Boolean, default=False)
    # user = db.relationship("User", back_populates="owner")
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    
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
        notes = cls.query.filter_by(date=date).all()
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
    name = db.Column(db.String)
    phone = db.Column(db.Integer, )
    # note = db.relationship(Note, back_populates="user")


    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        
