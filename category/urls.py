from django.urls import path
from category.apps import CategoryConfig
from category.views import CategoryListAPIView, CategoryRetrieveAPIView


app_name = CategoryConfig.name

urlpatterns = [
    path('<slug:slug>/', CategoryRetrieveAPIView.as_view(), name='retrieve_category'),
    path('', CategoryListAPIView.as_view(), name='list_category')
 ]
