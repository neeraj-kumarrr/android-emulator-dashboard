from .models import AndroidApp
from rest_framework import serializers

class AndroidAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidApp
        fields = '__all__'
