from django.urls import path
from .views import *


urlpatterns = [
    path("register/", UserRegistraionAPI.as_view(), name="register"),
    path("login/",UserLoginAPI.as_view(),name="login")
]
