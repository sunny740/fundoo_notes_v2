import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fundoo_notes_v2.settings")
app = Celery("fundoo_notes_v2")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

























# from time import sleep

# from celery import shared_task
# from django.conf import settings
# from django.core.mail import send_mail
# from rest_framework.reverse import reverse


# @shared_task()
# def send_user_email_task(token, email_id):
#     """
#     Sends an email when user is created
#     """
#     sleep(2)
#     send_mail(
#         subject='PyJWT Token',
#         message=settings.BASE_URL + reverse('verify_token_api', kwargs={"token": token}),
#         from_email=None,
#         recipient_list=[email_id]
#     )