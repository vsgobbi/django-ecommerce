from django.conf.urls import url
from .views import sales_detail, sales_list

app_name = "sales"

urlpatterns = [
    url(r"^$", sales_list, name="sales_list"),
    url(r"^index/$", sales_list, name="sales_list"),
    url(r"^(?P<category_slug>[-\w]+)/$", sales_list, name="sales_list_by_category"),
    url(r"^(?P<id>\d+)/(?P<slug>[-\w]+)/$", sales_detail, name="sales_detail"),
]
