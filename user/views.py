from datetime import date
import json
import logging
from urllib import response

from django.http import JsonResponse
from user.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404


logging.basicConfig(filename='fundoo_note.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()

class Register(APIView):
    """
    create a new class
    """
    def post(self,request):
        """
        POST METHOD
        """
        try:
            serializer = RegisterSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)
            serializer.save()
                
            return Response({"message": "User added", "data":serializer.data}, status=status.HTTP_201_CREATED)
            # return JsonResponse({"message": "Invalid Request"}, status = 400)
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
class Login(APIView):
    """
    Create new class 
    """

    def post(self, request):
        """
        create new function
        """
        try:
            user = authenticate(**request.data)
            if not user:
                raise Exception("Invalid Credentials")
            return Response({"message": "Login Successful", "status": 202, "data": {}},
                status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)  