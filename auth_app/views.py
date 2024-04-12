from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .models import *
from .serializers import *


class UserRegistraionAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = AccountSerializer

    @swagger_auto_schema(
        tags=["Authentication"],
        request_body=AccountSerializer,
        operation_description="Endpoint for user registration.",
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                "status": True,
                "message": "Your account has been registered successfully!",
            }

            return Response(data, status.HTTP_201_CREATED)


class UserLoginAPI(APIView):
    @swagger_auto_schema(
        tags=["Authentication"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="string"),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="string"
                ),
            },
        ),
    )
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        print(user, "------------")

        if user is not None:
            login(request, user)

            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)

            data = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "access_token": access_token,
                "refresh_token": str(refresh_token)
            }

            response_data = {
                "status": True,
                "message": "Login Successful!",
                "data": data
            }

            return Response(data=response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                "status": False,
                "message": "Login UnSuccessful!",
            }
            return Response(data=response_data, status=status.HTTP_200_OK)
