from rest_framework import serializers
from .models import list_app

class list_appSerializer(serializers.ModelSerializer):
    class Meta:
        model = list_app
        fields = ['name','genre','platform', 'vid', 'population', 'image', 'name_1', 'price_1', 'image_1', 'name_2', 'price_2', 'image_2', 'name_3', 'price_3', 'image_3']