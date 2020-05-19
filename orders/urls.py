from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'orders'



urlpatterns = [
    path("", views.index, name="index"),
    url(r'^menu/$', views.index, name="menu"),
]
