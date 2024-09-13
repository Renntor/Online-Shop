from django.urls import path
from product.apps import ProductConfig
from product.views import ProductRetrieveAPIView, ProductListAPIView, CartListCreateAPI

app_name = ProductConfig.name

urlpatterns = [
    path('', ProductRetrieveAPIView.as_view(), name='retrieve_product'),
    path('<slug:slug>/', ProductListAPIView.as_view(), name='list_product'),

    path('cart/<int:pk>', CartListCreateAPI.as_view(), name='create_list_cart')
]
