from rest_framework import (
    generics, mixins, 
    # permissions, authentication
    )
from rest_framework.decorators import (
    api_view
)
from rest_framework.response import Response
from .models import Product
from .serializers import (
    ProductSerializer
    )
from django.shortcuts import get_object_or_404

# from rest_framework import permissions

# from ..my_api.permissions import IsStaffEditorPermission
from my_api.permission_mixins import StaffEditorPermissionMixin


# -----------------
# Class Based Views
# -----------------
class ProductMixinViews(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    """
    Product Mixin View provides the GET and POST functionality.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # For Detail View
    

    def get(self, request, *args, **kwargs):
        """
        An http GET request.

        :param request: Request sent by a user.
        :param args: Non-keyword arguments.
        :param kwargs: Keyword arguments.
        """
        print("-----------------------------")
        print(f"ARGS: {args}")
        print("-----------------------------")
        print(f"KWARGS: {kwargs}")
        print("-----------------------------")
        
        # For Detail View
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        An http POST request.

        :param request: Request sent by a user.
        :param args: Non-keyword arguments.
        :param kwargs: Keyword arguments.
        """
        print("-----------------------------")
        print(f"ARGS: {args}")
        print("-----------------------------")
        print(f"KWARGS: {kwargs}")
        print("-----------------------------")
        return self.create(request, *args, **kwargs)

 
#=======================================


class ProductDetailViewAPI(
    generics.RetrieveAPIView , 
    StaffEditorPermissionMixin
    ):
    """
    Product Detail View API.
    """

    # """
    #     I replaced the permission_classes 
    #     by StaffEditorPermissionMixin
    # """
    # permission_classes = [IsStaffEditorPermission] # --> Custom permission class

    # <!-- Donot change the variable names ( phat jaye ga code !!) -->
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk' --> We will use this in UpdateViewAPI only

class ProductListCreateViewAPI(
    generics.ListCreateAPIView, 
    StaffEditorPermissionMixin
    ):
    """
    API which provides both list and create functionality.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication
    # ]

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.DjangoModelPermissions]
    # """
    #     I replaced the permission_classes 
    #     by StaffEditorPermissionMixin
    # """
    # permission_classes = [IsStaffEditorPermission] # --> Custom permission class 


class ProductUpdateViewAPI(generics.UpdateAPIView, StaffEditorPermissionMixin):
    """
    Product Update View API , used to update a product.
    """
    # """
    #     I replaced the permission_classes 
    #     by StaffEditorPermissionMixin
    # """
    # permission_classes = [IsStaffEditorPermission] # --> Custom permission class

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        """
        Method which will perform update action.

        :param serializer: A data serializer.
        """
        instance = serializer.save()
#########################################################################
# USE EITHER OF THESE ( ProductCreateAPIView or ProductListCreateAPIView )
# ProductListCreateAPIView performs the functionality of both 
# ProductListViewAPI and ProductCreateAPIView
#########################################################################

# class ProductListViewAPI(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

@api_view(['GET', 'POST'])
def product_alt_view(request, pk = None, *args, **kwargs):

    """
    A function based view which performs both Http GET and POST request.

    :param request: A request sent by the user.
    :param pk: A primary key of a specific product (None by default).
    :param args: Non-keyword arguments.
    :param kwargs: Keyword arguments.
    """
    print("===============================")
    print("WE're in the VIEW")
    print("===============================")
    if request.method == 'GET':
        if pk is not None:
            # Detail View
            obj = get_object_or_404(Product, pk = pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)
        else:
            # List View
            #""" 
            #List a queryset.
            #"""
            list_of_objects_or_querrysets = Product.objects.all()
            data = ProductSerializer(list_of_objects_or_querrysets, many = True).data

            return Response(data)
    if request.method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            instance  = serializer.save()
            return Response(serializer.data)
        # return Response({"NONE":"NONE"})    
