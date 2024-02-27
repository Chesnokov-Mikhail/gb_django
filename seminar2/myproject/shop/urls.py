from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetIndex.as_view(), name='get_index'),
    path('product/<int:product_id>/', views.GetProduct.as_view(), name='get_product_id'),
    path('client/<int:client_id>/', views.GetAllOrderClient.as_view(), name='get_all_orders_by_client'),
]