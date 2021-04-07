from django.urls import path
from products.views import (
    product_detail_view,
    product_create_view,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
    )

app_name = "products"
urlpatterns = [

    path('create', product_create_view, name='create'),
    path('product', product_detail_view, name='product'),
    path('', product_list_view, name='products'),
    
    path('<int:an_id>/', dynamic_lookup_view, name='one_product'),
    path('<int:an_id>/delete', product_delete_view, name='delete'),
]