from django.urls import path
from product.apps import ProductConfig
from product.views import ProductRetrieveAPIView, ProductListAPIView, CartListCreateAPI, \
    CartUpdateAPIView

app_name = ProductConfig.name

urlpatterns = [
    path('product/<slug:slug>/', ProductRetrieveAPIView.as_view(), name='retrieve_product'),
    path('', ProductListAPIView.as_view(), name='list_product'),

    path('cart/', CartListCreateAPI.as_view(), name='post_list_cart'),
    path('cart/update/', CartUpdateAPIView.as_view(), name='update_cart')
]
