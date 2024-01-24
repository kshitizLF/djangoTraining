from rest_framework import serializers
from rest.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

# class CarSerializer(serializers.Serializer):
#     company = serializers.CharField(max_length=40)
#     model = serializers.CharField(max_length=40)
