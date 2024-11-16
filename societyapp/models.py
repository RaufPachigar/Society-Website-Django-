# models.py
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=10)
    contact_info = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
