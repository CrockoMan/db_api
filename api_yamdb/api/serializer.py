from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # В прошлом уроке fields = '__all__' изменили на:
        fields = ('email', 'username')