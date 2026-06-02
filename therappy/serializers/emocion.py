from rest_framework import serializers
from therappy.models.emocion import Emocion

class EmocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emocion
        fields = '__all__'
