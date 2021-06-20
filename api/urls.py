from django.urls import re_path
from .views import ScidProxyView

urlpatterns = [
    re_path(r'scid/(?P<path>.*)', ScidProxyView.as_view(), name='put_customer-detail'),
]