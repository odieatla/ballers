from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.shortcuts import render_to_response

@never_cache
def index(request, **kwargs):
    return render_to_response('court/index.html')

def login(request, **kargs):
    return render_to_response('court/login.html')
