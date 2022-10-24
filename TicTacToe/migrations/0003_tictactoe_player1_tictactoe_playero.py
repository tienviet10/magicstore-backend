# Generated by Django 4.1.2 on 2022-10-24 16:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicTacToe', '0002_alter_tictactoe_currentboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='tictactoe',
            name='Player1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5), blank=True, default=[], size=5),
        ),
        migrations.AddField(
            model_name='tictactoe',
            name='PlayerO',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5), blank=True, default=[], size=5),
        ),
    ]
