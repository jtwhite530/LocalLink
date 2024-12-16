from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150)



# Event model linked to the CustomUser
class Event(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    title = models.CharField(max_length=200)  
    description = models.TextField()  
    location = models.CharField(max_length=255)  
    event_date = models.DateField()  
    event_time = models.TimeField()  

    def __str__(self):
        return self.title  