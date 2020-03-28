"""settings URL Configuration
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cart", include("cart.urls")),
    path("orders", include("orders.urls")),
    path("sales/", include("sales.urls")),
    path("register/", include("users.urls")),
    path("", include("shop.urls")),
    # url(r"^", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^api/auth/", include("knox.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




