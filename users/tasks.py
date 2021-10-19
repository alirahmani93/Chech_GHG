import time
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.shortcuts import redirect

from django.db import IntegrityError

from celery import shared_task

@shared_task(name="emailing")
def emailing(email,comment):
    send_mail(email, comment, settings.EMAIL_HOST_USER,
              ["info.bababarghi@gmail.com","ali93rahmani@gmail.com"],auth_password=settings.EMAIL_HOST_PASSWORD,)



@shared_task(name="summation")
def summation(a, b):
    time.sleep(10)
    return a + b