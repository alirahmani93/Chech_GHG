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
def emailing(request):
    # if request.uesr.is_annonymos:
    #     author = request.POST.get("author", None)
    #
    # else:
    #     author = request.user
    try:
        email = request.POST.get("email", None)
        comment = request.POST.get("comment", None)
        current_site = get_current_site(request)
        # message = render_to_string('contact.html',{
        #     'user': email,
        #     'domain': current_site.domain})

        send_mail(email, comment, settings.EMAIL_HOST_USER, ["info.bababarghi@gmail.com","ali93rahmani@gmail.com"],auth_password=settings.EMAIL_HOST_PASSWORD,)

        # messages.success(request, "Register Successfully!")
        return HttpResponse('dame shoma babat feedbacket garm ')

    except IntegrityError as e:
        messages.error(request, f"{e}")
        return redirect('/')




@shared_task(name="summation")
def summation(a, b):
    time.sleep(10)
    return a + b