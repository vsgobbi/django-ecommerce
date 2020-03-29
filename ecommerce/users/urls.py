from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import register_user, register_address
app_name = "users"


urlpatterns = [
    url(r"^$", register_user, name="register_user"),
    url("^address/$", register_address, name="register_address"),
    url(r'^logged_out/$', auth_views.LogoutView.as_view(), name='logget_out'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="register/login.html"), name="login"),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(
        template_name='register/password_reset.html',
        email_template_name='register/password_reset_email.html',
        subject_template_name="Recuperar senha [E-commerce]"), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'), name='password_reset_done'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^password_reset/complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(
        template_name='user/password_reset.html'), name='password_reset'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(
        template_name='user/password_reset_done.html'), name='password_reset_done'),
]
