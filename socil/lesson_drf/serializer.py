from django.contrib.auth.models import User
from rest_framework import serializers

from lesson_drf.models import Product, Category, Order, Address



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    # Используем вложенный сериализатор для чтения данных о категории
    category = CategorySerializer(read_only=True)
    # И PrimaryKeyRelatedField для записи (создания или обновления продукта)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'category_id']


class UserSerializer(serializers.ModelSerializer):
    username_length = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'username_length']

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен содержать не менее 8 символов.")
        return value

    def get_username_length(self, obj):
        return len(obj.username)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['country'].lower() != 'russia':
            raise serializers.ValidationError("Адреса могут быть созданы только в пределах России.")
        return super().create(validated_data)


class FeedbackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField()
