"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.contrib.auth.models import User
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from register import endpoints

#'''
#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ('url', 'username', 'email', 'is_staff')

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
    #serializer_class = users.CostumUser

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#'''

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('', include('shop.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(endpoints)),
    url(r'^api/auth/', include('knox.urls')), 
    #url(r'home', include('rest_framework.urls')),
    #url(r'^users/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



