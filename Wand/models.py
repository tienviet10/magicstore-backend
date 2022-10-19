from datetime import date
from email.policy import default

from django.db import models


# Inheritance.
class BaseItem(models.Model):
    id = models.AutoField(primary_key=True)
    MadeDate = models.DateTimeField(auto_now_add=True)
    MadeOf = models.CharField(max_length=150)
    Color = models.CharField(max_length=150)

    class Meta:
        abstract = True
        ordering = ['id']   

class Rings(BaseItem):
    Power = models.IntegerField()
    class Meta(BaseItem.Meta):
        ordering = ['-MadeDate']   

# OneToOne Model.
class Endcaps(models.Model):
    MadeDate = models.DateTimeField(default = date.today)
    MadeOf = models.CharField(max_length=150)
    Color = models.CharField(max_length=150)

class Topcaps(models.Model):
    endcaps = models.OneToOneField(Endcaps, on_delete=models.CASCADE, primary_key=True)
    SerialNumber = models.IntegerField(default=123456789)

# Normal Models.
class Tips(models.Model):
    TipId = models.AutoField(primary_key=True)
    TipName = models.CharField(max_length=500)

class Shafts(models.Model):
    ShaftId = models.AutoField(primary_key=True)
    ShaftName = models.CharField(max_length=500)
    ShaftMaterial = models.CharField(max_length=150)
    ShaftColor = models.CharField(max_length=150)
    ShaftDateMade = models.DateField()

class MagicWands(models.Model):
    magicWandId = models.AutoField(primary_key=True)
    description = models.TextField()
    pubDate = models.DateField(default=date.today)
    power = models.IntegerField()

class Handles(models.Model):
    HandleId = models.AutoField(primary_key=True)
    MadeDate = models.DateField()
    MadeOf = models.CharField(max_length=150)
    Color = models.CharField(max_length=150)
    AssociatedWand = models.ForeignKey(MagicWands, on_delete=models.CASCADE)

class Owner(models.Model):
    OwnerId = models.AutoField(primary_key=True)
    MagicWand =  models.ManyToManyField(MagicWands)
    FirstName = models.CharField(max_length=250, default="FirstName")
    LastName = models.CharField(max_length=250, default="LastName")



