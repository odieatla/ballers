from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.cache import never_cache
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from court.forms import LoginForm, SignupForm
import logging
logger = logging.getLogger(__name__)

@never_cache
def index(request, **kwargs):
    logger.error("hello??")
    if request.user.is_authenticated():
        logger.debug('logged in')
    else:
        logger.debug('not in..')
    return render_to_response('court/index.html')

def login(request, **kargs):
    if request.method == "POST":
        logger.debug("POST")
        login_form = LoginForm(request.POST, prefix='login')

        if login_form.is_valid():
            auth.login(request, login_form.user)
            return HttpResponseRedirect(reverse('index'))
    else:
        logger.debug("not post")
        login_form  = LoginForm(prefix='login')
    return render(request, 'court/login.html', {'form': login_form})

def logout(request, **kargs):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request, **kargs):
    if request.method == "POST":
        logger.debug('sign up action')
        signup_form = SignupForm(prefix='signup', data=request.POST)
        if signup_form.is_valid():
            new_user = signup_form.save()
            auth.login(request, new_user)
            return HttpResponseRedirect(reverse('index'))
    else:
        logger.debug('sign up form')
        signup_form = SignupForm(prefix='signup')
    #return HttpResponseRedirect(reverse('index'))
    return render(request, 'court/signup.html', {'form': signup_form})
