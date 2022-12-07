from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from table.views import Register, TableDownloadView, ChartShowView

urlpatterns = [
    # path('', index, name='index'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('users/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('char_download/', TableDownloadView.as_view(), name='chart_download_show'),
    path('chart_view/', ChartShowView.as_view(), name='chart_view'),
]