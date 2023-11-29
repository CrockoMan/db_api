from rest_framework import serializers

from api_yamdb.reviews.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # В прошлом уроке fields = '__all__' изменили на:
        fields = ('email', 'username')