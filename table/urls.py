from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from table.views import Register

urlpatterns = [
    # path('', index, name='index'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('users/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('char_download/', TemplateView.as_view(template_name='chart_download.html'), name='chard_download'),
]