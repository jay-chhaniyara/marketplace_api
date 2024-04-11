from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
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
