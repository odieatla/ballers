from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django.contrib import admin
from court import views as court_views
from court.api import LoginResource

admin.autodiscover()

login_resource = LoginResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ballers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', court_views.index, name='index'),
    #url(r'', include(login_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', court_views.login, name="login"),
    url(r'^logout', court_views.logout, name="logout"),
    url(r'^signup', court_views.signup, name="signup"),
)
