from django.urls import path
from subcategory.apps import SubcategoryConfig
from subcategory.views import SubcategoryRetrieveAPIView, SubcategoryListAPIView

app_name = SubcategoryConfig.name

urlpatterns = [
    path('', SubcategoryListAPIView.as_view(), name='list_subcategory'),
    path('<slug:slug>/', SubcategoryRetrieveAPIView.as_view(), name='retrieve_subcategory'),
]