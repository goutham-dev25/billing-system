from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.menu, name='menu'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('get_cart_data/', views.get_cart_data, name='get_cart_data'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('sales_report/', views.sales_report, name='sales_report'),
]