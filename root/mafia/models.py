from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    is_alive=models.BooleanField(default=True)