from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'orders'



urlpatterns = [
    path("", views.index, name="index"),
    url(r'^menu/$', views.index, name="menu"),
    url(r'^cart/$', views.index, name="cart"),
    url(r'^order/$', views.index, name="order"),
    path('item/<int:item_id>', views.additem, name='additem'),
    path('manageadmin/order', views.manage_admin_order, name='manage_admin_order'),

]
