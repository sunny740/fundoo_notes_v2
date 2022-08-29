import json
import logging

from django.http import JsonResponse
from user.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate


logging.basicConfig(filename='fundoo_note.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()

def registration(request):
    try:
        
        if request.method == 'POST':
            data = json.loads(request.body)
            User.objects.create_user(**data)

            return JsonResponse({"message": "User added"})
        return JsonResponse({"message": "Invalid Request"}, status = 400)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message": str(e)}, status = 400)


def login(request):
    
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user is not None:
                return JsonResponse({"message": "Login Successful"})
            return JsonResponse({"message": "Invalid"})
        return JsonResponse({"message": "Invalid Request"})
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message": str(e)})