from dataclasses import field
from wsgiref.validate import validator
from rest_framework import serializers

from .models import Product
from .validators import validate_title, UniqueValidator


class ProductSerializer(serializers.ModelSerializer):
    """
    A product serializer.
    """
    manual_url = serializers.SerializerMethodField(read_only = True)
    aatomatic_url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk') # --> This works only for ModelSerializers!
    title = serializers.CharField(validators = [validate_title, UniqueValidator])
    class Meta:
        model = Product
        fields = [
            'user',
            'manual_url',
            'aatomatic_url',
            'title',
            'content',
            'price',
            'discounted_price'
        ]


    # """
    #     Validators have been moved into 
    #     my_products app.
    # """

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"Title already taken.")

    def get_manual_url(self, obj):
        """
        To get a manual URL.
        
        :param obj: An object.
        """
        return f'/api/product/{obj.pk}/'