from my_product.models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

def validate_title(value):
        """
        A function to validate if the Product title is already taken or not.

        :param value: Title to be validated.
        :raises ValidationError: Title already taken error.
        """
        qs = Product.objects.filter(title__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"Title already taken.")


unique_product_validator = UniqueValidator(Product.objects.all())