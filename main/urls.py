from django.conf.urls import url, include
from django.contrib import admin

from main import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
]
