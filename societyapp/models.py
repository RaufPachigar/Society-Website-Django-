from django.db import models

# Create your models here.
class Dashboard(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=10)
    Flat_no = models.CharField(max_length=10)
    password = models.models.CharField(max_length=50)
    