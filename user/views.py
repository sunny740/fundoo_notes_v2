import json
import logging
# from django.http import HttpResponse

from django.http import JsonResponse
from user.models import User
from django.shortcuts import render

# log = '%(lineno)d ** %(asctime)s ** %(message)s'
# logging.basicConfig(filename='user_views.log', filemode='a', format=log, level=logging.DEBUG)

logging.basicConfig(filename='fundoo_note.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()

def registration(request):
    try:
        data = json.loads(request.body)
        if request.method == 'POST':

            user_registration = User.objects.create(username=data.get("user_name"), password=data.get("password"),
                                                    first_name=data.get("first_name"), last_name=data.get("last_name"),
                                                    email=data.get("email"), phone_number=data.get("phone_number"),
                                                    location=data.get("location"))

            return JsonResponse({"message": f"Data save successfully {user_registration.username}",
                                 "data": {"id": user_registration.id}})

        return JsonResponse({"message": "Method not allow"})
    except Exception as e:
        logger.exception(str(e))
        return JsonResponse({"message": "Unexpected error"})


def login(request):
    try:
        data = json.loads(request.body)

        if request.method == 'POST':
            login_user = User.objects.filter(username=data.get("username"), password=data.get("password")).first()
            if login_user is not None:
                return JsonResponse({'message': f'User {login_user.username} is successfully login'})
            else:
                return JsonResponse({'message': 'Invalid username/password'})
        return JsonResponse({'message': 'Method not allow'})
        
    except Exception as e:
        logger.exception(str(e))
        return JsonResponse({'message': 'Unexpected error'})