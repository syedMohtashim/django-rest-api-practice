from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token


from .views import (
    home_api, 
    post_home_api
)


urlpatterns = [
    path("auth/", obtain_auth_token),
    path("", post_home_api)
]
