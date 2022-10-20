from rest_framework import serializers

from TicTacToe.models import TicTacToe


class TicTacToeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TicTacToe
        fields=('TicTacToeId', 'CurrentPlayer', 'CurrentBoard')

