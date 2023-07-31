from django.urls import re_path,path
from .views import *

finance_urlpatterns = [
    path('api/v1/payment/', f_test, name="f_test"),
    ]