# Generated by Django 4.1.2 on 2022-10-24 16:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicTacToe', '0005_alter_tictactoe_currentboard_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tictactoe',
            name='CurrentBoard',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5), default=['', '', '', '', '', '', '', '', ''], size=9),
        ),
        migrations.AlterField(
            model_name='tictactoe',
            name='Player1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5), default=[], size=5),
        ),
        migrations.AlterField(
            model_name='tictactoe',
            name='PlayerO',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5), default=[], size=5),
        ),
    ]