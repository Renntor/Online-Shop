from django.urls import path
from category.apps import CategoryConfig
from category.views import CategoryListAPIView, CategoryRetrieveAPIView


app_name = CategoryConfig.name

urlpatterns = [
    path('', CategoryRetrieveAPIView.as_view(), name='retrieve_category'),
    path('<slug:slug>/', CategoryListAPIView.as_view(), name='list_category')
 ]
