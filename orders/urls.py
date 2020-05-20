"""order URL Configuration """

from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'orders'



urlpatterns = [
    path("", views.index, name="index"),
    url(r'^menu/$', views.index, name="menu"),
    url(r'^cart/$', views.index, name="cart"),
    path('user/history', views.index, name="order_history"),
    path('item/<int:item_id>', views.add_item, name='add_item'),
    path('manage/order', views.manage_admin_order, name='manage_admin_order'),

]
