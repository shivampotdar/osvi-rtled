from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from accounts.models import LoggedInUser
from django.contrib.sessions.models import Session
from django.utils import timezone
import os
#import RPi.GPIO as GP
from fabric import Connection
from mysite.settings import pi_ip
import subprocess


@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))
    #LoggedInUser.login_time
    request.user.logged_in_user.login_time = timezone.now()
    request.user.logged_in_user.save()

@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    cmd = " sudo pkill motion"
    #c = Connection(host=pi_ip, user='pi', connect_kwargs={'password': 'samsanjana12'})
    #c.run(cmd)
    p = subprocess.Popen("sshpass -p samsanjana12 ssh -p22 pi@" + pi_ip + cmd,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()
    cmd2 = " python3 /home/pi/runcode/stopit.py"
    p = subprocess.Popen("sshpass -p samsanjana12 ssh -p22 pi@" + pi_ip + cmd2,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()
    #GP.cleanup()
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()
