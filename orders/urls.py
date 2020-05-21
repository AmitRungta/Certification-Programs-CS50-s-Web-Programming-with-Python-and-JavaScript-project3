"""order URL Configuration """

from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'orders'



urlpatterns = [
    path("", views.index, name="index"),
    url(r'^menu/$', views.index, name="menu"),
    url(r'^cart/$', views.cart_item_list, name="cart"),
    path('cart/delete_item/<int:cartitem_id>', views.delete_cart_item, name="delete_cart_item"),
    path('cart/place_order', views.place_order, name='place_order'),
    path('user/history', views.index, name="order_history"),
    path('item/<int:item_id>', views.add_item, name='add_item'),
    path('manage/order', views.manage_admin_order, name='manage_admin_order'),

]
