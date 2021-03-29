from django.db import models
from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers
from school.api.payment.models import Payment
from user.models import User
from school.api.subject.models import Subject

class Lecture(models.Model):
    teacher = models.OneToOneField(to=User, on_delete=models.CASCADE)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    video_urls = ArrayField(models.CharField(max_length=200), blank=True)
    photo_urls = ArrayField(models.CharField(max_length=200), blank=True)
    
    def __str__(self):
        return '[{}] {}'.format(self.teacher, self.subject)
    