from django.conf.urls import url
from .views import order_create

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', order_create, name='order_create')
]
