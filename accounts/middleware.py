#Session model stores the session data
from django.contrib.sessions.models import Session
from .models import LoggedInUser
from .views import single_user, time_up
from django.utils import timezone
from mysite.settings import t_out, pi_ip
from django.contrib.auth.models import User
import subprocess


class OneSessionPerUserMiddleware:
    # Called only once when the web server starts
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print(LoggedInUser.objects.count())
        if request.user.is_authenticated:
            if LoggedInUser.objects.count() > 1:
                print("here")
                obj = LoggedInUser.objects.exclude(user_id=request.user.id)
                for i in obj:
                    if (timezone.now()-i.user.last_login).seconds > t_out:
                        user=User.objects.get(pk=i.user_id)
                        [s.delete() for s in Session.objects.all() if str(s.get_decoded().get('_auth_user_id')) == str(user.id)]
                        i.delete()
                    else:
                        return single_user(request)
            tnow = timezone.now()
            tlogin = request.user.logged_in_user.login_time
            if (tnow - tlogin).seconds > t_out:
                if request.user.is_staff or request.user.is_superuser:
                    pass
                else:
                    cmd = " sudo pkill motion"
                    p = subprocess.Popen("sshpass -p samsanjana12 ssh -p22 pi@" + pi_ip + cmd,
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    p.communicate()
                    cmd2 = " python3 /home/pi/runcode/stopit.py"
                    p = subprocess.Popen("sshpass -p samsanjana12 ssh -p22 pi@" + pi_ip + cmd2,
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    p.communicate()
                    cmd3 = "echo samsanjana12 | sudo -S rm -rf ./runcode/data/videos"
                    p = subprocess.Popen("sshpass -p samsanjana12 ssh -p22 pi@" + pi_ip + cmd3,
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    p.communicate()
                    return time_up(request)
            # if there is a stored_session_key  in our database and it is
            # different from the current session, delete the stored_session_key
            # session_key with from the Session table
            stored_session_key = request.user.logged_in_user.session_key
            if stored_session_key and stored_session_key != request.session.session_key:
                Session.objects.get(session_key=stored_session_key).delete()
            request.user.logged_in_user.session_key = request.session.session_key
            request.user.logged_in_user.save()
        response = self.get_response(request)
        return response
        # This is where you add any extra code to be executed for each request/response after
        # the view is called.
        # For this tutorial, we're not adding any code so we just return the response
