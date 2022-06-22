from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=24)
    info = models.CharField(max_length=256)
    rodo = models.CharField(max_length=128)
