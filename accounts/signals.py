from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from accounts.models import LoggedInUser
from django.contrib.sessions.models import Session
from django.utils import timezone
import os
#import RPi.GPIO as GP

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))
    #LoggedInUser.login_time
    request.user.logged_in_user.login_time = timezone.now()
    request.user.logged_in_user.save()

@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    cmd = " var=$(pidof motion) && echo samsanjana12 | sudo -S kill $var"
    #GP.cleanup()
    os.system(cmd)
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()
