from django.conf.urls import url
from .api import RegistrationAPI, LoginAPI, UserAPI
from .views import register_user

app_name = "register"


urlpatterns = [
    url(r"^$", register_user, name="register_user"),
    url("^auth/register/$", RegistrationAPI.as_view()),
    url("^auth/login/$", LoginAPI.as_view()),
    url("^auth/user/$", UserAPI.as_view()),
]
