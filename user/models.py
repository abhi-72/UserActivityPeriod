from django.db import models
import pytz

class User(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones,pytz.all_timezones))
    name = models.CharField(max_length=70)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    ref_id = models.CharField(max_length=10)


class Activity(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
