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
    path('cart/confirm_order', views.confirm_order, name='confirm_order'),
    path('cart/place_order', views.place_order, name='place_order'),
    path('user/history', views.order_history, name="order_history"),
    path('user/order_detail/<int:order_id>', views.order_detail, name="order_detail"),
    path('cart/add_item/<int:item_id>', views.add_item, name='add_item'),
    path('manage/order', views.manage_admin_order, name='manage_admin_order'),

]
