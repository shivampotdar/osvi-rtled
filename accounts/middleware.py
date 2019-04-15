#Session model stores the session data
from django.contrib.sessions.models import Session
from .models import LoggedInUser
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from .views import single_user, time_up
#from django.core.cache import cache, get_cache
from django.core.cache import caches
from importlib import import_module
from django.conf import settings
from django.utils import timezone
from mysite.settings import t_out
from django.contrib.auth.models import User

class OneSessionPerUserMiddleware:
    # Called only once when the web server starts
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        #!!!! BUG --session expire is enabled, so user's session is expired even if the time thing below doesn't log him out
        # but LoggedInUser will still have that entry, due to which someone else won't be able to log in.



        '''if LoggedInUser.objects.count() != 0:
            o = LoggedInUser.objects.all()[0]
            t1 = o.user.last_login
            if (tnow - t1).seconds > t_out:
                print("hi")
            #o.delete()'''
        print(LoggedInUser.objects.count())
        if request.user.is_authenticated:
            #if len(LoggedInUser.objects.all()) > 1:
            if LoggedInUser.objects.count() > 1:
                print("here")
                obj = LoggedInUser.objects.all()[0]
                if obj.user.id == request.user.id:
                    pass
                else:
                    if (timezone.now()-obj.user.last_login).seconds > t_out:
                        user=User.objects.get(pk=obj.user_id)
                        [s.delete() for s in Session.objects.all() if
                         str(s.get_decoded().get('_auth_user_id')) == str(user.id)]
                        #obj.delete()
                    else:
                        return single_user(request)
            tnow = timezone.now()
            tlogin = request.user.logged_in_user.login_time
            if (tnow - tlogin).seconds > t_out:
                if request.user.is_staff or request.user.is_superuser:
                    pass
                else:
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
