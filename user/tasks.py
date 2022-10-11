from time import sleep

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.reverse import reverse


@shared_task()
def send_user_email_task(token, email_id):
        """Sends an email when user is created"""
  
        send_mail(from_email = settings.EMAIL_HOST_USER,
                      recipient_list=[email_id],
                      message= f'Register first complete this process url is http://127.0.0.1:8000/user/verify_token/{token}',
                      subject='Registration link')

        print("hi")
        return "message sent"