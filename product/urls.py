from django.urls import path
from product.apps import ProductConfig
# from product.views import ...


app_name = ProductConfig.name

urlpatterns = [
#     path('', ProductRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_product'),
#     path('<slug:slug>/', ProductListCreateAPIView.as_view(), name='list_create_product')
]
