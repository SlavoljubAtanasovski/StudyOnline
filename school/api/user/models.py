from django.db import models
from rest_framework import serializers

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=200)
    user_country = models.CharField(max_length=200)
    user_city = models.CharField(max_length=200)
    user_address = models.CharField(max_length=200)
    user_birthday = models.DateTimeField('birthday')
    user_sex = models.IntegerField(default=0)
    
    def __str__(self):
        return '[{}] {}, {}'.format(self.user_id, self.user_name, self.user_email)