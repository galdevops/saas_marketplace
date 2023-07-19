from django.urls import re_path, include
from .views import *

accounts_urlpatterns = [
    re_path(r'^api/v1/users/test/', users_test, name="users_test"),
    re_path(r'^api/v1/', include('djoser.urls')),
    re_path(r'^api/v1/', include('djoser.urls.authtoken')),
    
]