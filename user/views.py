from base64 import encode
from datetime import date
import json
import logging
from urllib import response

from drf_yasg import openapi
from django.http import JsonResponse
from user.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import User
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.serializers import ValidationError
from .utils import JWTService
from user.tasks import send_user_email_task
# from rest_framework.reverse import reverse

from drf_yasg.utils import swagger_auto_schema

logging.basicConfig(filename='fundoo_note.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Register(APIView):
    """
    create a new class
    """
    
    @swagger_auto_schema(
        operation_summary="register",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='password'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='email'),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='phone_number'),
                'location': openapi.Schema(type=openapi.TYPE_STRING, description='location'),
            }
        ))
    def post(self,request):
        """
        POST METHOD
        """
        try:
            serializer = RegisterSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            username = serializer.data.get('username')
            userid = serializer.data.get('id')
            
            Jwt_services = JWTService()
            token = Jwt_services.encode_token({"user_id": userid, "username": username})
            send_user_email_task.delay(token, serializer.data.get('email'))
            # print(token)

            # send_mail(from_email = settings.EMAIL_HOST_USER,
            #           recipient_list=[serializer.data['email']], 
            #           message='Register first complete this process'
            #                   f'url is http://127.0.0.1:8000/user/verify_token/{token}',
            #           subject='Registration link')

            return Response({"message": "Email Verification", "data": serializer.data}, status=201)
        
        except ValidationError as e:
            logging.exception(e)
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)         
                
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
class Login(APIView):
    """
    Create new class 
    """
    @swagger_auto_schema(
        operation_summary="login user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='password'),
            }
        ))
    def post(self, request):
        """
        create post function
        """
        try:
            user = authenticate(**request.data)
            if not user:
                raise Exception("Invalid Credentials")
            # userid = request.data.get("user_id")
            # print(userid)
            Jwt_services = JWTService()
            token = Jwt_services.encode_token({"user_id": user.id, "username": user.username})

            return Response({"message": "Login Successful", "status": 202, "data": token},
                status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)  




class VerifyToken(APIView):
    """
    create VerifyToken class
    """

    def get(self, request, token=None):
        """
        create get function
        """
        try:
            Jwt_services = JWTService()
            de_token = Jwt_services.decode_token(token)

            user_id = de_token.get("user_id")
            username = de_token.get("username")

            user = User.objects.get(id=user_id, username=username)
            # if user is not None:
            user.is_verified = True
            user.save()
            return Response({"message": "Email is correct"})
            # return Response({"message": "Invalid credentials"})
        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e)})
