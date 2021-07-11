from .db import db
import datetime


class Note(db.Model):
    __tablename__ = 'notes'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    date_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.Boolean, default=False)
    user = db.relationship("User", back_populates="owner")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def find_by_telegram_id(cls, telegram_id):
        user = cls.query.filter_by(telegram_id=telegram_id).first()
        if not user:
            return None
        return user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    phone = db.Column(db.Integer, )
    note = db.relationship(Note, back_populates="user")


    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    # @classmethod
    # def get_word_by_name(cls, name:str):
    #     word = cls.query.filter_by(name=name).first()
    #     if not word:
    #         return None
    #     return word


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        
