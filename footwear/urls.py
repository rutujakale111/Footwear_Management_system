from django.urls import path
from . import views

urlpatterns = [
    path('', views.footwear_list, name='footwear_list'),
    path('order/<int:footwear_id>/', views.place_order, name='place_order'),
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),
]