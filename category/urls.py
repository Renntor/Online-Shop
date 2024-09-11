from django.urls import path
from category.apps import CategoryConfig
from category.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView


app_name = CategoryConfig.name

urlpatterns = [
    path('', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_category'),
    path('<slug:slug>/', CategoryListCreateAPIView.as_view(), name='list_create_category')
]
