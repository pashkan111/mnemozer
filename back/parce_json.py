from marshmallow import Schema, fields, EXCLUDE


class UserSchema(Schema):
    id = fields.Int()
    phone = fields.Int()
    telegram = fields.Int()
    name = fields.Str(allow_none=True, missing=False)
    email = fields.Str(allow_none=True, missing=False)
    registration = fields.Date()
    password = fields.Str()
    messangers = fields.Str(allow_none=True, missing=False)

    @classmethod
    def get_user_data(cls, data):
        user_schema = cls(unknown=EXCLUDE)
        user = user_schema.load(data)
        return user


class NoteSchema(Schema):
    id = fields.Int(allow_none=True)
    name = fields.Str(allow_none=True, missing=False)
    description = fields.Str(allow_none=True, missing=False)
    date_created = fields.Date(allow_none=True)
    date_remind = fields.Date(allow_none=True)
    time = fields.Time(allow_none=True)
    # status = fields.Boolean(allow_none=True, missing=False)
    # user = fields.Nested(UserSchema)


    @classmethod
    def get_note(cls, data):
        note_schema = cls(unknown=EXCLUDE)
        date = note_schema.load(data)
        return date