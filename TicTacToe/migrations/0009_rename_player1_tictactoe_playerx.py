# Generated by Django 4.1.2 on 2022-10-24 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TicTacToe', '0008_alter_tictactoe_player1_alter_tictactoe_playero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tictactoe',
            old_name='Player1',
            new_name='PlayerX',
        ),
    ]