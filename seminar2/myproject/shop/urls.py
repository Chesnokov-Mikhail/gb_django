from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetIndex.as_view(), name='get_index'),
    path('product/<int:product_id>/', views.GetProduct.as_view(), name='get_product_id'),
    path('clients/', views.GetClients.as_view(), name='get_clients'),
    path('client/<int:client_id>/', views.GetAllOrderClient.as_view(), name='get_all_orders_by_client'),
    path('products/<int:client_id>/', views.GetAllProductsByOrdersClient.as_view(), name='get_all_products_orders_by_client'),
    path('image_product/', views.PostImageProduct.as_view(), name='post_image_product'),
]