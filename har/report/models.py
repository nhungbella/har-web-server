from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Report(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    accuracy = models.FloatField(null=True, blank=True)
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    update_time = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
      db_table = "report"
    
    def __str__(self):
        return self.name
