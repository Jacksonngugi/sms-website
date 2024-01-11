from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=500)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(contact,on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    status = models.CharField(max_length=20)
    incoming_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.name
    
class unread_sms(models.Model):
    content = models.ForeignKey(Message,on_delete=models.CASCADE)

    def __str__(self):
        return self.content.user.name
    
class chats(models.Model):
    user_name = models.CharField(max_length=500)

    def __str__ (self):
        return self.user_name
    

class sms_count(models.Model):
    sent_sms = models.IntegerField(default=0)
    remaining_sms = models.IntegerField(default=0)
