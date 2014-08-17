from django.conf.urls import patterns, include, url
from django.contrib import admin
from court import views as court_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ballers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', court_views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
