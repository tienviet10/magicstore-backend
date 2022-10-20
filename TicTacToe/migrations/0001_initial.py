# Generated by Django 4.1.2 on 2022-10-19 18:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicTacToe',
            fields=[
                ('TicTacToeId', models.AutoField(primary_key=True, serialize=False)),
                ('CurrentPlayer', models.CharField(max_length=2)),
                ('CurrentBoard', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2), size=9)),
            ],
        ),
    ]