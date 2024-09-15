from django.urls import path
from product.apps import ProductConfig
from product.views import ProductRetrieveAPIView, ProductListAPIView, CartListCreateAPI, \
    CartUpdateAPIView, CartDestroyAPIView, CartsDestroyAPIView

app_name = ProductConfig.name

urlpatterns = [
    path('product/<slug:slug>/', ProductRetrieveAPIView.as_view(), name='retrieve_product'),
    path('', ProductListAPIView.as_view(), name='list_product'),

    path('cart/', CartListCreateAPI.as_view(), name='list_create_cart'),
    path('cart/update/', CartUpdateAPIView.as_view(), name='update_cart'),
    path('cart/destroy/', CartDestroyAPIView.as_view(), name='destroy_cart'),
    path('carts/destroy/', CartsDestroyAPIView.as_view(), name='destroy_carts'),
]
