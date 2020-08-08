from mongoengine import *

connect('user_history_details')


class LoginTime(EmbeddedDocument):
    start_date = DateTimeField()
    end_date = DateTimeField()


class Details(Document):
    real_name = StringField(max_length=200)
    tz = StringField(max_length=200)
    activity_periods = ListField(EmbeddedDocumentField(LoginTime))

