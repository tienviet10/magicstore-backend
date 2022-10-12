from django.db import models

# Create your models here.

class Tips(models.Model):
    TipId = models.AutoField(primary_key=True)
    TipName = models.CharField(max_length=500)

class Shafts(models.Model):
    ShaftId = models.AutoField(primary_key=True)
    ShaftName = models.CharField(max_length=500)
    ShaftMaterial = models.CharField(max_length=150)
    ShaftColor = models.CharField(max_length=150)
    ShaftDateMade = models.DateField()
