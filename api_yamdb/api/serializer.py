from rest_framework import serializers

from reviews.models import Category, Genre, Title, User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # В прошлом уроке fields = '__all__' изменили на:
        fields = ('email', 'username')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['name', 'slug']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        # fields = '__all__'
        fields = ['name', 'slug']


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True,)
    genre = GenreSerializer(many=True, read_only=True,)

    class Meta:
        model = Title
        # fields = '__all__'
        fields = ['id', 'name', 'year', 'description', 'genre', 'category']


class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())
    genre = serializers.SlugRelatedField(slug_field='slug',
                                         many=True,
                                         queryset=Genre.objects.all())

    class Meta:
        model = Title
        # fields = '__all__'
        fields = ['id', 'name', 'year', 'description', 'genre', 'category']

    def to_representation(self, instance):
        #Ответ сформировать из другого сериализатора
        serializer = TitleSerializer(instance)
        return serializer.data
