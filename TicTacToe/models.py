from django.contrib.postgres.fields import ArrayField
from django.db import models


class TicTacToe(models.Model):
    TicTacToeId = models.AutoField(primary_key=True)
    CurrentPlayer = models.CharField(max_length=2)
    CurrentBoard = ArrayField(models.CharField(max_length=5, blank=True), size=9, blank=True)

