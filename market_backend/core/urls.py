
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


from apps.accounts.urls import accounts_urlpatterns


urlpatterns = [
    path('', TemplateView.as_view(template_name="backend/main.html")),
    path('admin/', admin.site.urls),
]


urlpatterns += accounts_urlpatterns