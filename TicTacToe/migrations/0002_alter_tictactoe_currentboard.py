# Generated by Django 4.1.2 on 2022-10-19 19:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicTacToe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tictactoe',
            name='CurrentBoard',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5), blank=True, size=9),
        ),
    ]
