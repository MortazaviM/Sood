from django.db import models
from django.contrib.postgres.fields import JSONField
from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.
class data(Document):
    TICKER=fields.StringField()
    DTYYYYMMDD=fields.IntField()
    OPEN=fields.FloatField()
    HIGH=fields.FloatField()
    LOW=fields.FloatField()
    CLOSE=fields.FloatField()
    VOL=fields.IntField()
    Value=fields.FloatField()
    TEDAD=fields.IntField()

