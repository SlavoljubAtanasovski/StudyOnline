from django.db import models
from rest_framework import serializers
from school.api.user.models import User

class Payment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    creditcard = models.CharField(max_length=200)
    paypal = models.CharField(max_length=200)
    
    def __str__(self):
        return '{}'.format(user_id)