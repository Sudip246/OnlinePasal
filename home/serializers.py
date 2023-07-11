from rest_framework import serializers
from .models import *


# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"
