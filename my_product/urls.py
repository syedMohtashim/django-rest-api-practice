from django.urls import path

from .views.views import (
    ProductDetailViewAPI, 
    ProductListCreateViewAPI,
    product_alt_view,
    ProductUpdateViewAPI,
    ProductMixinViews
    )

urlpatterns = [
    # path("", ProductListCreateViewAPI.as_view(), name = 'product-list-create'),
    path("<int:pk>/", ProductDetailViewAPI.as_view(), name='product-detail'),
    path("<int:pk>/update/",ProductUpdateViewAPI.as_view()),

    # This ProductMixinViews handle three views, namely ;
    # 1) ListAPIView 
    # 2) CreateAPIView 
    # 3) DetailAPIView 
    path("", ProductMixinViews.as_view()), # List, Create
    # path("<int:pk>/detail/", ProductMixinViews.as_view()), # Detail
    # path("list/", product_alt_view),
    # path("create/",product_alt_view ),
    
    
    # path("<int:pk>/",product_alt_view )
]
