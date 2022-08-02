from pickle import GET
# from django.shortcuts import render
# from django.http import JsonResponse
import json
from my_product.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_product.serializers import ProductSerializer


@api_view(['GET'])
def home_api(request, *args, **kwargs):
    """
    DRF API VIEW TO GET DATA
    """
    # Serialization: 
    # 1) Take a model instance 
    # 2) Convert it into a python dict 
    # 3) Send a json response to the clients

    # 1) Take a model instance
    instance = Product.objects.all().order_by("?").first()
    data = {}
    try:
        # 2) Convert it into a python dict 
        # data['id'] = api_data.id
        # data['title'] = api_data.title
        # data['content'] = api_data.content
        # data['price'] = api_data.price

        # data = model_to_dict(api_data)

        data = ProductSerializer(instance).data

    except:

        data = model_to_dict(instance)

    
    # 3) Send a json response
    # return JsonResponse(data)
    return Response(data)

# This was data-injestion
@api_view(['POST'])
def post_home_api(request, *args, **kwargs):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # print(serializer.data)

        instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
        
    # return Response({"Invalid Data":" YOU TOOK AN L "})

    
# def home_api(request, *args, **kwargs):
#     print("============================")
#     print(request.GET)  # Prints my url querry prameters (params in the requests.get()) 
#     print("============================")
#     print(request.POST)
#     print("============================")
#     print(request.headers)
#     print("============================")
#     body = request.body # Byte string of json data
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     # print(data)
#     return JsonResponse(data)
    # return JsonResponse({"Response":"MY #$ RESPONSE"})