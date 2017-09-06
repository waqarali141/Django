from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

appname = 'appraisal'
urlpatterns = [
    url(r'^$', login_required(views.Index.as_view()), name='index'),
    url(r'^login$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, name='logout')
]
