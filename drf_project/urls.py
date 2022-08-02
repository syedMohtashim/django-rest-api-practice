from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("my_api.urls")),
    path("api/search/", include("search.urls")),
    path("api/product/", include("my_product.urls")),
    path("api/v2/", include("drf_project.routers"))
]
