from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from ads.models import Location, User, Category, Ad, Selection


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_password(self, value: str) -> str:
        return make_password(value)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        exclude = ["items"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True, )

    class Meta:
        model = Selection
        fields = "__all__"

class SelectionCreateOrUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = "__all__"
