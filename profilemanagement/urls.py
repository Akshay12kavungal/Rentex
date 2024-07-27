from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_overview, name='profile_overview'),
    path('wallet/', views.my_wallet, name='my_wallet'),
    path('orders/', views.my_orders, name='my_orders'),
    path('add_to_cart/<str:model_name>/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('cart/decrement/<int:item_id>/', views.decrement_cart_item_quantity, name='decrement_cart_item_quantity'),
    path('rent-from-cart/<int:cart_item_id>/', views.rent_from_cart, name='rent_from_cart'),
    path('cart/increment/<int:item_id>/', views.increment_cart_item_quantity, name='increment_cart_item_quantity'),
    path('cart/decrement/<int:item_id>/', views.decrement_cart_item_quantity, name='decrement_cart_item_quantity'),


    path('rent/<str:model_name>/<int:item_id>/', views.rent_item, name='rent_item'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),  # Add this view
    path('order/<int:order_id>/',views.order_details,name='order_details'),
    path('signup/customer/', views.signup_customer, name='signup_customer'),
    path('', views.login_customer, name='login_customer'),
    path('logout/', views.user_logout, name='user_logout'),
]
