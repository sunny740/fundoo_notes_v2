import jwt
import logging
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from user.utils import JWTService
from user.models import User


def verify_token(function):
    """
    verify_token
    """
    def wrapper(self, request, *args, **kwargs):
        token = request.headers.get('Token')
        
        jwt_service = JWTService()
        decodetoken = jwt_service.decode_token(token)
        print(decodetoken)
        user_id = decodetoken.get('user_id')
        
        if not user_id:
            raise Exception('user does not found')
        request.data.update({'user': user_id})
        return function(self, request, *args, **kwargs)

    return wrapper




# def verify_token(function): 

#     def wrapper(self, request):
#         if 'HTTP_TOKEN' not in request.META:
#             token = request.META.get("HTTP_TOKEN")    
#             resp = Response({'message': 'Token not provided in the header'})
#             resp.status_code = 400
#             logging.info('Token not provided in the header')
#             return resp
        
#         payload = JWTService.decode_token(token=token)
#         request.data.update({'user': payload.get('user_id')})

#         return function(self, request) 

#     return wrapper    