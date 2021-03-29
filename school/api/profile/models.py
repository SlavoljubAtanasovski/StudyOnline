from django.db import models
from user.models import User
from rest_framework import serializers

class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=200)
    user_country = models.CharField(max_length=200)
    user_city = models.CharField(max_length=200)
    user_address = models.CharField(max_length=200)
    user_birthday = models.DateField()
    user_sex = models.IntegerField(default=0)
    
    def __str__(self):
        return '[{}] {}, {}'.format(self.user_id, self.user_name, self.user_email)