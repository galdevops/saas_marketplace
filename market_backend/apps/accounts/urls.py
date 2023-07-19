from django.urls import re_path, include
from .views import *

accounts_urlpatterns = [
    re_path(r'^api/v1/accounts/test/', d_test, name="d_test"),
    re_path(r'^api/v1/', include('djoser.urls')),
    re_path(r'^api/v1/', include('djoser.urls.authtoken')),
    
]