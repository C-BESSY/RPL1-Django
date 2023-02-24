from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.CharField(max_length=5, primary_key=True)
    username = models.CharField(max_length=20)
    userpasw = models.CharField(max_length=10)

class Barang(models.Model):
    