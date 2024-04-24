from rest_framework import serializers
from choucair_testing_app.models import Products

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, required=True, max_length=100)
    password = serializers.CharField(allow_blank=False, required=True, max_length=100)


class UserRegisterSerializr(serializers.Serializer):
    first_name = serializers.CharField(allow_blank=False, required=True, max_length=100)
    last_name = serializers.CharField(allow_blank=False, required=True, max_length=100)
    username = serializers.CharField(allow_blank=False, required=True, max_length=100)
    password = serializers.CharField(allow_blank=False, required=True, max_length=100)
    email = serializers.CharField(allow_blank=False, required=True, max_length=100)

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "product_id",
            "product_name",
            "description",
            "price",
            "stock",
            "product_image",
            "create_date",
            "update_date"
        ]

class GetProductSerializer(serializers.Serializer):
    product_id = serializers.CharField(allow_blank=False, required=True, max_length=100)

class UpdateproductSerializer(serializers.Serializer):
    product_id = serializers.CharField(allow_blank=False, required=True, max_length=100)
    product_name = serializers.CharField(allow_blank=False, required=True, max_length=100)
    description = serializers.CharField(allow_blank=False, required=True, max_length=100)
    price = serializers.IntegerField(required=True)
    stock = serializers.IntegerField(required=True)
    product_image = serializers.ImageField(required=True)
    update_date = serializers.DateField(required=False)

class DeleteProductSerializer(serializers.Serializer):
    product_id = serializers.CharField(allow_blank=False, required=True, max_length=100)
