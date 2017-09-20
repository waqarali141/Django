from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'appraisal'
urlpatterns = [
    # url(r'^$', login_required(views.Index.as_view()), name='index'),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^detail/user/(?P<pk>[0-9 a-z A-Z]+)$', views.DetailUserView.as_view(),  name='detail'),
    url('feedback/user/(?P<pk>[0-9 a-z A-Z]+)$', views.add, name='feedback'),
    url('feedback/delete/(?P<pk>[0-9 a-z A-Z]+)/(?P<user_id>[0-9 a-z A-Z]+)', views.AuthorDelete.as_view(), name='delete_appraisal')
    ]

