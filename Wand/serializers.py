from rest_framework import serializers

from Wand.models import Shafts, Tips


class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tips
        fields=('TipId', 'TipName')


class ShaftsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shafts
        fields=('ShaftId', 'ShaftName', 'ShaftMaterial', 'ShaftColor', 'ShaftDateMade')
