from django.urls import path
from product.apps import ProductConfig
from product.views import ProductRetrieveAPIView, ProductListAPIView


app_name = ProductConfig.name

urlpatterns = [
    path('', ProductRetrieveAPIView.as_view(), name='retrieve_product'),
    path('<slug:slug>/', ProductListAPIView.as_view(), name='list_product')
]
