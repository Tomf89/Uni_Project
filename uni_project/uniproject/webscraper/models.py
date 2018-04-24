
# from django.db import models
from mongoengine import *
from django.db import models
# from django.contrib.auth.models import User

connect("test")

class Rise_against(Document):
	event_day = IntField(required=False)
	event_month = StringField(required=False)
	event_year = IntField(required=False)
	event_url = StringField(required=True)
	event_venue = StringField(required=True)
	event_city_country = StringField(required=True)