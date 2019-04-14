#Session model stores the session data
from django.contrib.sessions.models import Session
from .models import LoggedInUser
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from .views import single_user
#from django.core.cache import cache, get_cache
from django.core.cache import caches
from importlib import import_module
from django.conf import settings

class OneSessionPerUserMiddleware:
    # Called only once when the web server starts
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        #if request.user.is_authenticated:
            #stored_session_key = request.user.logged_in_user.session_key
            # if there is a stored_session_key  in our database and it is
            # different from the current session, delete the stored_session_key
            # session_key with from the Session table
            #if stored_session_key and stored_session_key != request.session.session_key:
             #   Session.objects.get(session_key=stored_session_key).delete()
            #request.user.logged_in_user.session_key = request.session.session_key
            #request.user.logged_in_user.save()
        response = self.get_response(request)
        print(LoggedInUser.objects.count())
        if len(LoggedInUser.objects.all()) > 1:
            #return redirect('/accounts/logout/')
            return single_user(request)
        if request.user.is_authenticated:
            cache = caches['default']
            cache_timeout = 86400
            cache_key = "user_pk_%s_restrict" % request.user.pk
            cache_value = cache.get(cache_key)

            if cache_value is not None:
                if request.session.session_key != cache_value:
                    engine = import_module(settings.SESSION_ENGINE)
                    session = engine.SessionStore(session_key=cache_value)
                    session.delete()
                    cache.set(cache_key, request.session.session_key,
                              cache_timeout)
            else:
                cache.set(cache_key, request.session.session_key, cache_timeout)
        return response
        # This is where you add any extra code to be executed for each request/response after
        # the view is called.
        # For this tutorial, we're not adding any code so we just return the response

'''
class OneSessionPerUserMiddleware:
    def process_request(self, request):
        """
        Checks if different session exists for user and deletes it.
        """
        if len(LoggedInUser.objects.all()) > 1:
            # return redirect('/accounts/logout/')
            return single_user(request)
        if request.user.is_authenticated():
            cache = caches('default')
            cache_timeout = 86400
            cache_key = "user_pk_%s_restrict" % request.user.pk
            cache_value = cache.get(cache_key)

            if cache_value is not None:
                if request.session.session_key != cache_value:
                    engine = import_module(settings.SESSION_ENGINE)
                    session = engine.SessionStore(session_key=cache_value)
                    session.delete()
                    cache.set(cache_key, request.session.session_key,
                              cache_timeout)
            else:
                cache.set(cache_key, request.session.session_key, cache_timeout)
'''