from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'api/users^$', views.UserCreate.as_view(), name='account-create'),
    url(r'^register/$', views.signup, name='register'),
    #re_path(r'^register/$', views.signup, name='register'),
    #url(r'/users^$', name='account-create'),
    #url(r'users^$', views.UserCreate, name='account:create'),
]
